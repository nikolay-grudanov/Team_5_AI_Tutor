---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.75
tokens: 8367
characters: 2137
timestamp: 2025-12-24T00:39:00.759745
finish_reason: stop
---

```python
def selectPattern(self, tag):
    # --- Code Removed -------------------------------------------------------------
    def mouseDown(self, event):
        self.curObject = None
        self.canvas.dtag('drawing')
        self.lineData = []
        self.lastx = self.startx = self.canvas.canvasx(event.x)
        self.lasty = self.starty = self.canvas.canvasy(event.y)
        if not self.curFunc:
            self.selObj = self.canvas.find_closest(self.startx, self.starty)[0]
            self.savedWidth = string.atoi(self.canvas.itemcget(
                self.selObj, 'width'))
            self.canvas.itemconfig(self.selObj,
                width=self.savedWidth + 2)
            self.canvas.lift(self.selObj)

    def mouseMotion(self, event):
        curx = self.canvas.canvasx(event.x)
        cury = self.canvas.canvasy(event.y)
        prevx = self.lastx
        prevy = self.lasty
        if self.curFunc:
            self.lastx = curx
            self.lasty = cury

        if self.regular and self.canvas.type('drawing') in \
            ['oval','rectangle']:
            dx      = self.lastx - self.startx
            dy      = self.lasty - self.starty
            delta   = max(dx, dy)
            self.lastx = self.startx + delta
            self.lasty = self.starty + delta
            self.curFunc(self.startx, self.starty, self.lastx,
                self.lasty, prevx, prevy, self.foreground,
                self.background, self.fillStyle, self.lineWidth,None)
        else:
            if self.selObj:
                self.canvas.move(self.selObj, curx-prevx, cury-prevy)
                self.lastx = curx
                self.lasty = cury

    def mouseUp(self, event):
        self.prevx = self.lastx
        self.prevy = self.lasty
        self.lastx = self.canvas.canvasx(event.x)
        self.lasty = self.canvas.canvasy(event.y)
        if self.curFunc:
            if self.regular and self.canvas.type('drawing') in \
                ['oval','rectangle']:
                dx      = self.lastx - self.startx
                dy      = self.lasty - self.starty
                delta   = max(dx, dy)
```