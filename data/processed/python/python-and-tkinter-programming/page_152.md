---
source_image: page_152.png
page_number: 152
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.45
tokens: 8361
characters: 1820
timestamp: 2025-12-24T00:35:35.974558
finish_reason: stop
---

def blinkoff(self):
    if self.blink:
        self.blink = 0
        self.status = self.onState
        self.onState = None
        self.on=0
        self.update()

def blinkstate(self, blinkstate): ①
    if blinkstate:
        self.blinkon()
    else:
        self.blinkoff()

def update(self):
    raise NotImplementedError

# The following define drawing vertices for various
# graphical elements
ARROW_HEAD_VERTICES = [
    ['x-d', 'y-d', 'x', 'y+d', 'x+d', 'y-d', 'x-d', 'y-d'],
    ['x', 'y-d', 'x-d', 'y+d', 'x+d', 'y+d', 'x', 'y-d'],
    ['x-d', 'y-d', 'x+d', 'y', 'x-d', 'y+d', 'x-d', 'y-d'],
    ['x-d', 'y', 'x+d', 'y+d', 'x+d', 'y-d', 'x-d', 'y']]

Code comments
① Note that although we have added methods such as turnon and blinkoff, we have defined an update method that raises a NotImplementedError. Since every widget will use very different display methods, this serves as a reminder to the developer that he is responsible for providing a method to override the base class.
② The previous code used a four-case if-elif-else statement to process the arrow direction. I like to remove these whenever possible, so we’ll take a different approach to constructing the code. Instead of breaking out the individual vertices for the arrow graphic, we are going to store them in yet another list, ARROW_HEAD_VERTICES, for later use.

Example_7_2.py
from Tkinter import *
from Common_7_1 import *
from GUICommon_7_1 import *

class LED(GUICommon):
    def __init__(self, master=None, width=25, height=25,
                 appearance=FLAT,
                 status=STATUS_ON, bd=1,
                 bg=None,
                 shape=SQUARE, outline='',
                 blink=0, blinkrate=1,
                 orient=POINT_UP,
                 takefocus=0):
        # Preserve attributes
        self.master = master