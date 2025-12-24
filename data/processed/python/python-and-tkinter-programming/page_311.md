---
source_image: page_311.png
page_number: 311
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.76
tokens: 8222
characters: 1380
timestamp: 2025-12-24T00:39:56.602277
finish_reason: stop
---

Code comments (continued)

17 Using the graph widget is quite easy. First, we create the line/curve that we wish to plot:
    for i in range(18):
        data.append((float(i)*di,
            (math.sin(float(i)*di)-math.cos(float(i)*di))))
        line = GraphLine(data, color='gray', smooth=0)
        linea = GraphLine(data, color='blue', smooth=1, splinesteps=500)

18 Next we create the GraphObject which does the necessary scaling:
    graphObject = GraphObjects([line, linea])

19 Finally, we create the graph widget and associate the GraphObject with it:
    graph = GraphBase(root, 500, 400, relief=SUNKEN, border=2)
    graph.pack(side=TOP, fill=BOTH, expand=YES)
    graph.draw(graphObject, 'automatic', 'automatic')

11.2.1 Adding bargraphs

Having developed the basic graph widget, it is easy to add new types of visuals. Bargraphs, sometimes called histograms, are a common way of presenting data, particularly when it is intended to portray the magnitude of the data, since the bars have actual volume as opposed to perceived volume under-the-curve. Figure 11.5 shows some typical bargraphs, in some cases combined with line graphs. Note that it is quite easy to set up multiple instances of the graph widget.

![Figure 11.5 Adding bar graphs to the graph widget](../images/ch11_05.png)

plot2.py

from Tkinter import *
from Canvas import Line, CanvasText, Rectangle