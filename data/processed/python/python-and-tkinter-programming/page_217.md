---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.31
tokens: 8162
characters: 1331
timestamp: 2025-12-24T00:37:22.730121
finish_reason: stop
---

lined in gray. The enlarged section shows the arrow keys in a little more detail. For each target, we need to determine the x-y coordinate of the top-left-hand corner and the x-y coordinate of the bottom-right-hand corner; together they define the rectangular area containing the button.

The next example demonstrates how a simple tool can be constructed to first collect the coordinates of rectangular areas on an image, and then to generate a simple program to test the image map. This example supports only rectangular targets; you may wish to extend it to support polygonal and other target shapes.

Example_8_12.py

from Tkinter import *
import sys, string
class MakeImageMap:

    def __init__(self, master, file=None):
        self.root = master
        self.root.title("Create Image Map")
        self.rubberbandBox = None
        self.coordinatedata = []
        self.file = file

        self.img = PhotoImage(file=file)
        self.width = self.img.width()
        self.height = self.img.height()

        self.canvas = Canvas(self.root, width=self.width,
                             height=self.height)
        self.canvas.pack(side=TOP, fill=BOTH, expand=0)
        self.canvas.create_image(0,0,anchor=NW, image=self.img)

        self.frame1 = Frame(self.root, bd=2, relief=RAISED)
        self.frame1.pack(fill=X)