---
source_image: page_033.png
page_number: 33
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.36
tokens: 8209
characters: 1331
timestamp: 2025-12-24T00:32:16.984516
finish_reason: stop
---

1.2.3 Dictionaries

Dictionaries are arrays of data indexed by keys. I think that they give Python the edge in designing compact systems. If you use lists and tuples as data contained within dictionaries you have a powerful mix (not to say that mixing code objects, dictionaries and abstract objects isn’t powerful!).

Initializing dictionaries
Dictionaries may be initialized by providing key:value pairs:

dict = {}                                 # Empty dictionary
dict = {'a': 1, 'b': 2, 'c': 3}           # String key
dict = {1: 'a', 2: 'b', 3: 'c'}           # Integer key
dict = {1: [1,2,3], 2: [4,5,6]}           # List data

Modifying dictionaries
Dictionaries are readily modifiable:

dict['a'] = 10
dict[10] = 'Larch'

Accessing dictionaries
Recent versions of Python facilitate lookups where the key may not exist. First, the old way:

if dict.has_key('a'):
    value = dict['a']
else:
    value = None

or:

try:
    value = dict['a']
except KeyError:
    value = None

This is the current method:

value = dict.get('a', None)

Iterating through entries
Get the keys and then iterate through them:

keys = dict.keys()
for key in keys:
    ...

Sorting dictionaries
Dictionaries have arbitrary order so you must sort the keys if you want to access the keys in order:

keys = dict.keys().sort()
for key in keys:
    ...