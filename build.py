import json

with open('data-full.json') as f:
    data_json = f.read()

with open('template.html') as f:
    template = f.read()

html = template.replace('__DATA_PLACEHOLDER__', data_json)

with open('index.html', 'w') as f:
    f.write(html)

print(f"Built index.html: {len(html):,} chars")
