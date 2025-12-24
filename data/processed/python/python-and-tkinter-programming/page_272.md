---
source_image: page_272.png
page_number: 272
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.08
tokens: 8343
characters: 2042
timestamp: 2025-12-24T00:38:56.024397
finish_reason: stop
---

('foval',    self.drawFilledOval, 'Filled oval')]:
    ToolBarButton(self, self.toolbar, key, '%s.gif' % key,
        command=self.selectFunc, balloonhelp=balloon,
        statushelp=balloon)
    self.func[key] = func

def createLineWidths(self):
    ToolBarButton(self, self.toolbar, 'sep', 'sep.gif', width=10,
        state='disabled')
    for width in ['1', '3', '5']:
        ToolBarButton(self, self.toolbar, width, 'tline%s.gif' % \
            width, command=self.selectWidth,
            balloonhelp='%s pixel linewidth' % width,
            statushelp='%s pixel linewidth' % width)

def createLineColors(self):
def createFillColors(self):
def createPatterns(self):

# --- Code Removed ---------------------------------------------------------------

Code comments
① The ToolBarButton class implements a simple iconic button. A bitmap or PhotoImage may be used for the icon.
② We establish bindings for the Label widget, since we have to create our own button-press animation when the user clicks on the button or places the cursor over the button.
③ Forcing rectangles to be squares and ovals to be circles is achieved by binding a <Keypress> event to the root window. When we receive the callback, we have to check that the SHIFT key is pressed and set a flag accordingly.

self.root.bind("<KeyPress>", self.setRegular)
self.root.bind("<KeyRelease>", self.setRegular)
def setRegular(self, event):
    if event.type == '2' and event.keysym == 'Shift_Left':
        self.regular = TRUE

④ We create a dispatch table for the various drawn object types, with a display name, function, and Balloon help text.
⑤ The method to create each group of toolbar buttons is essentially the same, so some of the code has been removed for brevity.

draw3.py (continued)

def selectFunc(self, tag):
    self.curFunc = self.func[tag]
    if self.curFunc:
        self.canvas.config(cursor='crosshair')
    else:
        self.canvas.config(cursor='arrow')

def selectWidth(self, tag):
def selectBackground(self, tag):
def selectForeground(self, tag):