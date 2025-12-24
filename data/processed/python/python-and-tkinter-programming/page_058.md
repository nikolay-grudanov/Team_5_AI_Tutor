---
source_image: page_058.png
page_number: 58
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.32
tokens: 8390
characters: 1963
timestamp: 2025-12-24T00:33:00.139846
finish_reason: stop
---

Label(t3, text='No wm decorations', bg='blue', fg='white').pack(padx=10, pady=10)
t3.overrideredirect(1)
t3.geometry('200x70+150+150')

root.mainloop()

Note The use of the option_readfile call in each of the examples to set application-wide defaults for colors and fonts is explained in “Setting application-wide default fonts and colors” on page 49. This call is used to ensure that most examples have consistent fonts and predictable field sizes.

Documentation for the Toplevel widget starts on page 539.

4.1.2 Frame

Frame widgets are containers for other widgets. Although you can bind mouse and keyboard events to callbacks, frames have limited options and no methods other than standard widget options.

One of the most common uses for a frame is as a master for a group of widgets which will be handled by a geometry manager. This is shown in figure 4.2. The second frame example, shown in figure 4.3 below, uses one frame for each row of the display.

![Frame widget](figure_4_2.png)

Figure 4.2 Frame widget

for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
    f = Frame(root, borderwidth=2, relief=relief)
    Label(f, text=relief, width=10).pack(side=LEFT)
    f.pack(side=LEFT, padx=5, pady=5)

In a similar manner to buttons and labels, the appearance of the frame can be modified by choosing a relief type and applying an appropriate borderwidth. (See figure 4.3.) In fact, it can be hard to tell the difference between these widgets. For this reason, it may be a good idea to reserve particular decorations for single widgets and not allow the decoration for a label to be used for a button, for example:

class GUI:
    def __init__(self):
        of = [None]*5
        for bdw in range(5):
            of[bdw] = Frame(self.root, borderwidth=0)
            Label(of[bdw], text='borderwidth = %d ' % bdw).pack(side=LEFT)
            ifx = 0
            iff = []
            for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]: