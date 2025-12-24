---
source_image: page_050.png
page_number: 50
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.94
tokens: 8045
characters: 743
timestamp: 2025-12-24T00:32:30.981810
finish_reason: stop
---

Code comments (continued)

9 A number of constants are defined. The following data structure is quite complex. Using constants makes it easy to change values throughout such a complex structure and they make the code much more readable and consequently easier to maintain.

FUN = 1        # A Function
KEY = 0        # A Key
KC1 = 'gray30' # Dark Keys
KC2 = 'gray50' # Light Keys

These are used to populate a nested list of lists, which contains tuples. The tuples store three labels, the key color, the function or key designator and the method to bind to the key’s cmd (activate) callback.

10 We create the Pmw ScrolledText widget and provide values for many of its attributes.

self.display = Pmw.ScrolledText(self, hscrollmode='dynamic',