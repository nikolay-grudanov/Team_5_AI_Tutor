---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.22
tokens: 7265
characters: 1185
timestamp: 2025-12-24T03:05:53.491529
finish_reason: stop
---

```python
print("KEY: %s, VALUE: %s" % (key, values))
if title in key:
    return title, key
for val in values:
    if title in val:
        return title, key

def move_image(val):
    """Создает новую копию загруженных на сайт изображений в каталоге img"""

    source_picture = "static/uploads/%s" % val["picture"]
    destination_dir = "static/img/"
    shutil.copy(source_picture, destination_dir)

def new_image_metadata(vals):
    new_paths = []
    for val in vals:
        pic = val['picture'].split("/")[1:-1].pop()
        destination_dir = "static/img/%s" % pic
        val['picture'] = destination_dir
        new_paths.append(val)
    return new_paths

CAT_LOOKUP = {'2100': 'Foo',
    'a': 'Biz',
    'b': 'Bam',
    'c': 'Bar',
    '1': 'Foobar',
    '2': 'bizbar',
    '3': 'bam'}

def write_post(val):

    tags = val["tags"]
    date = val["date"]
    title = val["title"]
    picture = val["picture"]
    categories = val["categories"]
    out = """
+++ 
tags = ["%s"]
categories = ["%s"]
date = "%s"
title = "%s"
banner = "%s"
+++
[![%s](%s)](%s)
**Product Name**: %s"""\n
(tags, categories, date, title, picture.lstrip("/"),
    title, picture, picture, title)
```