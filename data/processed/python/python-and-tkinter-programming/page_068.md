---
source_image: page_068.png
page_number: 68
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.10
tokens: 8277
characters: 1555
timestamp: 2025-12-24T00:33:13.134580
finish_reason: stop
---

4.1.10 Text

The Text widget is a versatile widget. Its primary purpose is to display text, of course, but it is capable of multiple styles and fonts, embedded images and windows, and localized event binding.

The Text widget may be used as a simple editor, in which case defining multiple tags and markings makes implementation easy. The widget is complex and has many options and methods, so please refer to the full documentation for precise details. Some of the possible styles and embedded objects are shown in figure 4.18.

![Text widget with several embedded objects](./images/fig_4_18.png)

Figure 4.18 Text widget with several embedded objects

text = Text(root, height=26, width=50)
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)

text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
text.tag_configure('big', font=('Verdana', 24, 'bold'))
text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
text.tag_configure('groove', relief=GROOVE, borderwidth=2)

text.tag_bind('bite', '<1>',
    lambda e, t=text: t.insert(END, "I'll bite your legs off!"))

text.insert(END, 'Something up with my banter, chaps?\n')
text.insert(END, 'Four hours to bury a cat?\n', 'bold_italics')
text.insert(END, 'Can I call you "Frank"?\n', 'big')
text.insert(END, "What's happening Thursday then?\n", 'color')
text.insert(END, 'Did you write this symphony in the shed?\n', 'groove')

button = Button(text, text='I do live at 46 Horton terrace')
text.window_create(END, window=button)