---
source_image: page_083.png
page_number: 83
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.64
tokens: 8200
characters: 1201
timestamp: 2025-12-24T00:33:32.220121
finish_reason: stop
---

w.pack(fill=BOTH, expand=1, padx=6, pady=6)
cw = Frame(w.interior(), width=150, height=20)
cw.pack(padx=2, pady=2, expand=1, fill=BOTH)

Documentation for the Group widget starts on page 564.

4.3.11 LabeledWidget

The LabeledWidget widget is a convenience container which labels a widget or collection of widgets. Options are provided to control the placement of the label and control the appearance of the graphic border. The child site can be populated with any combination of widgets. The example shown in figure 4.33 uses the widget as a frame which requires less code than using individual components.

![Screenshot of a labeled widget showing a sunset on Cat Island](./images/sunset_on_cat_island.png)

Figure 4.33 Pmw LabeledWidget widget

frame = Frame(root, background = 'gray80')
frame.pack(fill=BOTH, expand=1)

lw = Pmw.LabeledWidget(frame, labelfpos='n',
    label_text='Sunset on Cat Island')
lw.component('hull').configure(relief=SUNKEN, borderwidth=3)
lw.pack(padx=10, pady=10)

img = PhotoImage(file='chairs.gif')
cw = Button(lw.interior(), background='yellow', image=img)
cw.pack(padx=10, pady=10, expand=1, fill=BOTH)

Documentation for the LabeledWidget widget starts on page 565.