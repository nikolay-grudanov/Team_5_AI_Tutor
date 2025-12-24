---
source_image: page_230.png
page_number: 230
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.29
tokens: 8436
characters: 2398
timestamp: 2025-12-24T00:37:46.630365
finish_reason: stop
---

The structure of the code for this example requires that we make sure that instances of objects are unique. Each widget must keep references to its child widgets.

self.screen_frame = Frame(master, width=width, height=height,
    bg=bg, bd=0)

This creates a specific instance of screen_frame within self.

2 The air-intake screen illustrates the ease with which repeated graphical objects may be created. It also highlights the importance of careful code construction—it is easy to forget that Python is an interpreted language and it is important to ensure that code is constructed in a way that optimizes execution.

    y = ssize - radius
    for r in range(rows):
        x0 = ssize -radius
        for c in range(cols):
            x = x0 + (ssize*c)
            self.canvas.create_oval(x-radius, y-radius,
                x+radius, y+radius,
                fill=self.dbase,
                outline=self.lbase)
        y = y + ssize

Some additional code might be appropriate here, since the first air intake is the “tall” by “narrow” case, but the lower intake has an opposite aspect. The loop could be improved by having the outer loop iterate over largest dimension to reduce some of the math operations in the inner loop. Of course, this would increase the code complexity and for many operations might be unnecessary, but is worth considering. Remember that a good C or C++ would optimize loops for you; you are Python’s optimizer!

3 GUICommon.set_colors has been extended to pass a widget to provide access to winfo early in the initializer.

    def __init__(self, master, label='I   0', base=Color.PANEL):
        self.base = base
        self.set_colors(master)

In this case, the master container widget and base color have been passed in the constructor and are used to set the color variants for the object.

Components_1.py (continued)

class CardPuller(GUICommon):

    def __init__(self, master, torb, width=20):
        self.base = master['background']
        self.set_colors(master)
        self.puller_frame=Frame(master, width=width, height=32,
            bg=self.lbase, relief='flat')

        Frame(self.puller_frame, width=width/8, height=8,
            bg=self.dbase).place(relx=1.0, rely=[1.0,0][torb],
                anchor=[SE,NE][torb])

        Frame(self.puller_frame, width=width/3, height=24,
            bg=self.vdbase).place(relx=1.0, rely=[0,1.0][torb],