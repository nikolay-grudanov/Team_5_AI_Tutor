---
source_image: page_303.png
page_number: 303
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.37
tokens: 8262
characters: 1274
timestamp: 2025-12-24T00:39:54.054764
finish_reason: stop
---

This small amount of code produces an effective graph with little effort as you can see in figure 11.1. We can improve this graph easily by adding lines connecting the dots as shown in figure 11.2.

![A line graph with dots connected by blue lines, showing data points and axes labeled from 0 to 100 on the x-axis and 0 to 250 on the y-axis.](./images/figure_11_2.png)

Figure 11.2 Adding lines to a simple graph

**simpleplot2.py**

scaled = []
for x,y in [(12, 56), (20, 94), (33, 98), (45, 120), (61, 180), (75, 160), (98, 223)]:
    scaled.append(100 + 3*x, 250 - (4*y)/5)
canvas.create_line(scaled, fill='royalblue')
for x,y in scaled:
    canvas.create_oval(x-6,y-6,x+6,y+6, width=1, outline='black', fill='SkyBlue2')

**Code comments**

① So that we do not have to iterate through the data in a simple loop, we construct a list of x-y coordinates which may be used to construct the line (a list of coordinates may be input to the create_line method).

② We draw the line first. Remember that items drawn on a canvas are layered so we want the lines to appear under the blobs.

③ Followed by the blobs.

Here come the Ginsu knives! We can add line smoothing at no extra charge! If we turn on smoothing we get cubic splines for free; this is illustrated in figure 11.3.