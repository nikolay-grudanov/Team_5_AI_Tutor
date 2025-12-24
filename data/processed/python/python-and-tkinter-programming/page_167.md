---
source_image: page_167.png
page_number: 167
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.53
tokens: 8257
characters: 1586
timestamp: 2025-12-24T00:36:02.174965
finish_reason: stop
---

label_text='Returned value:  ',
labelpos=W, labelmargin=1)
self.result.pack(padx=15, pady=15)

root = Tk()
question = App(root)

button = askquestion("Question:",
    "Oh Dear, did somebody\nsay mattress to Mr Lambert?",
    default=NO)

question.result.setentry(button)

root.mainloop()

Code comments

① The first two arguments set the title and prompt (since this is a question dialog).
② default sets the button with the selected string to be the default action (the action associated with pressing the RETURN key).
③ The standard dialogs return the button pressed as a string—for example, ok for the OK button, cancel for the CANCEL button.

For this example, all of the standard dialogs are presented, both for Windows and UNIX architectures (the UNIX screens have light backgrounds); the screen corresponding to Example_8_1.py is the first screen in figure 8.1.

8.1.2 Data entry dialogs

A dialog can be used to request information from the user. Let’s take a quick look at how we query the user for data using the tkSimpleDialog module. Unlike many of our examples, this one is short and to the point:

Example_8_2.py

from Tkinter import *
from tkSimpleDialog import askinteger
import Pmw

class App:
    def __init__(self, master):
        self.result = Pmw.EntryField(master, entry_width=8,
            value='',
            label_text='Returned value:  ',
            labelpos=W, labelmargin=1)
        self.result.pack(padx=15, pady=15)

root = Tk()
display = App(root)

retVal = askinteger("The Larch",
    "What is the number of The Larch?",
    minvalue=0, maxvalue=50)