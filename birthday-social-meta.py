#!/usr/bin/env python3
"""Set safe, non-spoiler link metadata without changing any card artwork or behavior."""
from pathlib import Path
import re
import sys

page = Path(sys.argv[1])
html = page.read_text(encoding='utf-8')
head, separator, remainder = html.partition('</head>')
if not separator or '<head>' not in head:
    raise SystemExit('Cannot find HTML head; refusing to modify card')

# Delete any former cover-art Open Graph tags, and replace old link previews.
head = re.sub(
    r'(?m)^\s*<meta\s+(?:property="og:[^"]+"|name="(?:description|twitter:[^"]+)")[^>]*>\s*\n?',
    '\n',
    head,
)
head, title_count = re.subn(
    r'<title>[^<]*</title>',
    '<title>A special surprise for the most special person in the world — From Zac</title>',
    head,
    count=1,
)
if title_count != 1:
    raise SystemExit('Cannot find title; refusing to modify card')

preview = 'https://posnerzac-debug.github.io/Leah-Birthday-Card/birthday-preview.png?v=20260921b'
metadata = f'''<meta name="description" content="A special surprise for the most special person in the world. From Zac.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://posnerzac-debug.github.io/Leah-Birthday-Card/">
<meta property="og:title" content="A special surprise for the most special person in the world ♡">
<meta property="og:description" content="From Zac. ♡">
<meta property="og:image" content="{preview}">
<meta property="og:image:secure_url" content="{preview}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="A warm cream birthday countdown saying Nuh-uh-uh; unlocks September 24 at midnight.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="A special surprise for the most special person in the world ♡">
<meta name="twitter:description" content="From Zac. ♡">
<meta name="twitter:image" content="{preview}">'''
head = head.replace('<head>', '<head>\n' + metadata, 1)
page.write_text(head + separator + remainder, encoding='utf-8')
assert head.count('property="og:image"') == 1
print(f'Applied spoiler-free link preview to {page}')
