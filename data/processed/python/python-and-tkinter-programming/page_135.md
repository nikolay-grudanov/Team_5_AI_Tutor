---
source_image: page_135.png
page_number: 135
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.27
tokens: 8266
characters: 1521
timestamp: 2025-12-24T00:35:01.249939
finish_reason: stop
---

stantly displaying new values. In a “real” application, the update rate would be annoying to the user, and it requires throttling to create a reasonable update rate. Additionally, constantly redrawing the widgets consumes an exceptionally high number of CPU cycles. Compare Example_6_5.py with the code for Example_6_6.py.

Example_6_6.py

from Tkinter import *
import random
root = Tk()

class Indicator:
    def __init__(self, master=None, label='', value=0.0):
        self.var = DoubleVar()
        self.s = Scale(master, label=label, variable=self.var,
            from_=0.0, to=300.0, orient=HORIZONTAL,
            length=300)
        self.value = value
        self.var.set(value)
        self.s.pack()
        self.s.after(1000, self.update)

    def set(self, value):
        self.value = value

    def update(self):
        self.var.set(self.value)
        self.s.update_idletasks()
        self.s.after(1000, self.update)

def setTemp():
    slider = random.choice(range(10))
    value = random.choice(range(0, 300))
    slist[slider].set(value)
    root.after(5, setTemp)

slist = []
for i in range(10):
    slist.append(Indicator(root, label='Probe %d' % (i+1)))
setTemp()
root.mainloop()

Code comments

① In addition to the Tkinter variable, we create an instance variable for the widget’s current value:

    self.value = value

② An after timeout arranges for the update method to be called in one second:

    self.s.after(1000, self.update)

③ The class defines a set method to set the current value.