---
source_image: page_291.png
page_number: 291
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.56
tokens: 8480
characters: 2479
timestamp: 2025-12-24T00:39:34.374637
finish_reason: stop
---

```python
self.lastx = curx
self.lasty = cury
else:
    self.canvas.move('grab', curx-prevx, cury-prevy)
    self.lastx = curx
    self.lasty = cury

def mouseUp(self, event):
    self.prevx = self.lastx
    self.prevy = self.lasty
    self.lastx = self.canvas.canvasx(event.x)
    self.lasty = self.canvas.canvasy(event.y)
    if self.curFunc:
        if self.regular and self.curFunc in \
            [self.func['oval'], self.func['rect'],
             self.func['foval'],self.func['frect']]:
            dx = self.lastx - self.startx
            dy = self.lasty - self.starty
            delta = max(dx, dy)
            self.lastx = self.startx + delta
            self.lasty = self.starty + delta
            self.curFunc(self.startx, self.starty, self.lastx,
                         self.lasty, self.prevx, self.prevy, self.foreground,
                         self.background, self.fillStyle, self.lineWidth,
                         self.lineData)
        self.inGrab = FALSE
        self.releaseGrab = TRUE
        self.growFunc = None
        self.storeObject(self.startx, self.starty, self.lastx,
                         self.lasty, self.prevx, self.prevy, self.curFunc,
                         self.foreground, self.background, self.fillStyle,
                         self.lineWidth, self.lineData)
    else:
        if self.inGrab:
            tags = self.canvas.gettags(CURRENT)
            for tag in tags:
                if '*' in tag:
                    key, value = string.split(tag, '*')
                    var = transDict[key]
                    setattr(self, var, string.atoi(value))
                    x1,y1,x2,y2, px, py, self.growFunc, \
                        fg,bg,fill,lwid,ld = self.objects[self.uniqueID]
                    if self.boundX == 1 and self.adjX:
                        x1 = x1 + self.lastx-self.prevx
                    elif self.boundX == 2 and self.adjX:
                        x2 = x2 + self.lastx-self.prevx
                    if self.boundY == 1 and self.adjY:
                        y1 = y1 + self.lasty-self.prevy
                    elif self.boundY == 2 and self.adjY:
                        y2 = y2 + self.lasty-self.prevy
                    self.growFunc(x1,y1,x2,y2,px,py,fg,bg,fill,lwid,ld)
                    self.storeObject(x1,y1,x2,y2,px,py,self.growFunc,
                                     fg,bg,fill,lwid,ld)
                    self.addGrabHandles(self.uniqueID, self.uniqueID)
if self.selObj:
```