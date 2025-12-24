---
source_image: page_199.png
page_number: 199
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.21
tokens: 8124
characters: 972
timestamp: 2025-12-24T00:36:47.201153
finish_reason: stop
---

2 The name and text displayed in the notebook tab comes directly from the data dictionary:

def addPage(self, dictionary):
    table, top, anchor, incr, fields, \
        title, keylist = dataDict[dictionary]
    self.notebook.add(table, label=title)

3 Loading the fields from the data dictionary is similar to the previous example:

for label, field, width, proc, valid, nonblank in fields:
    pstr = 'Label(self.notebook.page(table).interior(),\'\
        'text="%s").place(relx=%f,rely=%f, anchor=E)\n' % \
        (label, (anchor-0.02), ypos)
    ...

4 The pages are tagged with the dictionary key:

def createPages(self):
    self.addPage('general')
    self.addPage('language')
    self.addPage('crewqualifications')
    self.update_display()

Figure 8.10 shows the result of running Example_8_9.py. Notice how the fields are much less cluttered and that they now have clear logical groupings.

![Notebooks](https://i.imgur.com/3Q5z5QG.png)

Figure 8.10 Notebooks