---
source_image: page_232.png
page_number: 232
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.58
tokens: 8339
characters: 1894
timestamp: 2025-12-24T00:37:46.556076
finish_reason: stop
---

5 We index into a list to obtain the y-coordinate and the anchor-position for the place call. This valuable technique is used in many examples throughout the book.

bg=self.dbase).place(relx=1.0, rely=[1.0,0][torb],
    anchor=[SE,NE][torb])

6 If widgets are created in a complex GUI, there can be some somewhat ugly effects to the display if the window is realized. One of these effects is that with the pack or grid geometry managers, the widgets are readjusted several times as additional widgets are created. Another effect is that it takes longer to draw the widgets, since the system redraws the widgets several times as widget configurations change. The solution is to delay the realization of the outer container of the widget hierarchy:

self.outer.forget()

7 The loop populates the card rack with blank cards:

incr = 325/9
x = 0.0
for i in range(9):
    card =CardBlank(self.rack, width=incr-1, height=414)
    card.card_frame.place(x=x, y=0, anchor=NW)
    x = x + incr

8 Finally, we change the state of one of the LEDs on the display. You’ll learn more about this later.

self.psu2.led.turnoff()

Since the front panel will be built incrementally, for the purpose of illustration, a separate module, FrontPanel_1.py, is used to create the device.

FrontPanel.py

#!/bin/env/python

from Tkinter import *
from Components_1 import *
from GUICommon import *
from Common import *

class Router(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createChassis()

    def createChassis(self):
        self.chassis = Chassis(self)
        # Realize the outer frame (which
        # was forgotten when created)
        self.chassis.outer.pack(expand=0)

if __name__ == '__main__':
    root = Router()
    root.master.title("CisForTron")
    root.master.iconname("CisForTron")
    root.mainloop()

1 Realize the frame