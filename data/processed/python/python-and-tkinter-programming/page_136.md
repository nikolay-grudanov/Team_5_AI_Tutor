---
source_image: page_136.png
page_number: 136
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.40
tokens: 8276
characters: 1803
timestamp: 2025-12-24T00:35:01.430297
finish_reason: stop
---

4 The update method sets the Tkinter variable with the current value, updating the widget’s display. To redraw the widgets, we call update_idletasks which processes events waiting on the event queue.

self.s.update_idletasks()

5 Now, when the value changes, we set the instance variable:

slist[slider].set(value)

The display now updates the widgets once a second, which results in a more relaxed display and noticeably lowers the CPU overhead. You can optimize the code more, if you wish, to further reduce the overhead. For example, the widgets could be updated from a single update timeout rather than from a one-per-widget call.

![Screenshot of a GUI window showing entry fields for Date, Time, Real, and Social Security number](./images/entry_field_validation.png)

Figure 6.2 Validating entry fields (Example_6_7.py)

6.8.2 Data verification

An important part of a GUI, which performs data entry, is verifying appropriate input values. This area can consume a considerable amount of time and effort for the programmer. There are several approaches to validating input, but we will not attempt to cover all of them here.

Pmw EntryField widgets provide built-in validation routines for common entryfield types such as dates, times and numeric fields. Using these facilities can save you a considerable amount of time. Here is a simple example of using Pmw validation:

Example_6_7.py

import time, string
from Tkinter import *
import Pmw

class EntryValidation:
    def __init__(self, master):
        now = time.localtime(time.time())
        self._date = Pmw.EntryField(master,
            labelfont = 'w', label_text = 'Date (mm/dd/yy):',
            value = '%d/%d/%d' % (now[1], now[2], now[0]),
            validate = {'validator':'date',
                'format':'mdy', 'separator':'/'})