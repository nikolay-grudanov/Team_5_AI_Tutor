---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.82
tokens: 8420
characters: 2161
timestamp: 2025-12-24T00:39:16.552500
finish_reason: stop
---

arrow.py

from Tkinter import *

class ArrowEditor:
    def __init__(self, master, width=500, height=350):
        Label(master, text="This widget allows you to experiment "
            "with different widths and arrowhead shapes for lines "
            "in canvases. To change the line width or the shape "
            "of the arrowhead, drag any of the three boxes "
            "attached to the oversized arrow. The arrows on the "
            "right give examples at normal scale. The text at "
            "the bottom shows the configuration options as you'd "
            "enter them for a canvas line item.",
            wraplength="5i", justify=LEFT).pack(side=TOP)
        self.control=Frame(master)
        self.control.pack(side=BOTTOM, fill=X, padx=2)
        Button(self.control, text='Quit', command=master.quit).pack()
        self.canvas = Canvas(master, width=width, height=height,
            relief=SUNKEN, borderwidth=2)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.a    = 8   # Setup default values
        self.b    = 10
        self.c    = 3
        self.width= 2
        self.motionProc = None
        self.x1   = 40
        self.x2   = 350
        self.y    = 150
        self.smallTips= (5,5,2)
        self.bigLine= 'SkyBlue2'
        self.boxFill= ''
        self.activeFill = 'red'

        self.arrowSetup()   # Draw default arrow
        self.canvas.tag_bind('box', '<Enter>', lambda e, s=self:
            s.canvas.itemconfig(CURRENT, fill='red'))
        self.canvas.tag_bind('box', '<Leave>', lambda e, s=self:
            s.canvas.itemconfig(CURRENT, fill=''))
        self.canvas.tag_bind('box1', '<1>', lambda e, s=self:
            s.motion(s.arrowMove1))
        self.canvas.tag_bind('box2', '<1>', lambda e, s=self:
            s.motion(s.arrowMove2) )
        self.canvas.tag_bind('box3', '<1>', lambda e, s=self:
            s.motion(s.arrowMove3))
        self.canvas.tag_bind('box', '<B1-Motion>', lambda e,
            s=self: s.motionProc(e))
        self.canvas.bind('<Any-ButtonRelease-1>', lambda e,
            s=self: s.arrowSetup())

    def motion(self, func):
        self.motionProc = func