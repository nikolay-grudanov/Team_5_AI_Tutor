---
source_image: page_155.png
page_number: 155
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.45
tokens: 8335
characters: 1640
timestamp: 2025-12-24T00:35:34.997873
finish_reason: stop
---

GUICommon_7_2.py (modifications only)

# This routine modifies an RGB color (returned by winfo_rgb),
# applies a factor, maps -1 < Color < 255, and returns a new RGB string
def transform(self, rgb, factor):
    retval = "#"
    for v in [rgb[0], rgb[1], rgb[2]]:
        v = (v*factor)/256
        if v > 255: v = 255
        if v < 0:   v = 0
        retval = "%s%02x" % (retval, v)
    return retval

# This routine factors dark, very dark, light, and very light colors
# from the base color using transform
def set_colors(self):
    rgb = self.winfo_rgb(self.base)
    self.dbase  = self.transform(rgb, 0.8)
    self.vdbase = self.transform(rgb, 0.7)
    self.lbase  = self.transform(rgb, 1.1)
    self.vlbase = self.transform(rgb, 1.3)

Code comments

① We calculate color variations derived from the base color. winfo_rgb returns a tuple for the RGB values.

② We set arbitrary values for each of the color transformations.

The following example illustrates the use of these routines:

Example_7_3.py

from Tkinter import *
from GUICommon_7_2 import *

import string

class TestColors(Frame, GUICommon):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.base = "#848484"
        self.pack()
        self.set_colors()
        self.make_widgets()

    def make_widgets(self):
        for tag in ['VDBase', 'DBase', 'Base', 'LBase', 'VLBase']:
            Button(self, text=tag, bg=getattr(self, '%s'% string.lower(tag)),
                   fg='white', command=self.quit).pack(side=LEFT)

if __name__ == '__main__':
    TestColors().mainloop()

Running Example_7_3.py displays the screen shown in figure 7.3: