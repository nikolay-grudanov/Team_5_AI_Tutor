---
source_image: page_062.png
page_number: 62
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.47
tokens: 8330
characters: 1922
timestamp: 2025-12-24T00:33:07.095123
finish_reason: stop
---

4.1.5 Entry

Entry widgets are the basic widgets used to collect input from a user. They may also be used to display information and may be disabled to prevent a user from changing their values.

Entry widgets are limited to a single line of text which can be in only one font. A typical entry widget is shown in figure 4.8. If the text entered into the widget is longer than the available display space, the widget scrolls the contents. You may change the visible position using the arrow keys. You may also use the widget’s scrolling methods to bind scrolling behavior to the mouse or to your application.

![Entry widget screenshot](images/entry_widget.png)

Figure 4.8 Entry widget

Label(root, text="Anagram:").pack(side=LEFT, padx=5, pady=10)
e = StringVar()
Entry(root, width=40, textvariable=e).pack(side=LEFT)
e.set("'A shroe! A shroe! My dingkom for a shroe!'")

Documentation for the Entry widget starts on page 484.

4.1.6 Radiobutton

The Radiobutton widget may need renaming soon! It is becoming unusual to see car radios with mechanical button selectors, so it might be difficult to explain the widget to future GUI designers. However, the idea is that all selections are exclusive, so that selecting one button deselects any button already selected.

In a similar fashion to Button widgets, Radiobuttons can display text or images and can have text which spans multiple lines, although in one font only. Figure 4.9 illustrates typical Radiobuttons.

You normally associate all of the radiobuttons in a group to a single variable.

![Radiobutton widget screenshot](images/radiobutton_widget.png)

Figure 4.9 Radiobutton widget

var = IntVar()
for text, value in [('Passion fruit', 1), ('Loganberries', 2),
                    ('Mangoes in syrup', 3), ('Oranges', 4),
                    ('Apples', 5), ('Grapefruit', 6)]:
    Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
var.set(3)