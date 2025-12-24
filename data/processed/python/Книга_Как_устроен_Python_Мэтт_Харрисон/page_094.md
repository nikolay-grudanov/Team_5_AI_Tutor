---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.98
tokens: 7038
characters: 457
timestamp: 2025-12-24T02:36:13.837391
finish_reason: stop
---

...
    names_to_bands.setdefault(name,
    []).append('Beatles')
>>> for name in band2_names:
    names_to_bands.setdefault(name,
    []).append('Wings')
>>> print(names_to_bands['Paul'])
['Beatles', 'Wings']

В развитие темы: без setdefault этот код получился бы более длинным:

>>> band1_names = ['John', 'George',
... 'Paul', 'Ringo']
>>> band2_names = ['Paul']
>>> names_to_bands = {}
>>> for name in band1_names:
...     if name not in names_to_bands: