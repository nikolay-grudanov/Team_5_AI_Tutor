---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.62
tokens: 8352
characters: 2185
timestamp: 2025-12-24T00:32:36.987428
finish_reason: stop
---

3.1 Calculator example: key features

The calculator example illustrates many features of applications written in Python and Tkinter, including these:

• GUI application structure Although this is a simple example, it contains many of the elements of larger applications that will be presented later in the book.
• Multiple inheritance It is simple in this example, but it illustrates how it may be used to simplify Python code.
• Lists, dictionaries and tuples As mentioned in chapter 1, these language facilities give Python a considerable edge in building concise code. In particular, this example illustrates the use of a dictionary to dispatch actions to methods. Of particular note is the use of lists of tuples to define the content of each of the keys. Unpacking this data generates each of the keys, labels and associated bindings in a compact fashion.
• Pmw (Python megawidgets) The scrolled text widget is implemented with Pmw. This example illustrates setting its attributes and gaining access to its components.
• Basic Tkinter operations Creating widgets, setting attributes, using text tags, binding events and using a geometry manager are demonstrated.
• eval and exec functions The example uses eval to perform many of the math functions in this example. However, as you will see later in this chapter, eval cannot be used to execute arbitrary Python code; exec is used to execute single or multiple lines of code (and multiple lines of code can include control flow structures).

Figure 3.2
A better calculator

3.2 Calculator example: source code

calc2.py

from Tkinter import *
import Pmw

class SLabel(Frame):
    """ SLabel defines a 2-sided label within a Frame. The left hand label has blue letters; the right has white letters. """
    def __init__(self, master, leftl, rightl):
        Frame.__init__(self, master, bg='gray40')
        self.pack(side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=leftl, fg='steelblue1',
              font=("arial", 6, "bold"), width=5, bg='gray40').pack(
            side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=rightl, fg='white',
              font=("arial", 6, "bold"), width=1, bg='gray40').pack()