---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.79
tokens: 8421
characters: 1955
timestamp: 2025-12-24T00:33:25.434894
finish_reason: stop
---

canvas.create_arc(xy, start=270, extent=5, fill='gray70')
canvas.create_arc(xy, start=275, extent=35, fill='gray80')
canvas.create_arc(xy, start=310, extent=49, fill='gray90')

canvas.create_polygon(205,105,285,125,166,177,210,199,205,105, fill='white')
canvas.create_text(350,150, text='text', fill='yellow', font=('verdana', 36))

img = PhotoImage(file='img52.gif')
canvas.create_image(145,280, image=img, anchor=CENTER)

frm = Frame(canvas, relief=GROOVE, borderwidth=2)
Label(frm, text="Embedded Frame/Label").pack()
canvas.create_window(285, 280, window=frm, anchor=CENTER)
canvas.pack()

Documentation for the Canvas widget starts on page 456.
Documentation for the Bitmap class starts on page 452.
Documentation for the PhotoImage class starts on page 512.

4.1.12 Scrollbar

Scrollbar widgets can be added to any widget that supports scrolling such as Text, Canvas and Listbox widgets.

Associating a Scrollbar widget with another widget is as simple as adding callbacks to each widget and arranging for them to be displayed together. Of course, there is no requirement for them to be co-located but you may end up with some unusual GUIs if you don’t! Figure 4.20 shows a typical application.

Figure 4.20
Scrollbar widget

list = Listbox(root, height=6, width=15)
scroll = Scrollbar(root, command=list.yview)
list.configure(yscrollcommand=scroll.set)
list.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
for item in range(30):
    list.insert(END, item)

Documentation for the Scrollbar widget starts on page 525.

4.1.13 Listbox

Listbox widgets display a list of values that may be chosen by the user. The default behavior of the widget is to allow the user to select a single item in the list. A simple example is shown in figure 4.21. You may add additional bindings and use the selectmode option of the widget to allow multiple-item and other properties.

See “Scrollbar” above, for information on adding scrolling capability to the listbox.