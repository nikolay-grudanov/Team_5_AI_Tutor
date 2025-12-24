---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.83
tokens: 8181
characters: 1184
timestamp: 2025-12-24T00:33:22.022790
finish_reason: stop
---

balloon and the status area, and make such choices persistent so that the user does not have to turn off the feature each time he uses the application.

balloon = Pmw.Balloon(root)
frame = Frame(root)
frame.pack(padx = 10, pady = 5)
field = Pmw.EntryField(frame, labelfpos=W, label_text='Name:')
field.setentry('A.N. Other')
field.pack(side=LEFT, padx = 10)

balloon.bind(field, 'Your name', 'Enter your name')
check = Button(frame, text='Check')
check.pack(side=LEFT, padx=10)
balloon.bind(check, 'Look up', 'Check if name is in the database')
frame.pack()

messageBar = Pmw.MessageBar(root, entry_width=40,
    entry_relief=GROOVE,
    labelfpos=W, label_text='Status:')
messageBar.pack(fill=X, expand=1, padx=10, pady=5)

balloon.configure(statuscommand = messageBar.helpmessage)

... After a few seconds

Documentation for the Balloon widget starts on page 545.

4.3.3 ButtonBox

The ButtonBox widget provides a convenient way to implement a number of buttons and it is usually used to provide a command area within an application. The box may be laid out either horizontally or vertically and it is possible to define a default button. A simple ButtonBox is shown in figure 4.25.