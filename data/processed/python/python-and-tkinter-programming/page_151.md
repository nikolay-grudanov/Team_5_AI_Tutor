---
source_image: page_151.png
page_number: 151
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.95
tokens: 8268
characters: 1644
timestamp: 2025-12-24T00:35:29.455867
finish_reason: stop
---

7.1.1 Let’s try that again

One thing that most Python programmers quickly discover is that whenever they take a look at a piece of code they wrote some time before, it always seems possible to rewrite it in fewer lines of code. In addition, having written a segment of code, it is often possible to reuse that code in later segments.

To demonstrate the ability to reduce the amount of code required to support our example, let’s take a look at how we can improve the code in it. First, we’ll remove the constants that we defined at the start of the program and save the code in Common_7_1.py; I’m sure that we’ll be using these constants again in later examples.

Common_7_1.py

SQUARE      = 1
ROUND       = 2
...
...
Color.WARN  = '#ffcc00'
Color.ALARM = '#ff4422'

Now, we have an excellent opportunity to make the LED methods mixins, since we can readily reuse the basic methods of the LED class to construct other widgets.

GUICommon_7_1.py

from Common_7_1 import *

class GUICommon:
    def turnon(self):
        self.status = STATUS_ON
        if not self.blink: self.update()

    def turnoff(self):
        self.status = STATUS_OFF
        if not self.blink: self.update()

    def alarm(self):
        self.status = STATUS_ALARM
        if not self.blink: self.update()

    def warn(self):
        self.status = STATUS_WARN
        if not self.blink: self.update()

    def set(self, color):
        self.status      = STATUS_SET
        self.specialColor = color
        self.update()

    def blinkon(self):
        if not self.blink:
            self.blink   = 1
            self.onState = self.status
            self.update()