---
source_image: page_254.png
page_number: 254
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.02
tokens: 8291
characters: 1793
timestamp: 2025-12-24T00:38:24.790757
finish_reason: stop
---

7 getRange parses the message received from the meter to determine the range and value to be displayed.

8 The meter holds the highest (or lowest) value measured. This code displays this data. The code is longer than we might expect because we have to be able to detect the most positive or the most negative value.

9 In this section of code, we change the overlaid selector knob position if the range has changed. Note that the previous image, tagged as control, is deleted first.

10 Finally, we update the annunciators according to the currently selected range. To simplify this, we fill the text stroke with either a very light or dark gray.

If we run Example_9_1.py we will observe the display shown in figure 9.12. As each value is displayed, the range selector is animated to indicate the range for the value. An example of the display is shown in figure 9.13.

To complete the example, we simply need to add asynchronous support to connect the multimeter. This makes use of a Python extension module, siomodule, which is readily available from the Python language site (http://www.python.org), with one small change to support an idiosyncrasy of the meter’s hand-shake protocol, but more about that in a moment. Extension modules are covered in detail in a later section, “Putting it all together...” on page 311. This module makes use of a commercial dll, which has been made available for general use (see “Sio-module” on page 625 for details). The necessary code changes are in Example_9_2.py:

Figure 9.12 Simulating measurements

Figure 9.13 Range selector animation

Example_9_2.py

from crilib import *
import sys, regex, serial, time, string, os
IGNORE = '\n\r'

class RS232(serial.Port):
    def __init__(self):
        serial.Port.__init__(self)

1 Load serial

2 Init UART