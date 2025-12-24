---
source_image: page_352.png
page_number: 352
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.47
tokens: 7977
characters: 510
timestamp: 2025-12-24T00:40:55.202542
finish_reason: stop
---

Code comments

1 This example is meant to represent a long-term lookup service, so we hang on to the references from call to call to reduce overhead.

2 We import the module dict.py. The PyImport_ImportModule call is entirely analogous to the Python statement import dict.

3 We create an instance of the dictionary using PyObject_CallMethod. Now, although instantiating a class is not really calling a method, Python’s implementation makes it a method call in effect. Here is the short Python module, dict.py: