---
source_image: page_148.png
page_number: 148
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.83
tokens: 8251
characters: 1485
timestamp: 2025-12-24T00:35:28.134069
finish_reason: stop
---

```python
    elif orient == POINT_RIGHT:
        self.light=self.canvas.create_polygon(x-d,y-d, x+d,y,
            x-d,y+d, x-d,y-d, outline=outline)
    elif orient == POINT_LEFT:
        self.light=self.canvas.create_polygon(x-d,y, x+d,y+d,
            x+d,y-d, x-d,y, outline=outline)

    self.canvas.pack(side=TOP, fill=X, expand=NO)
    self.update()

def turnon(self):
    self.status = STATUS_ON
    if not self.blink: self.update()
def turnoff(self):
    self.status = STATUS_OFF
    if not self.blink: self.update()
def alarm(self):
    self.status = STATUS_ALARM
    if not self.blink: self.update()
def warn(self):
    self.status = STATUS_WARN
    if not self.blink: self.update()
def set(self, color):
    self.status = STATUS_SET
    self.specialColor = color
    self.update()
def blinkon(self):
    if not self.blink:
        self.blink = 1
        self.onState = self.status
        self.update()
def blinkoff(self):
    if self.blink:
        self.blink = 0
        self.status = self.onState
        self.onState = None
        self.on = 0
        self.update()

def blinkstate(self, blinkstate):
    if blinkstate:
        self.blinkon()
    else:
        self.blinkoff()

def update(self):
    # First do the blink, if set to blink
    if self.blink:
        if self.on:
            if not self.onState:
                self.onState = self.status
                self.status = STATUS_OFF
                self.on = 0
        else:
            if self.onState:
```