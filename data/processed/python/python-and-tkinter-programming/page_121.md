---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.24
tokens: 8418
characters: 2607
timestamp: 2025-12-24T00:34:47.271613
finish_reason: stop
---

Readers familiar with events and event handlers in X or with Windows messages might wish to skip ahead to look at “Tkinter events” on page 98, since this information is specific to Tkinter.

6.1.1 What are events?

Events are notifications (messages in Windows parlance) sent by the windowing system (the X-server for X, for example) to the client code. They indicate that something has occurred or that the state of some controlled object has changed, either because of user input or because your code has made a request which causes the server to make a change.

In general, applications do not receive events automatically. However, you may not be aware of the events that have been requested by your programs indirectly, or the requests that widgets have made. For example, you may specify a command callback to be called when a button is pressed; the widget binds an activate event to the callback. It is also possible to request notification of an event that is normally handled elsewhere. Doing this allows your application to change the behavior of widgets and windows generally; this can be a good thing but it can also wreck the behavior of complex systems, so it needs to be used with care.

All events are placed in an event queue. Events are usually removed by a function called from the application’s mainloop. Generally, you will use Tkinter’s mainloop but it is possible for you to supply a specialized mainloop if you have special needs (such as a threaded application which needs to manage internal locks in a way which makes it impossible to use the standard scheme).

Tkinter provides implementation-independent access to events so that you do not need to know too much about the underlying event handlers and filters. For example, to detect when the cursor enters a frame, try the following short example:

Example_6_1.py

from Tkinter import *
root = Tk()

def enter(event):
    print 'Entered Frame: x=%d, y=%d' % (event.x, event.y)

frame = Frame(root, width=150, height=150)
frame.bind('<Any-Enter>', enter)        # Bind event
frame.pack()

root.mainloop()

The bind method of Frame is used to bind the enter callback to an Any-Enter event. Whenever the cursor crosses the frame boundary from the outside to the inside, the message will be printed.

Note This example introduces an interesting issue. Depending on the speed with which the cursor enters the frame, you will observe that the x and y coordinates show some variability. This is because the x and y values are determined at the time that the event is processed by the event loop not at the time the actual event occurs.