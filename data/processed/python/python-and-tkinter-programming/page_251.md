---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.38
tokens: 8322
characters: 1880
timestamp: 2025-12-24T00:38:24.371032
finish_reason: stop
---

self.dataReady = FALSE
self.root.after(5, self.buildScanner)
self.multimeter = MeterServer()
self.root.after(500, self.doPoll)

buildScanner converts the GIF files to photo images and this is a time-consuming task. By moving the initialization to the background, we can display the base GUI immediately (although the user has to wait for all of the images to load before proceeding).

4 buildRule constructs tickmarks used by the multimeter to indicate the currently measured value relative to full-scale deflection of the selected range and to animate a graphic when the value is over range.

Example_9_1.py (continued)

def animate(self):
    if self.action:
        self.canvas.create_line(self.animX,155, self.animX,167,
            width=2,fill="#333377",
            tags='anim')
        self.animX = self.animX + self.Xincr
        if self.animX > self.X1:
            self.animX= self.X
            self.canvas.delete('anim')
            self.root.after(30, self.animate)
    else:
        self.canvas.delete('anim')

def stopAnimation(self):
    self.action = FALSE

def buildScanner(self):
    self.primary_lookup = {}
    for key, hasr, rfmt, un, sec in PRIMARY_DATA:
        if not self.primary_lookup.has_key(key):
            self.primary_lookup[key] = []
            self.primary_lookup[key].append((hasr, rfmt, un, sec))
    keys = SECONDARY_DATA.keys()
    for key in keys:
        img = SECONDARY_DATA[key][-2]
        try:
            if getattr(self, 'i%s' % key):
                pass    # Already done...
        except:
            setattr(self, 'i%s' % key,
                PhotoImage(file="images/%s.gif" % img))
    self.dataReady = TRUE

def doPoll(self):
    if self.dataReady:
        result = self.multimeter.poll()
        if result:
            self.updateDisplay(result)
    self.root.after(1000, self.doPoll)

def getRange(self, tag, val, units):