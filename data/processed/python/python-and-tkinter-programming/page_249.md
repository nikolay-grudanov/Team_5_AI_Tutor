---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.06
tokens: 8254
characters: 1530
timestamp: 2025-12-24T00:38:11.790092
finish_reason: stop
---

The data is sent as a 14-character string. The first two characters (Tag) determine the category. The position of the decimal point, in conjunction with the units, determines the range.

Here is the main code to support the application:

Example_9_1.py

from Common import *
from Tkinter import *
from Example_9_1_data import *
import sys, time, string

class MeterServer:
    def __init__(self):
        # Open up the serial port
        pass

    def poll(self):
        import random
        choice = random.choice(range(0, len(TESTDATA)-1))
        return TESTDATA[choice]

class MultiMeter:
    def __init__(self, master):
        self.root = master
        self.root.title("Digital Multimeter")
        self.root.iconname('22-168a')

        self.holdVal = '0.0'
        self.curRange = None
        self.lineOpen = FALSE

        self.canvas = Canvas(self.root, width=300, height=694)
        self.canvas.pack(side="top", fill=BOTH, expand='no')

        self.img = PhotoImage(file='images/multimeter.gif')
        self.canvas.create_image(0,0,anchor=NW, image=self.img)
        self.buildRule()

        self.root.update()
        self.root.after(5, self.buildSymbols)
        self.dataReady = FALSE
        self.root.after(5, self.buildScanner)
        self.multimeter = MeterServer()
        self.root.after(500, self.doPoll)

    def buildSymbols(self):
        for x, y, font, txt, tag in PANEL_LABELS:
            self.canvas.create_text(x, y, text=txt,
                font=(font, 12),
                fill="gray75",