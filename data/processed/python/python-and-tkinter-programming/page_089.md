---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.36
tokens: 8209
characters: 1172
timestamp: 2025-12-24T00:33:49.249226
finish_reason: stop
---

p2 = nb.add('Page 2')
p3 = nb.add('Page 3')
nb.pack(padx=5, pady=5, fill=BOTH, expand=1)

Button(p1, text='This is text on page 1', fg='blue').pack(pady=40)
c = Canvas(p2, bg='gray30')
w = c.winfo_reqwidth()
h = c.winfo_reqheight()
c.create_oval(10,10,w-10,h-10,fill='DeepSkyBlue1')
c.create_text(w/2,h/2,text='This is text on a canvas', fill='white',
    font=('Verdana', 14, 'bold'))
c.pack(fill=BOTH, expand=1)

nb.setnaturalpagesize()
root.mainloop()

Documentation for the Notebook widget starts on page 578.

4.3.18 OptionMenu

The OptionMenu widget implements a classic popup menu motif familiar to Motif programmers. However, the appearance of the associated popup is a little different, as shown in figure 4.40. OptionMenus should be used to select limited items of data. If you populate the widget with large numbers of data the popup may not fit on the screen and the widget does not scroll.

![OptionMenu widgets showing different states](optionmenu_screenshots.png)

Figure 4.40 Pmw OptionMenu widget

var = StringVar()
var.set('Quantity Surveyor')
opt_menu = Pmw.OptionMenu(root, labelfpos=W,
    label_text='Choose profession:', menubutton_textvariable=var,