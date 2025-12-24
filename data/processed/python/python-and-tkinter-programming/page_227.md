---
source_image: page_227.png
page_number: 227
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.08
tokens: 8311
characters: 2039
timestamp: 2025-12-24T00:37:38.174373
finish_reason: stop
---

when contrasted with using the pack or grid geometry managers. However, precise placement of graphical objects requires the precision of the place geometry manager.

The approach I took to implement this panel was to take a drawing of the panel and to perform some basic measurements. In figure 9.2, lines have been drawn marking the key dimensions that are needed to recreate a graphic representation. Making measurements on a drawing can be easier than performing the measurements on a real device. Overall width and height are measured in some standard units (such as inches or centimeters) and then the relative size of each of the rectangular objects and the relative offset of one corner of the object must be calculated. The offset is used for the placer calls in the code. The selected corner is the anchor for this call. It may appear to be a lot of work, but it takes just a few minutes to get the required information.

The example extends the class library to provide a number of new graphical elements; in the listings that follow, elements that have already been presented have been eliminated.

Components_1.py

from Tkinter import *
from GUICommon import *
from Common import *

class Screen(GUICommon):
    def __init__(self, master, bg=Color.PANEL, height=1, width=1):
        self.screen_frame = Frame(master, width=width, height=height,
                                  bg=bg, bd=0)
        self.base = bg
        self.set_colors(self.screen_frame)
        radius = 4   # radius of an air hole
        ssize = radius*3   # spacing between holes

        rows = int(height/ssize)
        cols = int(width/ssize)

        self.canvas = Canvas(self.screen_frame, height=height, width=width,
                             bg=bg, bd=0, highlightthickness=0)

        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        y = ssize - radius#
        for r in range(rows):
            x0 = ssize -radius
            for c in range(cols):
                x = x0 + (ssize*c)

1 creating an instance

2 Optimizing performance