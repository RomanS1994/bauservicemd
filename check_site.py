"""Check generated static pages and local links without third-party dependencies."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.refs = path, [], []
        self.h1 = 0
        self.lang = None
        self.labels, self.inputs = [], []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'h1':
            self.h1 += 1
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'label' and 'for' in attrs:
            self.labels.append(attrs['for'])
        if tag in ('input', 'textarea') and attrs.get('type') != 'hidden':
            self.inputs.append(attrs.get('id'))
        for key in ('href', 'src'):
            if key in attrs:
                self.refs.append(attrs[key])


def main():
    paths = [ROOT / 'index.html', *sorted(p for lang in ('uk', 'de', 'en') for p in (ROOT / lang).glob('*.html'))]
    pages = {p.resolve(): Page(p) for p in paths}
    errors = []
    links = 0
    for path, page in pages.items():
        prefix = str(path.relative_to(ROOT))
        if page.h1 != 1:
            errors.append(f'{prefix}: expected one H1, got {page.h1}')
        if page.lang not in ('uk', 'de', 'en'):
            errors.append(f'{prefix}: missing or unsupported language')
        if len(page.ids) != len(set(page.ids)):
            errors.append(f'{prefix}: duplicate IDs')
        for target in page.inputs:
            if not target or target not in page.labels:
                errors.append(f'{prefix}: input missing associated label: {target}')
        for ref in page.refs:
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            if parsed.path.startswith('/'):
                errors.append(f'{prefix}: root-relative path breaks repository Pages: {ref}')
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.exists():
                errors.append(f'{prefix}: missing file {ref}')
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f'{prefix}: missing fragment {ref}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages, {links} local references, labels, IDs, H1 and languages.')


if __name__ == '__main__':
    main()
