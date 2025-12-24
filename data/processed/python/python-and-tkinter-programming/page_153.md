---
source_image: page_153.png
page_number: 153
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.00
tokens: 8352
characters: 1939
timestamp: 2025-12-24T00:35:35.767207
finish_reason: stop
---

```python
self.shape = shape
self.Colors = [None, Color.OFF, Color.ON,
                Color.WARN, Color.ALARM, '#00ffdd']
self.status = status
self.blink = blink
self.blinkrate = int(blinkrate)
self.on = 0
self.onState = None

if not bg:
    bg = Color.PANEL

## Base frame to contain light
self.frame=Frame(master, relief=appearance, bg=bg, bd=bd,
                 takefocus=takefocus)

basesize = width
d = center = int(basesize/2)

if self.shape == SQUARE:
    self.canvas=Canvas(self.frame, height=height, width=width,
                       bg=bg, bd=0, highlightthickness=0)
    self.light=self.canvas.create_rectangle(0, 0, width, height,
                                            fill=Color.ON)
elif self.shape == ROUND:
    r = int((basesize-2)/2)
    self.canvas=Canvas(self.frame, width=width, height=width,
                       highlightthickness=0, bg=bg, bd=0)
    if bd > 0:
        self.border=self.canvas.create_oval(center-r, center-r,
                                           center+r, center+r)
        r = r - bd
    self.light=self.canvas.create_oval(center-r-1, center-r-1,
                                       center+r, center+r,
                                       fill=Color.ON,
                                       outline=outline)
else: # Default is an ARROW
    self.canvas=Canvas(self.frame, width=width, height=width,
                       highlightthickness=0, bg=bg, bd=0)

x = d
y = d
VL = ARROW_HEAD_VERTICES[orient] # Get the vertices for the arrow
self.light=self.canvas.create_polygon(eval(VL[0]),
                                      eval(VL[1]), eval(VL[2]), eval(VL[3]),
                                      eval(VL[4]), eval(VL[5]), eval(VL[6]),
                                      eval(VL[7]), outline = outline)

self.canvas.pack(side=TOP, fill=X, expand=NO)
self.update()

def update(self):
    # First do the blink, if set to blink
    if self.blink:
        if self.on:
```