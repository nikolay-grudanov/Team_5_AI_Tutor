---
source_image: page_263.png
page_number: 263
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.19
tokens: 8353
characters: 2150
timestamp: 2025-12-24T00:38:44.032610
finish_reason: stop
---

10.1 Drawing on a canvas

We have already encountered several examples of objects drawn on canvases. However, these objects were drawn to represent physical objects on front panels and to create images programmatically. Now we need to allow the user to create drawn objects on the canvas.

Almost all drawing operations define a *bounding box* which encloses the object. The bounding box is expressed as a pair of x/y coordinates at the top-left and bottom-right corners. Lines are special cases; they have a start and end coordinate which does not have to correspond to the coordinates of its bounding box. The bounding box for a line will always be the top-left and bottom-right coordinates. It is important to note that Tk does not guarantee that the bounding box *exactly* bounds the object, so some allowances may have to be made in critical code. This is illustrated in figure 10.1.

![Figure 10.1 Bounding boxes for rectangles, ovals, and lines](./figures/fig_10_1.png)

Figure 10.1 Bounding boxes for rectangles, ovals, and lines

Curved lines (not arcs) are defined as a series of straight lines, each with its own bounding box. Although we will see the application of these object types in some of the examples, they really require special consideration.

Let’s start with a very simple drawing program, inspired by one of the examples in Douglas A. Young’s *The X Window System: Programming and Applications with Xt*. This example allows the user to draw lines, rectangles and ovals on a canvas and then select each of these objects. The original example was written in C using X Window, so I have obviously Tkin-terized it. It does not allow editing of the resulting drawn objects, so it is somewhat akin to drawing on soft paper with a very hard pencil!

draw.py

```python
from Tkinter import *
import Pmw, AppShell, math

class Draw(AppShell.AppShell):
    usecommandarea = 1
    appname        = 'Drawing Program - Version 1'
    frameWidth     = 800
    frameHeight    = 600

    def createButtons(self):
        self.buttonAdd('Close', helpMessage='Close Screen',
                       statusMessage='Exit', command=self.close)
```