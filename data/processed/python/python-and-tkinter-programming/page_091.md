---
source_image: page_091.png
page_number: 91
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.03
tokens: 8232
characters: 1395
timestamp: 2025-12-24T00:33:54.112678
finish_reason: stop
---

4.3.20 PromptDialog

The PromptDialog widget is a convenience dialog which displays a single EntryField and a number of buttons in a ButtonBox. It is useful for creating a simple dialog on-the-fly. The example shown in figure 4.42 collects a password from a user.

![Password prompt dialog](./images/fig_4_42.png)

Figure 4.42 Pmw PromptDialog widget

dialog = Pmw.PromptDialog(root, title='Password', label_text='Password:',
    entryfield_labelfpos=N, entry_show='*', defaultbutton=0,
    buttons=('OK', 'Cancel'))

result = dialog.activate()
print 'You selected', result

Documentation for the PromptDialog widget starts on page 587.

4.3.21 RadioSelect

The RadioSelect widget implements an alternative to the Tkinter RadioButton widget. RadioSelect creates a manager that contains a number of buttons. The widget may be configured to operate either in single-selection mode where only one button at a time may be activated, or multiple selection mode where any number of buttons may be selected. This is illustrated in figure 4.43.

![RadioSelect example](./images/fig_4_43.png)

Figure 4.43 Pmw RadioSelect widget

horiz = Pmw.RadioSelect(root, labelfpos=W, label_text=HORIZONTAL,
    frame_borderwidth=2, frame_relief=RIDGE)
horiz.pack(fill=X, padx=10, pady=10)

for text in ('Passion fruit', 'Loganberries', 'Mangoes in syrup',
    'Oranges', 'Apples', 'Grapefruit'):
    horiz.add(text)