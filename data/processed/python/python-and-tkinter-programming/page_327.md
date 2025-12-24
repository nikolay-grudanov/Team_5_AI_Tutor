---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.78
tokens: 8547
characters: 2856
timestamp: 2025-12-24T00:40:51.197485
finish_reason: stop
---

There may be times when the mouse is unavailable (I’ve had problems with a cat sleeping on my desk and leaving mouse-jamming hairs!) or when an application is intended to be deployed in a hostile environment where a mouse just would not survive.

This method of navigation does require some discipline in how your GUI is created. The order in which focus moves between and within groups is determined by the order in which widgets are created. So careless maintenance of a GUI can result in erratic behavior, with focus jumping all over the screen. Also, some widgets cannot accept focus (if they are disabled, for instance) and others bind the navigation keys internally (the Text widget allows you to enter Tab characters, for instance).

It is also important to remember that the pointer always directs events (such as Enter, Leave and Button1) to the widget under it, regardless of where the keyboard focus is set. Thus, you may have to change focus to a widget if it does not take keyboard focus itself.

12.4 Building navigation into an application

Let’s look at a simple example which allows you to discover how widgets behave in the focus models and under certain states. Widgets with the takefocus option set to true are placed in the window’s tab group and focus moves from one widget to the next as the TAB key is pressed. If the widget’s highlightthickness is at least one pixel, you will see which widget currently has focus. One thing to note is that there is somewhat less control of the navigation model under Tkinter. This is not normally a problem, but X Window programmers may find the restrictions limiting.

Example_12_1.py

from Tkinter import *

class Navigation:
    def __init__(self, master):

        frame = Frame(master, takefocus=1, highlightthickness=2,
                      highlightcolor='blue')
        Label(frame, text='   ').grid(row=0, column=0, sticky=W)
        Label(frame, text='   ').grid(row=0, column=5, sticky=W)

        self.B1 = self.mkbutton(frame, 'B1', 1)
        self.B2 = self.mkbutton(frame, 'B2', 2)
        self.B3 = self.mkbutton(frame, 'B3', 3)
        self.B4 = self.mkbutton(frame, 'B4', 4)

        frame2 = Frame(master, takefocus=1, highlightthickness=2,
                       highlightcolor='green')
        Label(frame2, text='   ').grid(row=0, column=0, sticky=W)
        Label(frame2, text='   ').grid(row=0, column=4, sticky=W)
        self.Disable = self.mkbutton(frame2, 'Disable', 1, self.disable)
        self.Enable = self.mkbutton(frame2, 'Enable', 2, self.enable)
        self.Focus = self.mkbutton(frame2, 'Focus', 3, self.focus)

        frame3 = Frame(master, takefocus=1, highlightthickness=2,
                       highlightcolor='yellow')
        Label(frame3, text='   ').grid(row=0, column=0, sticky=W)
        Label(frame2, text='   ').grid(row=0, column=4, sticky=W)