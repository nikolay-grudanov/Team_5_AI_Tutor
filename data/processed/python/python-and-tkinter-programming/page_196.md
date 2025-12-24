---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.64
tokens: 8091
characters: 945
timestamp: 2025-12-24T00:36:43.156889
finish_reason: stop
---

8 The update_display method is responsible for setting the markers to indicate new, deleted and modified records:

def update_display(self):
    idx = 0
    for label, field, width, proc, valid, nonblank in self.fields:
        v=self.records[self.current][idx]
        if not v:v=""
        exec 'self.%sV.set(v)' % field
        idx = idx + 1
    if self.current in self.deleted:
        ...

9 The methods bound to the control buttons do nothing in our example, but they are required for Python to run the application:

def unimplemented(self):
    pass

Running Example_8_7.py will display a screen similar to figure 8.9. Notice that the layout could be improved if the fields were individually placed, or if more than one field were placed on a single line, but that would obviate the simplicity of using a data dictionary.

![A screen created from a data dictionary](./images/fig8-9.png)

Figure 8.9 A screen created from a data dictionary