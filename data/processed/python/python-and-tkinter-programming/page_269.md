---
source_image: page_269.png
page_number: 269
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.55
tokens: 8217
characters: 1607
timestamp: 2025-12-24T00:38:45.978822
finish_reason: stop
---

self.canvas.move(self.selObj, cx-self.lastx, cy-self.lasty)
    self.lastx = cx
    self.lasty = cy

Code comments
1 We need to store the x- and y-coordinates in intermediate variables, since we need to determine how far the mouse moved since the last time we updated the screen.
2 If we are drawing the object, we use the x- and y-coordinates as the second coordinate of the bounding box.
3 If we are moving the object, we calculate the difference between the current location and the last bounding box location.

10.2 A more complete drawing program

The examples so far demonstrate basic drawing methods, but a realistic drawing program must supply many more facilities. Let’s take a look at some of the features that we are adding in this example before studying the code:

![Drawing program screenshot showing various drawing tools and features](./images/drawing_program_screenshot.png)

Figure 10.6 Drawing program: extended features

1 A Toolbar to give access to a number of specific drawing tools and options:
   • Drawing tools for freehand curves, smoothed curves, straight (rubber) lines, open and filled rectangles, and open and filled ovals.
   • Provision to set the color of the line or outline of a drawn object.
   • Provision to set the width of the line or outline of a drawn object.
   • Provision to set the fill color of an object.
   • A limited number of stipple masks (to allow variable transparency).
2 Holding down the SHIFT key draws rectangles and ovals as squares and circles respectively.
3 An option to generate a PostScript file rendering the current content of the canvas.