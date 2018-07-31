import os
from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) < 2:
    sys.exit()

input_file = sys.argv[1]

xml1 = """
<?xml version="1.0" encoding="UTF-8"?>
<opml version="1.0">
  <head>
    <title>OPML file for Blaugust Reborn 2018</title>
  </head>
  <body>
    <outline title="Blogs" text="Blogs">
"""

xml2 = """
    </outline>
  </body>
</opml>
"""

xml3 = '      <outline text="{}" title="{}" type="{}" xmlUrl="{}"/>'


def slugify(s):
  s = s.replace('/', '_')
  s = s.replace(':', '_')
  return s

with open(input_file, 'r') as f:
  for line in f.readlines():
    line = line.strip()
    slug = slugify(line)
    if line[0] == '#':
      print('# Skipping', slug)
      continue
    print('#', line, slug)
    fname = './cache/{}'.format(slug)
    if os.path.isfile(fname):
      print('### EXISTS:', slug)
      continue
    try:
      req = requests.get(line)
      print('#', req.status_code)
      data = req.text
      if req.status_code >= 400 or len(data) < 1:
        print('### ERROR:', slug)
        continue
      with open(fname, 'w') as fout:
        fout.write(data)
    except Exception as ex:
      print('#', ex)


rows = []
with open(input_file, 'r') as f:
  for line in f.readlines():
    line = line.strip()
    slug = slugify(line)
    fname = './cache/{}'.format(slug)
    if os.path.isfile(fname):
      with open(fname, 'r') as fin:
        data = fin.read()
        soup = BeautifulSoup(data, 'html.parser')
        li = soup.head.find(type='application/rss+xml')
        print('#li# ', li)
        if li is None:
          print('# ERROR: None')
          li = soup.head.find(type='application/atom+xml')
          if li is None:
            print('# ERROR: None')
            continue
        print('#', li.get('href'))
        row = {
          'href': li.get('href'),
          'type': li.get('type'),
          'title': li.get('title'),
          'ptitle': soup.head.title.text,
        }
        rows.append(row)

print("#",len(rows))
print(xml1.strip())
for row in rows:
  tp = 'atom'
  if row['type'] == 'application/rss+xml':
    tp = 'rss'
  row['title'] = row['title'].replace(' » Feed', '')
  row['title'] = row['title'].replace(' - RSS', '')
  row['title'] = row['title'].strip()
  if row['title'] == '' or row['title'] == 'RSS':
    if 'medium.com' in row['href']:
      row['title'] = row['ptitle']
      row['title'] = row['title'].replace(' – Medium', '')
    if 'youtube.com' in row['href']:
      row['title'] = row['ptitle']
      row['title'] = row['title'].replace(' - YouTube', '')
  row['title'] = row['title'].strip()
  print(xml3.format(row['title'],row['title'],tp, row['href']))

print(xml2.rstrip())
