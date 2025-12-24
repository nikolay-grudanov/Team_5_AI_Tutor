---
source_image: page_328.png
page_number: 328
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.80
tokens: 8420
characters: 2263
timestamp: 2025-12-24T00:40:41.870525
finish_reason: stop
---

self.text = Text(frame3, width=20, height=3, highlightthickness=2)
self.text.insert(END, 'Tabs are valid here')
self.text.grid(row=0, col=1, columnspan=3)

frame.pack(fill=X, expand=1)
frame2.pack(fill=X, expand=1)
frame3.pack(fill=X, expand=1)

def mkbutton(self, frame, button, column, action=None):
    button = Button(frame, text=button, highlightthickness=2)
    button.grid(padx=10, pady=6, row=0, col=column, sticky=NSEW)
    if action:
        button.config(command=action)
    return button

def disable(self):
    self.B2.configure(state=DISABLED, background='cadetblue')
    self.Focus.configure(state=DISABLED, background='cadetblue')

def enable(self):
    self.B2.configure(state=NORMAL, background=self.B1.cget('background'))
    self.Focus.configure(state=NORMAL,
                         background=self.B1.cget('background'))

def focus(self):
    self.B3.focus_set()

root = Tk()
root.title('Navigation')
top = Navigation(root)
quit = Button(root, text='Quit', command=root.destroy)
quit.pack(side=BOTTOM, pady=5)

root.mainloop()

Code comments

① To show where keyboard focus is, we must give the highlight size, since the default for a Frame is 0. The color is also set so that it is easy to see.

② The Text widget also requires highlightthickness to be set. Text widgets are in the class of widgets that do not propagate TAB characters so you cannot navigate out of a Text widget using the TAB key (you must use CTRL-TAB).

③ Buttons are window-system dependent. On Win32, buttons show their highlight as a dotted line, whereas Motif widgets require you to set the highlight width. If your application is targeted solely for Win32, you could omit the highlightthickness option.

Let’s run the code in example 12.1 and see how TAB-key navigation works:

Each time you press the TAB key, the focus will move to the next widget in the group. To reverse the traversal, use the SHIFT-TAB key. In the second frame in figure 12.1, you can see that the frame is showing a highlight. Tkinter gets the order of the widgets right if you make sure that the widgets are presented to the geometry manager in the order that you want to navigate. If you do not take care, you will end up with the focus jumping all over the GUI as you attempt to navigate.