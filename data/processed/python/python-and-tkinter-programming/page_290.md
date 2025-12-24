---
source_image: page_290.png
page_number: 290
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.64
tokens: 8469
characters: 2197
timestamp: 2025-12-24T00:39:32.215434
finish_reason: stop
---

```python
self.uniqueID = objectID
else:
    self.inGrab = FALSE
    self.addGrabHandles(objectID, 'grab')
    self.canvas.config(cursor='fleur')
    self.uniqueID = objectID
else:
    self.canvas.delete("grabHandle")
    self.canvas.dtag("grabHandle")
    self.canvas.dtag("grab")

def mouseMotion(self, event):
    curx = self.canvas.canvasx(event.x)
    cury = self.canvas.canvasy(event.y)
    prevx = self.lastx
    prevy = self.lasty
    if not self.inGrab and self.curFunc:
        self.lastx = curx
        self.lasty = cury
        if self.regular and self.curFunc in \
            [self.func['oval'], self.func['rect'],
             self.func['foval'],self.func['frect']]:
            dx      = self.lastx - self.startx
            dy      = self.lasty - self.starty
            delta   = max(dx, dy)
            self.lastx = self.startx + delta
            self.lasty = self.starty + delta
            self.curFunc(self.startx, self.starty, self.lastx,
                         self.lasty, prevx, prevy, self.foreground,
                         self.background, self.fillStyle, self.lineWidth,None)
    elif self.inGrab:
        self.canvas.delete("grabbedObject")
        self.canvas.dtag("grabbedObject")
        tags = self.canvas.gettags(CURRENT)
        for tag in tags:
            if '*' in tag:
                key, value = string.split(tag, '*')
                var = transDict[key]
                setattr(self, var, string.atoi(value))
        self.uniqueID = 'S*%d' % self.uniqueIDINT
        x1, y1, x2, y2, px, py, self.growFunc, \
            fg, bg, fill, lwid, ld= self.objects[self.uniqueID]
        if self.boundX == 1 and self.adjX:
            x1 = x1 + curx-prevx
        elif self.boundX == 2 and self.adjX:
            x2 = x2 + curx-prevx
        if self.boundY == 1 and self.adjY:
            y1 = y1 + cury-prevy
        elif self.boundY == 2 and self.adjY:
            y2 = y2 + cury-prevy
        self.growFunc(x1,y1,x2,y2,px,py,fg,bg,fill,lwid,ld)
        self.canvas.addtag_withtag("grabbedObject",
                                   self.uniqueID)
        self.storeObject(x1,y1,x2,y2,px,py,self.growFunc,
                         fg,bg,fill,lwid,ld)
```