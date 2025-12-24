---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.43
tokens: 8379
characters: 1658
timestamp: 2025-12-24T00:39:39.601002
finish_reason: stop
---

```python
ghandle = self.canvas.create_rectangle(x-2,y-2,x+2,y+2,
    outline='black', fill='black', tags=('grab',
    'grabHandle','%s'%tagBx,'%s'%tagBy,'%s'%tagX,
    '%s'%tagY,'%s'%objectID))

def storeObject(self, x1,y1,x2,y2,px,py,func,fg,bg,fill,lwid,ld):
    self.objects[self.uniqueID] = ( x1,y1,x2,y2,px,py,func,fg,bg,
        fill,lwid,ld )

def redraw(self):
    self.canvas.delete(ALL)
    keys = self.objects.keys()
    keys.sort()
    for key in keys:
        startx, starty, lastx, lasty, prevx, prevy, func, \
            fg, bg, fill, lwid , ld= self.objects[key]
        self.curObject = None
        self.uniqueID = key
        func(startx, starty, lastx, lasty, prevx, prevy,
            fg, bg, fill, lwid, ld)

def newDrawing(self):
    self.canvas.delete(ALL)
    self.initData()

def openDrawing(self):
    ofile = askopenfilename(filetypes=[("PTkP Draw", "ptk"),
        ("All Files", "*")])
    if ofile:
        self.currentName = ofile
        self.initData()
        fd = open(ofile)
        items = marshal.load(fd)
        for i in range(items):
            self.uniqueID, x1,y1,x2,y2,px,py,cfunc, \
                fg,bg,fill,lwid,ld = marshal.load(fd)
            self.storeObject(x1,y1,x2,y2,px,py,self.func[cfunc],
                fg,bg,fill,lwid,ld)
        fd.close()
    self.redraw()

def saveDrawing(self):
    self.doSave()

def saveAsDrawing(self):
    ofile = asksaveasfilename(filetypes=[("PTkP Draw", "ptk"),
        ("All Files", "*")])
    if ofile:
        self.currentName = ofile
        self.doSave()

def doSave(self):
    fd = open(self.currentName, 'w')
    keys = self.objects.keys()
    keys.sort()
```