---
source_image: page_099.png
page_number: 99
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.36
tokens: 8323
characters: 1829
timestamp: 2025-12-24T00:34:13.964853
finish_reason: stop
---

4.4.2 Options

In addition to the options for the scale and gauge components, we will need to define some options for the megawidget. First, we define min and max to allow the programmer the range supported by the widget. Secondly, we define fill and size to control the color and size of the gauge. Lastly, we define value to allow us to set the initial value of the megawidget.

4.4.3 Creating the megawidget class

Pmw megawidgets inherit from either Pmw.MegaWidget, Pmw.MegaToplevel or Pmw.Dialog. The gauge widget is intended to be used within other code widgets so it inherits from Pmw.MegaWidget. Here is the code for the megawidget.

pmw_megawidget.py

from Tkinter import *
import Pmw

class Gauge(Pmw.MegaWidget):
    def __init__(self, parent=None, **kw):
        # Define the options for the megawidget
        optiondefs = (
            ('min', 0, Pmw.INITOPT),
            ('max', 100, Pmw.INITOPT),
            ('fill', 'red', None),
            ('size', 30, Pmw.INITOPT),
            ('value', 0, None),
            ('showvalue', 1, None),
        )

        self.defineoptions(kw, optiondefs)

        # Initialize the base class
        Pmw.MegaWidget.__init__(self, parent)

        interior = self.interior()

        # Create the gauge component
        self.gauge = self.createcomponent('gauge',
            (), None,
            Frame, (interior,),
            borderwidth=0)
        self.canvas = Canvas(self.gauge,
            width=self['size'], height=self['size'],
            background=interior.cget('background'))
        self.canvas.pack(side=TOP, expand=1, fill=BOTH)
        self.gauge.grid()

        # Create the scale component
        self.scale = self.createcomponent('scale',
            (), None,
            Scale, (interior,),
            command=self._setGauge,
            length=200,