---
source_image: page_319.png
page_number: 319
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.82
tokens: 8451
characters: 1933
timestamp: 2025-12-24T00:40:25.219160
finish_reason: stop
---

```python
self.xorigin+self.awidth-self.hoffset, self.yorigin+self.voffset,
self.xorigin-self.hoffset, self.yorigin+self.voffset,
self.xorigin, self.yorigin, fill='', outline=self.lineColor)

self.canvas.create_rectangle(self.xorigin, self.yorigin-self.vheight,
    self.xorigin+self.awidth, self.yorigin,
    fill='', outline=self.lineColor)

self.canvas.create_polygon(self.xorigin, self.yorigin,
    self.xorigin-self.hoffset, self.yorigin+self.voffset,
    self.xorigin-self.hoffset, self.yorigin+self.voffset-self.vheight,
    self.xorigin, self.yorigin-self.vheight,
    fill='', outline=self.lineColor)

self.canvas.create_text(self.xorigin-self.hoffset-5,
    self.yorigin+self.voffset, text='%d' % self.minY,
    fill=self.lineColor, anchor=E)
self.canvas.create_text(self.xorigin-self.hoffset-5,
    self.yorigin+self.voffset-self.vheight, text='%d' % \
    self.maxY, fill=self.lineColor, anchor=E)

self.canvas.create_text(self.xorigin-self.hoffset,
    self.yorigin+self.voffset+5, text='%d' % self.minX,
    fill=self.lineColor, anchor=N)
self.canvas.create_text(self.xorigin+self.awidth-self.hoffset,
    self.yorigin+self.voffset+5, text='%d' % self.maxX,
    fill=self.lineColor, anchor=N)

def initData(self):
    self.minY = 0
    self.maxY = 100
    self.minX = 0
    self.maxX = 100
    self.steps = 100
    self.rows = 10
    self.spectrum = Pmw.Color.spectrum(self.steps, saturation=0.8,
        intensity=0.8, extraOrange=1)
    self.lineColor = 'gray80'
    self.lowThresh = 30
    self.highThresh = 70

def transform(self, base, factor):
    rgb = self.winfo_rgb(base)
    retval = "#"
    for v in [rgb[0], rgb[1], rgb[2]]:
        v = (v*factor)/256
        if v > 255: v = 255
        if v < 0:   v = 0
        retval = "%s%02x" % (retval, v)
    return retval

def plotData(self, row, rowdata):
    rootx = self.xorigin - (row*self.hrowoff)
    rooty = self.yorigin + (row*self.vrowoff)
    cidx = 0
```