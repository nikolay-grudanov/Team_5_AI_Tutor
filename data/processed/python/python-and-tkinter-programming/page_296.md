---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.12
tokens: 8237
characters: 1572
timestamp: 2025-12-24T00:39:36.347948
finish_reason: stop
---

12 doSave implements the writing of the marshaled data to a file. Figure 10.12 illustrates the tkFileDialog used to get the file name. Note that the dialogs are native dialogs for the particular architecture upon which Tk is running at release 8.0 and above.

![Save As dialog](./images/save_as_dialog.png)

Figure 10.12 Save As dialog

10.7 Speed drawing

In general, creating canvas objects is relatively efficient and rarely causes a performance problem. However, for very complex drawings, you may notice a delay in drawing the canvas. This is particularly noticeable when the display contains a large number of objects or when they contain complex line segments.

One way of improving drawing performance is to draw the canvas as an image. The Python Imaging Library, which was introduced briefly in chapter 5 on page 89, has the facility to draw directly to a GIF file. We will use this facility to draw a quite challenging image. I always found Mandelbrot diagrams, now generally referred to as fractals, fascinating. While I was looking at Douglas A. Young’s The X Window System: Programming and Applications with Xt, I noticed the fractal on the cover. Here is an adaptation of the fractal in Python, Tkinter and PIL.

fractal.py

from Tkinter import *
import Pmw, AppShell, Image, ImageDraw, os

class Palette:
    def __init__(self):
        self.palette = [(0,0,0), (255,255,255)]

    def getpalette(self):
        # flatten the palette
        palette = []
        for r, g, b in self.palette:
            palette = palette + [r, g, b]
        return palette