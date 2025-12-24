---
source_image: page_275.png
page_number: 275
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.60
tokens: 8305
characters: 1811
timestamp: 2025-12-24T00:39:00.967203
finish_reason: stop
---

def selectFunc(self, tag):
    self.curFunc = self.func[tag]
    if self.curFunc:
        self.canvas.config(cursor='crosshair')
    else:
        self.canvas.config(cursor='arrow')
A cursor is also selected, appropriate for the current operation.

7 The mouse callbacks are similar to those in the earlier two examples.
8 This code implements the squaring or rounding of rectangles and ovals if the appropriate flags have been set.
9 The draw methods are quite similar to earlier examples with the addition of storing a list of line segments (for curved lines), smoothing and object attributes.

draw3.py (continued)

def storeObject(self):
    self.objects.append((self.startx, self.starty, self.lastx,
                         self.lasty, self.prevx, self.prevy, self.curFunc,
                         self.foreground, self.background, self.fillStyle,
                         self.lineWidth, self.lineData))

def redraw(self):
    self.canvas.delete(ALL)
    for startx, starty, lastx, lasty, prevx, prevy, func, \
        fg, bg, fill, lwid, ld, in self.objects:
        self.curObject = None
        func(startx, starty, lastx, lasty, prevx, prevy,
             fg, bg, fill, lwid, ld)

def initData(self):
    self.curFunc      = self.drawLine
    self.curObject    = None
    self.selObj       = None
    self.lineData     = []
    self.savedWidth   = 1
    self.objects      = []
    self.foreground   = 'black'
    self.background   = 'white'
    self.fillStyle    = None
    self.lineWidth    = 1
    self.regular      = FALSE

def ipostscript(self):  12
    postscript = self.canvas.postscript()
    fd = open('drawing.ps', 'w')
    fd.write(postscript)
    fd.close()

def close(self):
    self.quit()

def createInterface(self):
    AppShell.AppShell.createInterface(self)
    self.createButtons()