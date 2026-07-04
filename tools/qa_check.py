import os
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('img', 'script') and 'src' in attrs:
            self.links.append(attrs['src'])
        if tag == 'link' and 'href' in attrs:
            self.links.append(attrs['href'])

def find_html_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            if f.lower().endswith('.html'):
                yield os.path.join(dirpath, f)

def check_refs(project_root):
    errors = []
    for html_path in find_html_files(project_root):
        with open(html_path, 'r', encoding='utf-8') as fh:
            data = fh.read()
        parser = LinkParser()
        parser.feed(data)
        for ref in parser.links:
            if ref.startswith(('http://','https://','mailto:','tel:','#')):
                continue
            # normalize path
            ref_path = os.path.normpath(os.path.join(os.path.dirname(html_path), ref))
            if not os.path.exists(ref_path):
                errors.append((html_path, ref, ref_path))
    return errors

if __name__ == '__main__':
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print('Project root:', root)
    errs = check_refs(root)
    if not errs:
        print('No missing local references found.')
        exit(0)
    print('Missing references:')
    for html, ref, path in errs:
        print(f'- {html} -> {ref} (resolved: {path})')
    exit(2)
