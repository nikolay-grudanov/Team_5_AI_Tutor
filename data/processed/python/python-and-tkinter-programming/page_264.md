---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.87
tokens: 8190
characters: 1235
timestamp: 2025-12-24T00:38:38.272312
finish_reason: stop
---

Figure 10.2 A very simple drawing program

def createBase(self):
    self.width = self.root.winfo_width()-10
    self.height = self.root.winfo_height()-95
    self.command= self.createcomponent('command', (), None,
        Frame, (self.interior(),), width=self.width*0.25,
        height=self.height, background="gray90")
    self.command.pack(side=LEFT, expand=YES, fill=BOTH)

    self.canvas = self.createcomponent('canvas', (), None,
        Canvas, (self.interior(),), width=self.width*0.73,
        height=self.height, background="white")
    self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)

    Widget.bind(self.canvas, "<Button-1>", self.mouseDown)
    Widget.bind(self.canvas, "<Button1-Motion>", self.mouseMotion)
    Widget.bind(self.canvas, "<Button1-ButtonRelease>", self.mouseUp)

    self.radio = Pmw.RadioSelect(self.command, labelpos = None,
        buttontype = 'radiobutton', orient = VERTICAL,
        command = self.selectFunc, hull_borderwidth = 2,
        hull_relief = RIDGE,)
    self.radio.pack(side = TOP, expand = 1)

    self.func = {}
    for text, func in ( ('Select', None),
        ('Rectangle', self.drawRect),
        ('Oval', self.drawOval),
        ('Line', self.drawLine)):

DRAWING ON A CANVAS