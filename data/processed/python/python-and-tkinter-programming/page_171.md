---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.60
tokens: 8227
characters: 1654
timestamp: 2025-12-24T00:36:02.630643
finish_reason: stop
---

Figure 8.3  A tkSimpleDialog that is used to collect passwords. The error dialog is displayed for bad entries.

8.1.3 Single-shot forms

If your application has simple data requirements, you may need only simple forms. Many user interfaces implement a simple model:

1  Display some fields, maybe with default values.
2  Allow the user to fill out or modify the fields.
3  Collect the values from the screen.
4  Do something with the data.
5  Display the results obtained with the values collected.

If you think about the applications you’re familiar with, you’ll see that many use pretty simple, repetitive patterns. As a result, building forms has often been viewed as a rather tedious part of developing GUIs; I hope that I can make the task a little more interesting.

There is a problem in designing screens for applications that do not need many separate screens; developers tend to write a lot more code than they need to satisfy the needs of the application. In fact, code that supports forms often consumes more lines of code than we might prefer. Later, we will look at some techniques to reduce the amount of code that has to be written, but for now let’s write the code in full.

This example collects basic information about a user and displays some of it. The example uses Pmw widgets and is a little bit longer than it needs to be, so that we can cover the basic framework now; we will leave those components out in subsequent examples.

Example_8_4.py

from Tkinter import *
import Pmw
import string

class Shell:
    def __init__(self, title=''):
        self.root = Tk()
        Pmw.initialise(self.root)
        self.root.title(title)