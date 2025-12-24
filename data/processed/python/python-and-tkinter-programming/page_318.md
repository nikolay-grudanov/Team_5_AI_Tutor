---
source_image: page_318.png
page_number: 318
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.03
tokens: 8161
characters: 1061
timestamp: 2025-12-24T00:40:09.017963
finish_reason: stop
---

Figure 11.7 three-dimensional graphical display

self.buttonAdd('Close',
    helpMessage='Close Screen',
    statusMessage='Exit',
    command=self.close)

def createBase(self):
    self.width = self.root.winfo_width()-10
    self.height = self.root.winfo_height()-95
    self.canvas = self.createcomponent('canvas', (), None,
        Canvas, (self.interior(),), width=self.width,
        height=self.height, background="black")
    self.canvas.pack(side=TOP, expand=YES, fill=BOTH)

    self.awidth = int(self.width * 0.68)
    self.aheight = int(self.height * 0.3)
    self.hoffset = self.awidth / 3
    self.voffset = self.aheight +3
    self.vheight = self.voffset / 2
    self.hrowoff = (self.hoffset / self.rows)
    self.vrowoff = self.voffset / self.rows
    self.xincr = float(self.awidth) / float(self.steps)
    self.xorigin = self.width/3.7
    self.yorigin = self.height/3
    self.yfactor = float(self.vheight) / float(self.maxY-self.minY)

    self.canvas.create_polygon(self.xorigin, self.yorigin,
        self.xorigin+self.awidth, self.yorigin,