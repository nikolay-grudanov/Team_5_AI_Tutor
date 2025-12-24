---
source_image: page_268.png
page_number: 268
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.46
tokens: 8092
characters: 982
timestamp: 2025-12-24T00:38:37.817479
finish_reason: stop
---

10.1.1 Moving canvas objects

The selection of objects in the first example simply raises them in the display stack. If you were to raise a large object above smaller objects you could quite possibly prevent access to those objects. Clearly, we need to provide a more useful means of manipulating the drawn objects. Typically, draw tools move objects in response to a mouse drag. Adding this to the example is very easy. Here are the modifications which have been applied to draw.py:

![Figure 10.5 Moving objects on a canvas](./images/figure_10_5.png)

draw2.py

def mouseMotion(self, event):
    cx = self.canvas.canvasx(event.x)
    cy = self.canvas.canvasy(event.y)
    if self.currentFunc:
        self.lastx = cx
        self.lasty = cy
        self.canvas.delete(self.currentObject)
        self.currentFunc(self.startx, self.starty,
                         self.lastx, self.lasty,
                         self.foreground, self.background)
    else:
        if self.selObj: