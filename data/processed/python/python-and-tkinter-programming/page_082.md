---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.38
tokens: 8376
characters: 1584
timestamp: 2025-12-24T00:33:43.584109
finish_reason: stop
---

int    = Pmw.EntryField(root, labelpos=W, label_text = 'Integer (5 to 42):',
    validate = {'validator' : 'numeric',
        'min' : 5, 'max' : 42, 'minstrict' : 0},
    value = '12')

date = Pmw.EntryField(root, labelpos=W,label_text = 'Date (in 2000):',
    value = '2000/1/1', validate = {'validator' : 'date',
        'min' : '2000/1/1', 'max' : '2000/12/31',
        'minstrict' : 0, 'maxstrict' : 0,
        'format' : 'ymd'})

widgets = (noval, real, int, date)
for widget in widgets:
    widget.pack(fill=X, expand=1, padx=10, pady=5)
Pmw.alignlabels(widgets)

real.component('entry').focus_set()

Documentation for the EntryField widget starts on page 559.

4.3.10 Group

The Group widget provides a convenient way to place a labeled frame around a group of widgets. The label can be any reasonable widget such as a Label but it can also be an EntryField, RadioButton or CheckButton depending on the application requirements. It is also possible to use the widget as a graphic frame with no label. These examples are shown in figure 4.32.

![Figure 4.32 Pmw Group widget](figure_4_32.png)

w = Pmw.Group(root, tag_text='place label here')
w.pack(fill=BOTH, expand=1, padx=6, pady=6)
cw = Label(w.interior(), text='A group with a\nsimple Label tag')
cw.pack(padx=2, pady=2, expand=1, fill=BOTH)

w = Pmw.Group(root, tag_pyclass=None)
w.pack(fill=BOTH, expand=1, padx=6, pady=6)
cw = Label(w.interior(), text='A group\nwithout a tag')
cw.pack(padx=2, pady=2, expand=1, fill=BOTH)

w = Pmw.Group(root, tag_pyclass=Checkbutton,
    tag_text='checkbutton', tag_foreground='blue')