---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.68
tokens: 8134
characters: 845
timestamp: 2025-12-24T00:35:15.752666
finish_reason: stop
---

work management alarm levels) along with the blink on/off state, which may be selected at instantiation. The LED class also defines the methods to set the status and blink state at run-time. Figure 7.1 demonstrates the wide range of LED formats that can be generated from this simple class.

![LED Example - Stage 1](./images/led_example.png)

Figure 7.1 LED example

Example_7_1.py

from Tkinter import *

SQUARE = 1
ROUND = 2
ARROW = 3

POINT_DOWN = 0
POINT_UP = 1
POINT_RIGHT = 2
POINT_LEFT = 3

STATUS_OFF = 1
STATUS_ON = 2
STATUS_WARN = 3
STATUS_ALARM = 4
STATUS_SET = 5

class StructClass:
    pass

Color = StructClass()

Color.PANEL = '#545454'
Color.OFF = '#656565'
Color.ON = '#00FF33'
Color.WARN = '#ffcc00'
Color.ALARM = '#ff4422'

class LED:
    def __init__(self, master=None, width=25, height=25,
                 appearance=FLAT,