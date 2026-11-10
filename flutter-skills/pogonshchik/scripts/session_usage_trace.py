#!/usr/bin/env python3
"""Export usage/action metadata for one Codex chat, never transcript or source bodies."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
import shlex
import uuid

USAGE_KEYS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens',
              'output_tokens', 'reasoning_output_tokens', 'total_tokens')
PATH_PATTERN = re.compile(r'\.(?:dart|md|json|jsonl|yaml|yml|txt|py|sh|ps1|xml|gradle|kts)$')


def command_text(item):
    value = item.get('command', '')
    return value[-1] if isinstance(value, list) and value else value if isinstance(value, str) else ''


def read_paths(command, parsed):
    """Observed explicit shell read targets, not a complete dynamic file-access trace."""
    paths = {x['path'] for x in parsed if x.get('type') == 'read' and isinstance(x.get('path'), str)}
    # Do not inspect generated code/heredoc bodies as if they were shell commands.
    first = command.split('<<', 1)[0]
    for part in re.split(r';|&&|\|\|', first):
        try:
            tokens = shlex.split(part.split('|', 1)[0])
        except ValueError:
            continue
        if not tokens or tokens[0] not in ('cat', 'head', 'tail', 'sed') or any('>' in x for x in tokens):
            continue
        for token in tokens[1:]:
            if not token.startswith('-') and PATH_PATTERN.search(token) and '$' not in token:
                paths.add(token)
    return sorted(paths)


def action_tags(command, paths):
    tags = set()
    if 'library/' in command or 'CIN-MOT' in command:
        tags.add('design-library')
    if any('/lib/' in '/' + x or x.startswith('test/') for x in paths):
        tags.add('source-read')
    if any(x.endswith(('.md', '.yaml', '.yml', '.json')) for x in paths):
        tags.add('document-read')
    if re.search(r'flutter\s+(?:test|analyze)|pytest|dart\s+analyze', command):
        tags.add('verification')
    if re.search(r'flutter\s+build|check.release', command):
        tags.add('build-release')
    if re.search(r'adb|screencap|screenrecord|device_ui|ffmpeg|ffprobe|qlmanage', command):
        tags.add('device-capture')
    if re.search(r'<<|apply_patch|write_text\(|write_bytes\(', command):
        tags.add('script-or-edit')
    return sorted(tags or {'other'})


def feedback_metadata(payload):
    output = payload.get('output')
    texts, images = [], 0
    if isinstance(output, str):
        texts.append(output)
    elif isinstance(output, list):
        for block in output:
            if not isinstance(block, dict):
                continue
            if block.get('type') in ('input_text', 'text'):
                texts.append(block.get('text', ''))
            elif block.get('type') in ('input_image', 'image'):
                images += 1
    text = '\n'.join(texts)
    # Image data is not treated as text tokens or exported.
    text = re.sub(r'data:image/[^\s"\']+', '[image data omitted]', text)
    return {'call_id': payload.get('call_id'), 'text_chars': len(text),
            'image_blocks': images,
            'truncated': bool(re.search(r'Warning: truncated output|output truncated|original token count:', text, re.I))}


def analyze(events):
    native = any(e.get('type') == 'token_usage_record' for e in events)
    requests, actions, pending, feedback = [], [], [], []
    seen_actions, seen_usage = set(), set()
    calls, last_input, current_call, stage, turn = {}, 0, None, None, None
    previous_total, models = None, set()
    for event in events:
        payload = event.get('payload', {})
        if not isinstance(payload, dict):
            continue
        kind = event.get('type')
        if kind == 'turn_context':
            if turn != payload.get('turn_id'):
                stage = None
            turn = payload.get('turn_id')
            if payload.get('model'):
                models.add(payload['model'])
        if kind == 'response_item' and payload.get('type') in ('custom_tool_call', 'function_call'):
            current_call = payload.get('call_id')
            raw = payload.get('input', payload.get('arguments', ''))
            marker = re.search(r'^\s*//\s*usage-stage:\s*([a-z][a-z0-9_-]{0,31})\s*$', str(raw)[:600], re.M)
            if marker:
                stage = marker.group(1)
        if kind == 'event_msg' and payload.get('type') == 'item_completed':
            item = payload.get('item', {})
            if item.get('type') == 'CommandExecution' and item.get('id') not in seen_actions:
                seen_actions.add(item.get('id'))
                command = command_text(item)
                paths = read_paths(command, item.get('parsed_cmd', []))
                action = {'kind': 'CommandExecution', 'id': item.get('id'), 'timestamp': event.get('timestamp'),
                          'turn_id': turn, 'call_id': current_call,
                          'request_hint': len(requests) + 1, 'stage': stage,
                          'tags': action_tags(command, paths), 'read_paths': paths,
                          'command_chars': len(command),
                          'runtime_output_chars': len(item.get('aggregated_output') or ''),
                          'exit_code': item.get('exit_code')}
                actions.append(action)
                pending.append(action['id'])
                calls.setdefault(current_call, []).append(action['id'])
        if kind == 'event_msg' and payload.get('type') == 'item_completed':
            item = payload.get('item', {})
            if item.get('type') in ('McpToolCall', 'Extension', 'ImageView') and item.get('id') not in seen_actions:
                seen_actions.add(item.get('id'))
                action = {'kind': item['type'], 'id': item.get('id'),
                          'timestamp': event.get('timestamp'), 'turn_id': turn,
                          'call_id': current_call, 'request_hint': len(requests) + 1,
                          'stage': stage, 'tool': item.get('tool') or item.get('kind') or 'view_image',
                          'tags': ['image-view'] if item['type'] == 'ImageView' else ['external-tool'],
                          'read_paths': [], 'command_chars': 0, 'runtime_output_chars': 0}
                actions.append(action); pending.append(action['id'])
                calls.setdefault(current_call, []).append(action['id'])
        if kind == 'response_item' and payload.get('type') in ('custom_tool_call_output', 'function_call_output'):
            value = feedback_metadata(payload)
            value['action_ids'] = list(calls.get(value['call_id'], []))
            feedback.append(value)
        usage, cumulative, identity = None, None, None
        if native and kind == 'token_usage_record':
            usage = payload.get('usage')
            cumulative = payload.get('thread_token_usage')
            identity = payload.get('response_id') or event.get('timestamp')
        elif not native and kind == 'event_msg' and payload.get('type') == 'token_count':
            info = payload.get('info') or {}
            cumulative = info.get('total_token_usage')
            if cumulative == previous_total:
                continue
            usage = info.get('last_token_usage')
            identity = 'counter:' + json.dumps(cumulative, sort_keys=True)
        if not isinstance(usage, dict) or identity in seen_usage:
            continue
        seen_usage.add(identity)
        previous_total = cumulative
        values = {key: usage.get(key, 0) for key in USAGE_KEYS}
        if not all(isinstance(v, int) and not isinstance(v, bool) and v >= 0 for v in values.values()):
            raise ValueError('Unsupported usage values; no token estimate substituted')
        input_tokens = values['input_tokens']
        requests.append({'n': len(requests) + 1, 'timestamp': event.get('timestamp'),
                         'turn_id': payload.get('turn_id', turn), 'response_id': identity,
                         'stage': stage, **values,
                         'uncached_input_tokens': input_tokens - values['cached_input_tokens'],
                         'input_growth_from_previous_request': input_tokens - last_input,
                         'actions': pending, 'preceding_tool_feedback': feedback})
        last_input, pending, feedback = input_tokens, [], []
    totals = {key: sum(row[key] for row in requests) for key in USAGE_KEYS}
    totals['uncached_input_tokens'] = totals['input_tokens'] - totals['cached_input_tokens']
    reads = Counter(path for action in actions for path in action['read_paths'])
    turns = []
    for turn_id in dict.fromkeys(row['turn_id'] for row in requests):
        selected = [row for row in requests if row['turn_id'] == turn_id]
        turns.append({'turn_id': turn_id, 'requests': len(selected),
                      'first_request': selected[0]['n'], 'last_request': selected[-1]['n'],
                      **{key: sum(row[key] for row in selected) for key in USAGE_KEYS},
                      'uncached_input_tokens': sum(row['uncached_input_tokens'] for row in selected)})
    summary = {'models': sorted(models), 'request_records': len(requests),
               'usage_source': 'token_usage_record' if native else 'deduplicated token_count',
               'totals': totals, 'turns': turns,
               'cumulative_counter_matches_record_sum': all(totals[key] == previous_total[key] for key in USAGE_KEYS if key in previous_total) if isinstance(previous_total, dict) else None,
               'first_input_tokens': requests[0]['input_tokens'] if requests else None,
               'last_input_tokens': requests[-1]['input_tokens'] if requests else None,
               'command_actions': sum(a['kind'] == 'CommandExecution' for a in actions),
               'all_tool_actions': len(actions),
               'other_tools': dict(Counter(a.get('tool') for a in actions if a['kind'] != 'CommandExecution')),
               'library_action_count': sum('design-library' in a['tags'] for a in actions),
               'runtime_outputs_over_15000_chars': sum(a['runtime_output_chars'] > 15000 for a in actions),
               'truncated_feedback_requests': sum(any(f['truncated'] for f in r['preceding_tool_feedback']) for r in requests),
               'image_blocks_in_feedback': sum(f['image_blocks'] for r in requests for f in r['preceding_tool_feedback']),
               'repeated_observed_read_paths': [{'path': p, 'count': c} for p, c in reads.most_common() if c > 1],
               'largest_uncached_requests': [{k: row[k] for k in ('n', 'timestamp', 'turn_id', 'input_tokens', 'cached_input_tokens', 'uncached_input_tokens', 'input_growth_from_previous_request')} for row in sorted(requests, key=lambda row: row['uncached_input_tokens'], reverse=True)[:8]],
               'largest_runtime_outputs': sorted(actions, key=lambda a: a['runtime_output_chars'], reverse=True)[:10],
               'limits': [
                   'No transcripts, generated source, tool result bodies, image payloads, secrets or rate-limit snapshots are exported.',
                   'Whole-request usage is measured. Exact tokens or waste per file cannot be recovered from these records.',
                   'Runtime output chars may exceed text delivered to the model; they are not token counts.',
                   'Read paths and action tags are heuristic lower bounds, not OS file-access tracing. Repeated reads may follow legitimate edits.',
                   'Preceding feedback is chronological evidence, not proof that all input growth was caused by it.',
                   'A cache miss is observable; its server-side cause is not established.',
                   'Reasoning tokens are included in output. Cached input is included in input. Do not add them again.',
                   'Text-model usage is not a complete bill for image generation or external tools. No billing estimate; no application source files are opened by this analyzer.'
               ]}
    return summary, requests, actions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--thread-id', required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--codex-home', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))))
    args = parser.parse_args()
    thread_id = str(uuid.UUID(args.thread_id))
    files = [p for folder in ('sessions', 'archived_sessions')
             for p in (args.codex_home / folder).rglob('*' + thread_id + '.jsonl')
             if p.name.endswith(thread_id + '.jsonl')]
    if not files:
        parser.error('No local journal for this exact thread ID')
    events = []
    for file in files:
        with file.open(encoding='utf-8') as stream:
            for line in stream:
                try:
                    event = json.loads(line)
                except ValueError:
                    continue
                if isinstance(event, dict):
                    events.append(event)
    events.sort(key=lambda event: event.get('timestamp', ''))
    summary, requests, actions = analyze(events)
    summary.update(thread_id=thread_id, source_files=[str(p) for p in files])
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, values in [('summary.json', summary), ('requests.jsonl', requests), ('actions.jsonl', actions)]:
        target = args.output_dir / name
        if target.is_symlink():
            raise ValueError('Refusing symlink output')
        if isinstance(values, list):
            target.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in values))
        else:
            target.write_text(json.dumps(values, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'summary': str(args.output_dir / 'summary.json'), 'requests': len(requests),
                      'total_tokens': summary['totals']['total_tokens']}))


if __name__ == '__main__':
    main()
