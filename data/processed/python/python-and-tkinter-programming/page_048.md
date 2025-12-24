---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.89
tokens: 8403
characters: 2363
timestamp: 2025-12-24T00:32:48.571765
finish_reason: stop
---

else:
    self.current = self.current[:-1]

def keyAction(self, key):
    self.display.insert(END, key)
    self.current = self.current + key

def evalAction(self, action):
    try:
        self.actionDict[action](action)
    except KeyError:
        pass

Code comments

① Pmw (Python MegaWidgets) widgets are used. These widgets will feature prominently in this book since they provide an excellent mechanism to support a wide range of GUI requirements and they are readily extended to support additional requirements.

② In the constructor for the Key class, we add key-value pairs to the kw (keyword) dictionary and then apply these values to the Button constructor.
    def __init__(self, master, font=('arial', 8, 'bold'),
                 fg='white', width=5, borderwidth=5, **kw):
        kw['font'] = font
        ...
        apply(Button.__init__, (self, master), kw)
    This allows us a great deal of flexibility in constructing our widgets.

③ The Calculator class uses a dictionary to provide a dispatcher for methods within the class.
    'matrix': self.doThis, 'program': self.doThis,
    'vars': self.doThis, 'clear': self.clearall,
    'sin': self.doThis, 'cos': self.doThis,
    Remember that dictionaries can handle much more complex references than the relatively simple cases we need for this calculator.

④ We use a Pmw ScrolledText widget, which is a composite widget. To gain access to the contained widgets, the component method is used.
    self.display.component('text').delete(1.0, END)

⑤ When the ENTER key is clicked, the collected string is directed to the calculator’s evaluator:
    result = self.calc.runpython(self.current)
    The result of this evaluation is displayed in the scrolled text widget.

⑥ The final argument in the text insert function is a text tag 'ans' which is used to change the foreground color of the displayed text.
    self.display.insert(END, '%s\n' % result, 'ans')

⑦ doKeypress is a callback bound to all keys. The event argument in the callback provides the client data for the callback. event.char is the key entered; several attributes are available in the client data, such as x-y coordinates of a button press or the state of a mouse operation (see “Tkinter events” on page 98). In this case we get the character entered.

⑧ A simple exception mechanism to take action on selected keys is used.