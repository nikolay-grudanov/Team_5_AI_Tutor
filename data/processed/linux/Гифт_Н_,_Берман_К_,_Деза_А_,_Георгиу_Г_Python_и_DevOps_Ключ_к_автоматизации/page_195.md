---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.66
tokens: 7262
characters: 1385
timestamp: 2025-12-24T03:05:57.033628
finish_reason: stop
---

url = "<a href='%sproducts/%s'>%s</a>" %\
    (base_url.strip(), title.lower(), title)
return url

def clean_title(title):
    title_one = title.replace("_", " ")
    title_two = title_one.replace("-", " ")
    title_three = title_two.capitalize()
    return title_three

def build_index():
    baseurl = get_base_url()
    index = []
    posts = os.listdir(CONTENT_ROOT)
    for line in posts:
        print("FILE NAME: %s" % line)
        record = {}
        title = line.strip(".md")
        record['url'] = build_url(baseurl, title)
        record['title'] = clean_title(title)
        print("INDEX RECORD: %s" % record)
        index.append(record)
    return index

def write_index():
    index = build_index()
    with open(INDEX_PATH, 'w') as outfile:
        json.dump(index, outfile)

if __name__ == '__main__':
    write_index()

Наконец, с помощью следующего фрагмента кода можно отправить этот индекс в Algolia:

import json
from algoliasearch import algoliasearch

def update_index():
    """Удаляет индекс, затем обновляет его"""
    print("Starting Updating Index")
    client = algoliasearch.Client("YOUR_KEY", "YOUR_VALUE")
    index = client.init_index("your_INDEX")
    print("Clearing index")
    index.clear_index()
    print("Loading index")
    batch = json.load(open('../index.json'))
    index.add_objects(batch)

if __name__ == '__main__':
    update_index()