---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.96
tokens: 8199
characters: 1511
timestamp: 2025-12-24T00:36:00.015066
finish_reason: stop
---

display.result.setentry(retVal)
root.mainloop()

Code comments
① askinteger can be used with just two arguments: title and prompt.
② In this case, a minimum and maximum value have been added. If the user types a value outside this range, a dialog box is displayed to indicate an error (see figure 8.1).

Note Avoid popping up dialogs whenever additional information is required from the user. If you find that the current form that is displayed frequently requires the user to supply additional information, it’s very possible that your original form design is inadequate. Reserve popup dialogs for situations which occur infrequently or for near-boundary conditions.

Running Example_8_2.py displays screens similar to those shown in figure 8.2.

![Figure 8.2 tkSimpleDialog: askinteger](https://i.imgur.com/3Q5z5QG.png)

Figure 8.2 tkSimpleDialog: askinteger

Despite the warning in the note above, if you have just a few fields to collect from the user, you can use dialog windows. This is especially true if the application doesn’t require the information every time it is run; adding the information to screens in the application adds complexity and clutters the screen. Using a dialog saves quite a bit of work, but it may not be particularly attractive, especially if you need to have more than two or three entry fields or if you need several widget types. However, this example is quite short and to the point.

Example_8_3.py
from Tkinter import *
from tkSimpleDialog import Dialog
import tkMessageBox