---
source_image: page_080.png
page_number: 80
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.93
tokens: 8290
characters: 1533
timestamp: 2025-12-24T00:33:37.084985
finish_reason: stop
---

entryfield_value='1,5',
datatype={'counter' : 'real', 'separator' : ','},
entryfield_validate={'validator' : 'real',
    'min' : '-2,0', 'max' : '5,0',
    'separator' : ','},
increment= .1)

int = Pmw.Counter(root, labelpos=W,
    label_text='Integer:',
    orient=VERTICAL,
    entry_width=2,
    entryfield_value=50,
    entryfield_validate={'validator' : 'integer',
        'min' : 0, 'max' : 99})

counters = (date, real)
Pmw.alignlabels(counters)
for counter in counters:
    counter.pack(fill=X, expand=1, padx=10, pady=5)
    int.pack(padx=10, pady=5)

Documentation for the Counter widget starts on page 553.

4.3.7 CounterDialog

The CounterDialog widget provides a convenience dialog requesting the user to select a value from a Counter widget. The counter can contain any data type that the widget is capable of cycling through, such as the unlikely sequence shown in figure 4.29.

![Screenshot of a CounterDialog window showing an entry field and two buttons labeled OK and Cancel](figure_4_29.png)

Figure 4.29  Pmw CounterDialog widget

choice = None
dialog = Pmw.CounterDialog(root,
    label_text='Enter the number of twits (2 to 8)\n',
    counter_labelpos=N, entryfield_value=2,
    counter_datatype='numeric',
    entryfield_validate={'validator': 'numeric', 'min': 2, 'max': 8},
    buttons=('OK', 'Cancel'), defaultbutton='OK',
    title='Twit of the Year')
dialog.tkraise()

result = dialog.activate()
print 'You clicked on', result, dialog.get()

Documentation for the CounterDialog widget starts on page 556.