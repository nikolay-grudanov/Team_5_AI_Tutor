---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.66
tokens: 8416
characters: 2671
timestamp: 2025-12-24T00:36:09.171814
finish_reason: stop
---

provide you with some readily-usable templates that may be used in your own applications. Many of the standard form methods will be used again in examples in later chapters.

Pmw widgets will be used extensively in the examples since these widgets encapsulate a lot of functionality and allow us to construct quite complex interfaces with a relatively small amount of code. The use and behavior of these widgets are documented in more detail in “Pmw reference: Python megawidgets” on page 542.

8.1 Dialogs

Dialogs are really just special cases of forms. In general, dialogs present warning or error messages to the user, ask questions or collect a limited number of values from the user (typically one value). You could argue that all forms are dialogs, but we don’t need an argument! Normally dialogs are modal: they remain displayed until dismissed. Modality can be application-wide or system-wide, although you must take care to make sure that system-modal dialogs are reserved for situations that must be acknowledged by the user before any other interaction is possible.

Note Exercise care in selecting when to use a modal dialog to get input from the user. You’ll have many opportunities to use other methods to get input from the user and using too many dialogs can be annoying to the user. A typical problem is an application that always asks “Are you sure you want to...” on almost every operation. This can be a valuable technique for novice users, but an expert soon finds the dialogs frustrating. It is important to provide a means to switch off such dialogs for expert users.

Tkinter provides a Dialog module, but it has the disadvantage of using X bitmaps for error, warning and other icons, and these icons do not look right on Windows or MacOS. The tkSimpleDialog module defines askstring, askinteger and askfloat to collect strings, integers and floats respectively. The tkMessageBox module defines convenience functions such as showinfo, showwarning, showerror and askyesno. The icons used for tkMessageBox are architecture-specific, so they look right on all the supported platforms.

8.1.1 Standard dialogs

Standard dialogs are simple to use. Several convenience functions are available in tkMessageBox, including showerror, showwarning and askretrycancel. The example shown here illustrates the use of just one form of available dialogs (askquestion). However, figure 8.1 shows all of the possible formats both for UNIX and Windows.

Example_8_1.py

from Tkinter import *
from tkMessageBox import askquestion
import Pmw

class App:
    def __init__(self, master):
        self.result = Pmw.EntryField(master, entry_width=8,
            value='',