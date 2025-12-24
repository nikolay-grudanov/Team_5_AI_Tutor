---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.30
tokens: 8364
characters: 2088
timestamp: 2025-12-24T00:35:48.535318
finish_reason: stop
---

pretty boring, we can add some pizzazz to any GUI that represents any device which has on/off controls. We are also going to introduce some animation, albeit simple.

Note In subsequent examples, GUICommon.py and Common.py will be edited directly, rather than creating new versions each time.

We need to define two more constants in Common.py because switches point up when on in the U.S., but point down when on in the UK (I know that this is an arcane property of switches in these countries, but it is important to the locals!):

Common.py

MODE_UK      = 0
MODE_US      = 1

Here is the code to draw a toggle switch:

Example_7_5.py

from Tkinter    import *
from GUICommon  import *
from Common     import *
from Example_7_4 import HexNut

class ToggleSwitch(Frame, HexNut):
    def __init__(self, master, outside=70, inset=8, bg=Color.PANEL,
                 nutbase=Color.CHROME, mount=1, frame=1,
                 top=NUT_POINT, mode=MODE_US, status=STATUS_ON):
        Frame.__init__(self)
        HexNut.__init__(self,master=master, outside=outside+40,
                        inset=35, frame=frame, mount=mount,
                        bg=bg, nutbase=nutbase, top=top)
        self.status = status
        self.mode   = mode
        self.center = (outside+44)/2
        self.r     = (outside/2)-4
        ## First Fill in the center
        self.r1=self.canv.create_oval(self.center-self.r,
                                      self.center-self.r, self.center+self.r,
                                      self.center+self.r, fill=self.vdbase,
                                      outline=self.dbase, width=1)
        self.update()  ## The rest is dependent on the on/off state

    def update(self):
        self.canv.delete('lever')  ## Remove any previous toggle lever
        direction = POINT_UP
        if (self.mode == MODE_UK and self.status == STATUS_ON) or \
           (self.mode == MODE_US and self.status == STATUS_OFF):
            direction = POINT_DOWN
        # Now update the status
        if direction == POINT_UP:  ①
            ## Draw the toggle lever