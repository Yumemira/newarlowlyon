#!/usr/bin/env python3
"""Read token_count metadata for one local Codex session; never emit transcript."""
import argparse
import json
import os
from pathlib import Path
import uuid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--thread-id', required=True)
    parser.add_argument('--codex-home', type=Path,
                        default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))))
    args = parser.parse_args()
    try:
        thread_id = str(uuid.UUID(args.thread_id))
    except ValueError:
        parser.error('--thread-id must be a UUID')
    latest = None
    for directory in ('sessions', 'archived_sessions'):
        root = args.codex_home / directory
        if not root.is_dir():
            continue
        for path in root.rglob('*' + thread_id + '*.jsonl'):
            # A local rollout filename must end with exactly this session ID.
            if not path.name.endswith(thread_id + '.jsonl'):
                continue
            try:
                with path.open(encoding='utf-8') as stream:
                    for line in stream:
                        try:
                            event = json.loads(line)
                        except (ValueError, UnicodeError):
                            continue  # A running session may have an unfinished last line.
                        if not isinstance(event, dict) or event.get('type') != 'event_msg':
                            continue
                        payload = event.get('payload')
                        if not isinstance(payload, dict) or payload.get('type') != 'token_count':
                            continue
                        info = payload.get('info')
                        if not isinstance(info, dict):
                            continue
                        timestamp = event.get('timestamp')
                        key = timestamp if isinstance(timestamp, str) else ''
                        if latest is None or key >= latest[0]:
                            latest = (key, path, info)
            except (OSError, UnicodeError):
                continue
    if latest is None:
        print(json.dumps({'status': 'unavailable', 'thread_id': thread_id,
                          'reason': 'No readable token_count metadata for this local session'}))
        return 2
    timestamp, path, info = latest
    last = info.get('last_token_usage')
    total = info.get('total_token_usage')
    last = last if isinstance(last, dict) else {}
    total = total if isinstance(total, dict) else {}
    fields = ('input_tokens', 'cached_input_tokens', 'output_tokens',
              'reasoning_output_tokens', 'total_tokens')
    def numbers(source):
        return {k: source[k] for k in fields
                if isinstance(source.get(k), int) and not isinstance(source[k], bool)
                and source[k] >= 0}
    last, total = numbers(last), numbers(total)
    window = info.get('model_context_window')
    window = window if isinstance(window, int) and not isinstance(window, bool) and window > 0 else None
    used = last.get('total_tokens')
    pct = round(100 * used / window, 2) if used is not None and window else None
    print(json.dumps({'status': 'available' if pct is not None else 'incomplete',
                      'thread_id': thread_id, 'source': str(path),
                      'event_timestamp': timestamp or None,
                      'last_token_usage': last, 'total_token_usage': total,
                      'model_context_window': window,
                      'last_request_total_percent_of_window': pct,
                      'measurement': 'Last recorded request snapshot, not live next-request occupancy'},
                     ensure_ascii=False, indent=2))
    return 0 if pct is not None else 2


if __name__ == '__main__':
    raise SystemExit(main())
