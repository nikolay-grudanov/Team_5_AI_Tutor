---
source_image: page_271.png
page_number: 271
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.71
tokens: 8391
characters: 2262
timestamp: 2025-12-24T00:39:00.520351
finish_reason: stop
---

```python
def buttonUp(self, event):
    if self.state != 'disabled':
        if self.command != None:
            self.command()
        time.sleep(0.05)
        self.config(relief='flat', bg=self.bg)

class Draw(AppShell.AppShell):
    usecommandarea = 1
    appname = 'Drawing Program - Version 3'
    frameWidth = 840
    frameHeight = 600

    def createButtons(self):
        self.buttonAdd('Postscript',
            helpMessage='Save current drawing (as PostScript)',
            statusMessage='Save drawing as PostScript file',
            command=self.ipostscript)
        self.buttonAdd('Refresh', helpMessage='Refresh drawing',
            statusMessage='Redraw the screen', command=self.redraw)
        self.buttonAdd('Close', helpMessage='Close Screen',
            statusMessage='Exit', command=self.close)

    def createBase(self):
        self.toolbar = self.createcomponent('toolbar', (), None,
            Frame, (self.interior(),), background="gray90")
        self.toolbar.pack(fill=X)

        self.canvas = self.createcomponent('canvas', (), None,
            Canvas, (self.interior(),), background="white")
        self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)

        Widget.bind(self.canvas, "<Button-1>", self.mouseDown)
        Widget.bind(self.canvas, "<Button1-Motion>", self.mouseMotion)
        Widget.bind(self.canvas, "<Button1-ButtonRelease>", self.mouseUp)
        self.root.bind("<KeyPress>", self.setRegular)
        self.root.bind("<KeyRelease>", self.setRegular)

    def setRegular(self, event):
        if event.type == '2' and event.keysym == 'Shift_L':
            self.regular = TRUE
        else:
            self.regular = FALSE

    def createTools(self):
        self.func = {}
        ToolBarButton(self, self.toolbar, 'sep', 'sep.gif',
            width=10, state='disabled')
        for key, func, balloon in [
            ('pointer', None, 'Edit drawing'),
            ('draw', self.drawFree, 'Draw freehand'),
            ('smooth', self.drawSmooth, 'Smooth freehand'),
            ('line', self.drawLine, 'Rubber line'),
            ('rect', self.drawRect, 'Unfilled rectangle'),
            ('frect', self.drawFilledRect, 'Filled rectangle'),
            ('oval', self.drawOval, 'Unfilled oval'),
```