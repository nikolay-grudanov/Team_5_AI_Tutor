---
source_image: page_162.png
page_number: 162
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.80
tokens: 8300
characters: 1957
timestamp: 2025-12-24T00:35:57.673679
finish_reason: stop
---

```python
Example_7_6.py

from Tkinter    import *
from Common     import *
from Components import *

class SwitchIndicator:
    def __init__(self, master, outside=70, bg=Color.PANEL,
                 metal=Color.CHROME, mount=1, frame=1,
                 shape=ROUND, top=NUT_POINT, mode=MODE_US, status=1):
        self.frame = Frame(master, bg=bg)
        self.frame.pack(anchor=N, expand=YES, fill=X)

        self.led = LED(self.frame, width=outside, height=outside,
                        status=status, bg=bg, shape=shape,
                        outline=metal)
        self.led.frame.pack(side=TOP)

        self.switch = ToggleSwitch(self.frame, mount=mount,
                                   outside=outside, nutbase=metal,
                                   mode=mode, bg=bg, top=top,
                                   status=status)
        self.switch.frame.pack(side=TOP)
        self.update()

    def update(self):
        self.led.update()
        self.switch.update()

class TestComposite(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        # List of switches to display,
        # with sizes and other attributes
        switches = [(NUT_POINT, 0, STATUS_OFF, MODE_US),
                    (NUT_FLAT,1, STATUS_ON,   MODE_US),
                    (NUT_FLAT,0, STATUS_ON,   MODE_UK),
                    (NUT_POINT, 0, STATUS_OFF, MODE_UK)]

        frame = Frame(self, bg="gray80")
        frame.pack(anchor=N, expand=YES, fill=X)

        for top, mount, state, mode in switches:
            SwitchIndicator(frame,
                            mount=mount,
                            outside=20,
                            metal=Color.CHROME,
                            mode=mode,
                            bg="gray80",
                            top=top,
                            status=state).frame.pack(side=LEFT,
```