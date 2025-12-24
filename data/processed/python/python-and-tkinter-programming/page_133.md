---
source_image: page_133.png
page_number: 133
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.88
tokens: 8342
characters: 2230
timestamp: 2025-12-24T00:35:01.250035
finish_reason: stop
---

6.8 Putting events to work

In several of the early chapters, we saw examples of setting widgets with data and of getting that data and using it in our applications. In “Dialogs and forms” on page 140, we will see several schemes for presenting and getting data. This is an important topic that may require some ingenuity on your part to devise correct behavior. In the next few paragraphs, I’ll present some ideas to help you solve your own requirements.

6.8.1 Binding widgets to dynamic data

Tkinter provides a simple mechanism to bind a variable to a widget. However, it not possible to use an arbitrary variable. The variable must be subclassed from the Variable class; several are predefined and you could define your own, if necessary. Whenever the variable changes, the widget’s contents are updated with the new value. Look at this simple example:

Example_6_4.py

from Tkinter import *
root = Tk()

class Indicator:
    def __init__(self, master=None, label='', value=0):
        self.var = BooleanVar()
        self.i = Checkbutton(master, text=label, variable = self.var,
            command=self.valueChanged)
        self.var.set(value)
        self.i.pack()

    def valueChanged(self):
        print 'Current value = %s' % ['Off','On'][self.var.get()]

ind = Indicator(root, label='Furnace On', value=1)
root.mainloop()

This example defines self.var and binds it to the widget’s variable; it also defines a callback to be called whenever the value of the widget changes. In this example the value is changed by clicking the checkbutton—it could equally be set programmatically.

Setting the value as a result of an external change is a reasonable scenario, but it can introduce performance problems if the data changes rapidly. If our GUI contained many widgets that displayed the status and values of components of the system, and if these values changed asynchronously (for instance, each value arrived in the system as SNMP traps), the overhead of constantly updating the widgets could have an adverse effect on the application’s performance. Here is a possible implementation of a simple GUI to monitor the temperature reported by ten sensors.

Example_6_5.py

from Tkinter import *
import random
root = Tk()