---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.19
tokens: 8389
characters: 2137
timestamp: 2025-12-24T00:35:34.603410
finish_reason: stop
---

```python
status=STATUS_ON, bd=1,
bg=None,
shape=SQUARE, outline="",
blink=0, blinkrate=1,
orient=POINT_UP,
takefocus=0):
    # Preserve attributes
    self.master = master
    self.shape = shape
    self.onColor = Color.ON
    self.offColor = Color.OFF
    self.alarmColor = Color.ALARM
    self.warningColor = Color.WARN
    self.specialColor = '#00ffdd'
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
                                           center+r, center+r, fill=Color.ON,
                                           outline=outline)
    else:  # Default is an ARROW
        self.canvas=Canvas(self.frame, width=width, height=width,
                           highlightthickness=0, bg=bg, bd=0)
        x = d
        y = d
        if orient == POINT_DOWN:  #1
            self.light=self.canvas.create_polygon(x-d,y-d, x,y+d,
                                                   x+d,y-d, x-d,y-d, outline=outline)
        elif orient == POINT_UP:
            self.light=self.canvas.create_polygon(x,y-d, x-d,y+d,
                                                   x+d,y+d, x,y-d, outline=outline)
```