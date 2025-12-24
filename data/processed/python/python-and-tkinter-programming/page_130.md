---
source_image: page_130.png
page_number: 130
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.30
tokens: 8247
characters: 1579
timestamp: 2025-12-24T00:34:49.911206
finish_reason: stop
---

Class level
Binding at the class level allows you to make sure that classes behave uniformly across an application. In fact, Tkinter binds this way to provide standard bindings for widgets. You will probably use class binding if you implement new widgets, or you might use class binding to provide audio feedback for entry fields across an application, for example.

Toplevel window level
Binding a function at the root level allows an event to be generated if focus is in any part of a shell. This might be used to bind a print screen function, for example.

Instance level
We have already seen several examples of this, so we will not say any more at this stage.
The following hypothetical example illustrates all four of the binding modes together.

Example_6_3.py

from Tkinter import *
def displayHelp(event):
    def displayHelp(event):
        print 'hlp', event.keysym

def sayKey(event):
    print 'say',event.keysym, event.char

def printWindow(event):
    print 'prt', event.keysym

def cursor(*args):
    print 'cursor'

def unbindThem(*args):
    root.unbind_all('<F1>')
    root.unbind_class('Entry', '<KeyPress>')
    root.unbind('<Alt_L>')
    frame.unbind('<Control-Shift-Down>')
    print 'Gone...'

root = Tk()
frame = Frame(root, takefocus=1, highlightthickness=2)
text = Entry(frame, width=10, takefocus=1, highlightthickness=2)

root.bind_all('<F1>', displayHelp)

text.bind_class('Entry', '<KeyPress>', lambda e, x=101: sayKey(e,x))

root.bind('<Alt_L>', printWindow)

frame.bind('<Control-Shift-Down> , cursor)

text.bind('<Control-Shift-Up>', unbindThem)