---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.48
tokens: 8156
characters: 1011
timestamp: 2025-12-24T00:33:07.122410
finish_reason: stop
---

list = Listbox(root, width=15)
list.pack()
for item in range(10):
    list.insert(END, item)

Documentation for the Listbox widget starts on page 497.

Figure 4.21 List box widget

4.1.14 Scale

The Scale widget allows you to set linear values between selected lower and upper values and it displays the current value in a graphical manner. Optionally, the numeric value may be displayed.

The Scale widget has several options to control its appearance and behavior; otherwise it is a fairly simple widget.

The following example, shown in figure 4.22, is an adaptation of one of the demonstrations supplied with the Tcl/Tk distribution. As such, it may be useful for programmers in Tcl/Tk to see how a conversion to Tkinter can be made.

def setHeight(canvas, heightStr):
    height = string.atoi(heightStr)
    height = height + 21
    y2 = height - 30
    if y2 < 21:
        y2 = 21
    canvas.coords('poly',
        15,20,35,20,35,y2,45,y2,25,height,5,y2,15,y2,15,20)

Figure 4.22 Scale widget: application