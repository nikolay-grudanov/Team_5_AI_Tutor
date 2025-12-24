---
source_image: page_069.png
page_number: 69
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.13
tokens: 8305
characters: 1539
timestamp: 2025-12-24T00:33:18.305488
finish_reason: stop
---

photo=PhotoImage(file='lumber.gif')
text.image_create(END, image=photo)

text.insert(END, 'I dare you to click on this\n', 'bite')
text.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

Documentation for the Text widget starts on page 528.

4.1.11 Canvas

Canvases are versatile widgets. Not only can you use them to draw complex objects, using lines, ovals, polygons and rectangles, but you can also place images and bitmaps on the canvas with great precision. In addition to these features you can place any widgets within a canvas (such as buttons, listboxes and other widgets) and bind mouse or keyboard actions to them.

You will see many examples in this book where Canvas widgets have been used to provide a free-form container for a variety of applications. The example shown in figure 4.19 is a somewhat crude attempt to illustrate most of the available facilities.

One property of Canvas widgets, which can be either useful or can get in the way, is that objects are drawn on top of any objects already on the canvas. You can change the order of canvas items later, if necessary.

![Canvas widget screenshot](https://i.imgur.com/3Q5z5QG.png)

Figure 4.19 Canvas widget

canvas = Canvas(root, width =400, height=400)
canvas.create_oval(10,10,100,100, fill='gray90')
canvas.create_line(105,10,200,105, stipple='@bitmaps/gray3')
canvas.create_rectangle(205,10,300,105, outline='white', fill='gray50')
canvas.create_bitmap(355, 53, bitmap='questhead')

xy = 10, 105, 100, 200
canvas.create_arc(xy, start=0, extent=270, fill='gray60')