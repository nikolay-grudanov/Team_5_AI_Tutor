---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.62
tokens: 8477
characters: 2369
timestamp: 2025-12-24T00:35:32.589511
finish_reason: stop
---

7 Finally, we react to the result of validation, setting the widget’s content. In the case of a validation error, we reset focus to the widget. Here we set the flag to ignore the resulting focus event:

self._ignoreEvent = 1

6.8.3 Formatted (smart) widgets

Several data-entry formats benefit from widgets that format data as it is entered. Some examples include dates, times, telephone numbers, Social Security numbers and Internet (IP) addresses. Making this work may reintroduce some of the issues that were solved by the previous example, since the ideal behavior of the widget is to update the format continuously as opposed to the alternate scheme of reformatting the field after it has been entered. This introduces even more problems. Take entering a phone number, for example. Several number groupings are typical:

1  1-(401) 111-2222   Full number with area code
2  1-401-111-2222     Full number separated with dashes
3  401-111-2222       Area code and number without 1
4  111-2222            Local number
5  017596-475222      International (United Kingdom)
6  3-1111-2222        International (Japan)

With so many combinations, it is important that the user is shown the format of the telephone number, or other data, in the label for the widget. If your application has requirements to accommodate a range of conflicting formats, it may be better to format the string after it has been entered completely or else leave the formatting to the user. For date and time fields, you might want to use Pmw widgets, which help the user get the input in the correct format.

For other formats, you are going to have to write code. This example demonstrates how to format phone numbers and Social Security numbers.

Example_6_9.py

import string
from Tkinter import *

class EntryFormatting:
    def __init__(self, master):
        frame = Frame(master)
        Label(frame, text='    ').grid(row=0, column=0, sticky=W)
        Label(frame, text='    ').grid(row=0, column=3, sticky=W)

        self._ipaddr = self.createField(frame, width=16, row=0, col=2,
            label='Phone Number:\n(nnn)-nnn-nnn',
            format=self.fmtPhone, enter=self.activate)
        self._crdprt = self.createField(frame, width=11, row=1, col=2,
            label='SSN#: ', format=self.fmtSSN,
            enter=self.activate)
        frame.pack(side=TOP, padx=15, pady=15)