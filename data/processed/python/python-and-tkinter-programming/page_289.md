---
source_image: page_289.png
page_number: 289
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.08
tokens: 8370
characters: 2009
timestamp: 2025-12-24T00:39:22.284161
finish_reason: stop
---

self.menuBar.addmenuitem('File', 'command', 'Exit program',
    label='Exit', command=self.quit)

def createTools(self):
    self.func      = {}
    self.transFunc = {}  ③
    ToolBarButton(self, self.toolbar, 'sep', 'sep.gif',
        width=10, state='disabled')
    for key, func, balloon in [
        ('pointer', None, 'Edit drawing'),
        ('draw',    self.drawFree, 'Draw freehand'),
        ('smooth',  self.drawSmooth, 'Smooth freehand'),
        ('line',    self.drawLine, 'Rubber line'),
        ('rect',    self.drawRect, 'Unfilled rectangle'),
        ('frect',   self.drawFilledRect, 'Filled rectangle'),
        ('oval',    self.drawOval, 'Unfilled oval'),
        ('foval',   self.drawFilledOval, 'Filled oval')]:
        ToolBarButton(self, self.toolbar, key, '%s.gif' % key,
            command=self.selectFunc, balloonhelp=balloon,
            statushelp=balloon)
        self.func[key]    = func
        self.transFunc[func] = key

# --- Code Removed ---------------------------------------------------------------

Code comments
① The ToolBarButton class has been moved to a separate module.
② transDict is going to be used when we parse the tags assigned to each of the grab handles. See ⑥ below.
③ transFunc is created as a reverse-lookup, so that we can find the key associated with a particular function.

draw4.py (continued)

def mouseDown(self, event):
    self.curObject = None
    self.canvas.dtag('drawing')
    self.lineData = []
    self.lastx = self.startx = self.canvas.canvasx(event.x)
    self.lasty = self.starty = self.canvas.canvasy(event.y)
    self.uniqueID = 'S*%d' % self.serial
    self.serial = self.serial + 1  ④

    if not self.curFunc:
        if event.widget.find_withtag(CURRENT):
            tags = self.canvas.gettags(CURRENT)
            for tag in tags:
                if tag[:2] == 'S*':
                    objectID = tag
                if 'grabHandle' in tags:
                    self.inGrab = TRUE
                    self.releaseGrab = FALSE  ⑤