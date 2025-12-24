---
source_image: page_309.png
page_number: 309
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.54
tokens: 8519
characters: 1900
timestamp: 2025-12-24T00:40:11.971177
finish_reason: stop
---

```python
return
self.canvas.configure(width=new_width, height=new_height)
self._setsize()
self.clear()
self.replot()

def bind(self, *args):
    apply(self.canvas.bind, args)

def _setsize(self):
    self.width = string.atoi(self.canvas.cget('width'))
    self.height = string.atoi(self.canvas.cget('height'))
    self.plotarea_size[0] = 0.97 * self.width
    self.plotarea_size[1] = 0.97 * -self.height
    xo = 0.5*(self.width-self.plotarea_size[0])
    yo = self.height-0.5*(self.height+self.plotarea_size[1])
    self.plotarea_origin = (xo, yo)

def draw(self, graphics, xaxis = None, yaxis = None):
    self.last_drawn = (graphics, xaxis, yaxis)
    p1, p2 = graphics.boundingBox()
    xaxis = self._axisInterval(xaxis, p1[0], p2[0])
    yaxis = self._axisInterval(yaxis, p1[1], p2[1])
    text_width = [0., 0.]
    text_height = [0., 0.]

    if xaxis is not None:
        p1 = xaxis[0], p1[1]
        p2 = xaxis[1], p2[1]
        xticks = self._ticks(xaxis[0], xaxis[1])
        bb = self._textBoundingBox(xticks[0][1])
        text_height[1] = bb[3]-bb[1]
        text_width[0] = 0.5*(bb[2]-bb[0])
        bb = self._textBoundingBox(xticks[-1][1])
        text_width[1] = 0.5*(bb[2]-bb[0])
    else:
        xticks = None
    if yaxis is not None:
        p1 = p1[0], yaxis[0]
        p2 = p2[0], yaxis[1]
        yticks = self._ticks(yaxis[0], yaxis[1])
        for y in yticks:
            bb = self._textBoundingBox(y[1])
            w = bb[2]-bb[0]
            text_width[0] = max(text_width[0], w)
            h = 0.5*(bb[3]-bb[1])
            text_height[0] = h
            text_height[1] = max(text_height[1], h)
    else:
        yticks = None
    text1 = [text_width[0], -text_height[1]]
    text2 = [text_width[1], -text_height[0]]
    scale = ((self.plotarea_size[0]-text1[0]-text2[0]) / \
             (p2[0]-p1[0]),
             (self.plotarea_size[1]-text1[1]-text2[1]) / \
```