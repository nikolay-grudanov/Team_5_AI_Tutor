---
source_image: page_131.png
page_number: 131
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.98
tokens: 8319
characters: 2091
timestamp: 2025-12-24T00:34:55.001114
finish_reason: stop
---

text.pack()
frame.pack()
text.focus_set()
root.mainloop()

Code comments

1 First, the callbacks are defined. These are all simple examples and all but the last one take account of the event object being passed as the callback’s argument, from which we extract the keysym of the key generating the event.

def displayHelp(event):
    print 'hlp', event.keysym

2 Although the class-level binding was made with a method call to an Entry widget, bind_class is an inherited method, so any instance will work and root.unbind_class is quite acceptable. This is not true for an instance binding, which is local to the instance.

3 We make an application-level binding:

root.bind_all('<F1>', displayHelp)

4 In this class-level binding we use a lambda function to construct an argument list for the callback:

text.bind_class('Entry', '<KeyPress>', lambda e, x=101: sayKey(e,x))

5 Here we make a toplevel binding for a print-screen callback:

root.bind('<Alt_L>', printWindow)

6 Finally, we make instance bindings with double modifiers:

frame.bind('<Control-Shift-Down>', cursor)
text.bind('<Control-Shift-Up>', unbindThem)

Note Be prepared to handle multiple callbacks for events if you use combinations of the four binding levels that have overlapping bindings.
Tkinter selects the best binding at each level, starting with any instance bindings, then toplevel bindings, followed by any class bindings. Finally, application level bindings are selected. This allows you to override bindings at any level.

6.5.2 Handling multiple bindings

As I mentioned in the note above, you can bind events at each of the four binding events. However, because events are propagated, that might not result in the behavior that you intended.

For a simple example, suppose you want to override the behavior of a widget, and rather than have BACKSPACE remove the previous character, you want to insert \h into the widget. So you set up the binding like this:

text.bind('<BackSpace>', lambda e: dobackspace(e))

and define the callback like this:

def dobackspace(event):

    event.widget.insert(END, '\\h')