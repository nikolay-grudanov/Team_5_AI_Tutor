---
source_image: page_276.png
page_number: 276
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.96
tokens: 8193
characters: 1465
timestamp: 2025-12-24T00:38:52.943777
finish_reason: stop
---

self.initData()
self.createBase()
self.createTools()
self.createLineWidths()
self.createLineColors()
self.createFillColor()
self.createPatterns()

if __name__ == '__main__':
    draw = Draw()
    draw.run()

Code comments (continued)

10 The purpose of storeObject is to store a list of object descriptors in the order in which they were created, so that the drawing can be refreshed in the correct order.

11 redraw deletes all of the current objects and recreates them, with all original attributes and tags.

12 Tk canvases have a wonderful ability to create a PostScript representation of themselves (it is a pity that the rest of the widgets cannot do this). As a result, we are able to output a file containing the PostScript drawing, which can be printed or viewed with the appropriate software.

10.3 Scrolled canvases

Frequently, the size of a drawing exceeds the available space on the screen. To provide a larger canvas, we must scroll the canvas under a viewing area. Handling scrollbars in some windowing systems (X Window, for example) can require a moderate amount of code. Tkinter (Tk) makes scroll operations relatively easy to code. Take a look at this example, which was reworked directly from a Tk example.

![A screenshot of a scrolled canvas window showing a grid of rectangles with indices, and instructions about scrolling using scrollbars or dragging with button 3.](https://i.imgur.com/3Q5z5QG.png)

Figure 10.7 Managing a scrolled canvas