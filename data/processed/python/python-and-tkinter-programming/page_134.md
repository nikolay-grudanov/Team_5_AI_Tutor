---
source_image: page_134.png
page_number: 134
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.10
tokens: 8243
characters: 1434
timestamp: 2025-12-24T00:34:54.648730
finish_reason: stop
---

class Indicator:
    def __init__(self, master=None, label='', value=0.0):
        self.var = DoubleVar()
        self.s = Scale(master, label=label, variable=self.var,
            from_=0.0, to=300.0, orient=HORIZONTAL,
            length=300)
        self.var.set(value)
        self.s.pack()

def setTemp():
    slider = random.choice(range(10))
    value = random.choice(range(0, 300))
    slist[slider].var.set(value)
    root.after(5, setTemp)

slist = []
for i in range(10):
    slist.append(Indicator(root, label='Probe %d' % (i+1)))
setTemp()
root.mainloop()

Code comments
① First we create a Tkinter variable. For this example we store a real value:
    self.var = DoubleVar()
② We then bind it to the Tk variable:
    self.s = Scale(master, label=label, variable=self.var,
③ Then we set its value. This immediately updates the widget to display the new value:
    self.var.set(value)
④ The purpose of the setTemp function is to create a value randomly for one of the “sensors” at 5 millisecond intervals.
⑤ The variable is updated for each change:
    slist[slider].var.set(value)
⑥ Since after is a one-shot timer, we must set up the next timeout:
    root.after(5, setTemp)'
⑦ The call to setTemp starts the simulated stream of sensor information.

The display for this example is not reproduced here (the code is available online, of course). However, the display’s behavior resembles Brownian motion, with widgets con-