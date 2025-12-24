---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.41
tokens: 8322
characters: 2067
timestamp: 2025-12-24T00:36:20.006591
finish_reason: stop
---

8.1.4 Tkinter variables

The previous example used Pmw widgets to provide setentry and get methods to give access to the widget’s content. Tk provides the ability to link the current value of many widgets (such as text, toggle and other widgets) to an application variable. Tkinter does not support this mode, instead it provides a Variable class which may be subclassed to give access to the variable, textvariable, value, and other options within the widget. Currently, Tkinter supports StringVar, IntVar, DoubleVar and BooleanVar. These objects define get and set methods to access the widget.

Example_8_5.py

from Tkinter import *

class Var(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.field = Entry()
        self.field.pack()

        self.value = StringVar()
        self.value.set("Jean-Paul Sartre")
        self.field["textvariable"] = self.value

        self.field.bind('<Key-Return>', self.print_value)

    def print_value(self, event):
        print 'Value is "%s"' % self.value.get()

test = Var()
test.mainloop()

Code comments

1 Remember that you cannot get directly at the Tk widget’s variable; you must create a Tkinter variable. Here we create an instance of StringVar.
2 Set the initial value.
3 Bind the variable to the textvariable option in the widget.
4 Extract the current value using the get method of the string variable.

If you run this example, you will see a dialog similar to figure 8.5. This is as simple a dialog as you would want to see; on the other hand, it really is not very effective, because the only way to get anything from the entry field is to press the RETURN key, and we do not give the user any information on how to use the dialog. Nevertheless, it does illustrate Tkinter variables!

Pmw provides built-in methods for setting and getting values within widgets, so you do not need to use Tkinter variables directly. In addition, validation, valuechanged (modified) and selection callbacks are defined as appropriate for the particular widget.