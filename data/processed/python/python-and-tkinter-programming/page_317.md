---
source_image: page_317.png
page_number: 317
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.24
tokens: 8490
characters: 2586
timestamp: 2025-12-24T00:40:22.828887
finish_reason: stop
---

xy = 25+adj, 25+adj, x1-25-adj, y1-25-adj
xys = 25+adj, 25+adj+10, x1-25-adj, y1-25-adj+10

The shadow disc (xys) is used if the pie chart is being displayed as a tilted disc.

3 The shadow is drawn as a pie slice with an almost complete circular slice:
    if not x1 == y1:
        canvas.create_arc(xys, start=0.0, extent=359.99,
            fill='gray60', outline=outline, style='pieslice')

4 As in the case of adding bar graphs, adding pie charts requires a specialized draw routine.
5 The scaling factors are determined by the presence of multiple graphs in the same widget.
6 self.multiple is passed down to the graph object’s draw method.

As you have seen in these examples, adding a new graph type is quite easy and it produces some reasonably attractive graphs. I hope that you can make use of them and perhaps create new visual formats for the Python community.

11.3 3-D graphs

If you have a large amount of data and that data follows a pattern that encourages examining the graphs on the same axes (same scale), there are a number of ways to display the graphs. One way is to produce a series of separate graphs and then present them side by side. This is good if you want to examine the individual graphs in detail, but it does not readily demonstrate the relationship between the graphs. To show the relationship you can produce a single diagram with all of the plots superimposed using different symbols, line styles, or combinations of both. However, there is often a tendency for the lines to become entangled or for symbols to be drawn on top of each other. This can produce very confusing results.

I always like to solve these problems by producing three-dimensional graphs. They allow the viewer to get a sense of the topology of the data as a whole, often highlighting features in the data that may be difficult to discern in other formats. The next example illustrates such a graph (see figure 11.7). I have taken a few shortcuts to reduce the overall amount of code. For example, I have made no provision for modifying the orientation of the axes or the viewing position. I’ll leave that as an exercise for the enthusiastic reader!

3dgraph.py

from Tkinter import *
import Pmw, AppShell, math

class Graph3D(AppShell.AppShell):
    usecommandarea = 1
    appname        = '3-Dimensional Graph'
    frameWidth     = 800
    frameHeight    = 650

    def createButtons(self):
        self.buttonAdd('Print',
            helpMessage='Print current graph (PostScript)',
            statusMessage='Print graph as PostScript file',
            command=self.iprint)