#!/usr/bin/env python3
"""Search compact design cards; expand only selected IDs instead of dumping catalogs."""
import argparse
import json
from pathlib import Path
import re


def load_catalog(root):
    result = []
    # patterns.json is an aggregate duplicate; recipes.json is named composition examples.
    # Search canonical ID catalogs only, including both legacy ID catalogs.
    names = ('styles', 'navigation', 'interactions', 'motion', 'layouts', 'legacy-motion', 'legacy-compositions')
    for path in (root / 'catalog' / (name + '.json') for name in names):
        if not path.is_file():
            continue
        values = json.loads(path.read_text())
        if not isinstance(values, list):
            raise ValueError(f'Expected card list: {path}')
        for card in values:
            result.append((card, str(path)))
    return result


def compact(card, path):
    purpose = card.get('use') or card.get('purpose') or card.get('trigger') or card.get('behavior') or card.get('composition') or ''
    return {'id': card['id'], 'name': card.get('name') or card.get('screen') or card['id'], 'category': card.get('category'),
            'purpose': str(purpose)[:160], 'source': path}


def search(root, query, category=None, limit=6):
    words = re.findall(r'\w+', query.casefold())
    results = []
    for card, path in load_catalog(root):
        if category and category not in (card.get('category'), Path(path).stem):
            continue
        title = str(card.get('name', '')).casefold()
        body = ' '.join(str(card.get(k, '')) for k in ('name', 'screen', 'composition', 'genre', 'use', 'purpose', 'treatment', 'behavior', 'trigger', 'typography')).casefold()
        score = sum(4 if word in title else 1 if word in body else 0 for word in words)
        if not words or score:
            results.append((score, card['id'], compact(card, path)))
    results.sort(key=lambda item: (-item[0], item[1]))
    return {'matched': len(results), 'shown': min(limit, len(results)),
            'cards': [x[2] for x in results[:limit]],
            'next': 'Expand chosen IDs with show. Search another relevant category if needed; do not dump all catalog bodies.'}


def show(root, ids):
    by_id = {card['id']: (card, path) for card, path in load_catalog(root)}
    missing = [key for key in ids if key not in by_id]
    if missing:
        raise ValueError('Unknown design IDs: ' + ', '.join(missing))
    return [{'source': by_id[key][1], 'card': by_id[key][0]} for key in ids]


def history(root, app=None, limit=6):
    try:
        values = json.loads((root / 'usage.json').read_text())
    except FileNotFoundError:
        return []
    if app:
        values = [v for v in values if app in (v.get('project_slug'), v.get('app_path'))]
    values = sorted(values, key=lambda v: str(v.get('date', '')), reverse=True)
    # Profile contains the design identity; exclude full evidence, screenshots and reports.
    return [{'project_slug': v.get('project_slug'), 'date': v.get('date'),
             'status': v.get('status'), 'profile': v.get('profile'),
             'rationale': str(v.get('rationale', ''))[:200]} for v in values[:limit]]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library-root', type=Path, default=Path(__file__).resolve().parent)
    sub = parser.add_subparsers(dest='command', required=True)
    find = sub.add_parser('search'); find.add_argument('query', nargs='?', default='')
    find.add_argument('--category'); find.add_argument('--limit', type=int, default=6)
    expand = sub.add_parser('show'); expand.add_argument('ids', nargs='+')
    recent = sub.add_parser('history'); recent.add_argument('--app'); recent.add_argument('--limit', type=int, default=6)
    args = parser.parse_args()
    if hasattr(args, 'limit') and args.limit < 1:
        parser.error('--limit must be positive')
    try:
        if args.command == 'search':
            result = search(args.library_root, args.query, args.category, args.limit)
        elif args.command == 'show':
            result = show(args.library_root, args.ids)
        else:
            result = history(args.library_root, args.app, args.limit)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(2, f'Design query failed: {exc}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
