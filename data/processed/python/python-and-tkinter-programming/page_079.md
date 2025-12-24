---
source_image: page_079.png
page_number: 79
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.35
tokens: 8154
characters: 1181
timestamp: 2025-12-24T00:33:25.028125
finish_reason: stop
---

Figure 4.27 Pmw ComboBoxDialog widget

Documentation for the ComboBoxDialog widget starts on page 551.

4.3.6 Counter

The Counter widget is a versatile widget which allows the user to cycle through a sequence of available values. Pmw provides integer, real, time and date counters and it is possible to define your own function to increment or decrement the displayed value. There is no limitation on the value that is displayed as the result of incrementing the counter, so there is no reason that the counter cannot display “eine, zwei, drei” or whatever sequence is appropriate for the application. Some examples are shown in figure 4.28.

Figure 4.28 Pmw Counter widget

def execute(self):
    print 'Return pressed, value is', date.get()

    date = Pmw.Counter(root, labelpos=W,
        label_text='Date (4-digit year):',
        entryfield_value=time.strftime('%d/%m/%Y',
            time.localtime(time.time())),
        entryfield_command=execute,
        entryfield_validate={'validator' : 'date', 'format' : 'dmy'},
        datatype = {'counter' : 'date', 'format' : 'dmy', 'yyyy' : 1})

    real = Pmw.Counter(root, labelpos=W,
        label_text='Real (with comma):',