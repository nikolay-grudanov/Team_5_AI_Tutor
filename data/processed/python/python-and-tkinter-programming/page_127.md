---
source_image: page_127.png
page_number: 127
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.36
tokens: 8421
characters: 2692
timestamp: 2025-12-24T00:34:49.472481
finish_reason: stop
---

Note If you are new to handling events, you might find it useful to run Example_6_2.py to investigate the behavior of the system as you perform some simple tasks in the window. For example, holding the SHIFT key down creates a stream of events; moving the mouse creates a stream of motion events at an even greater frequency.

This may come as a surprise initially, since the events are normally invisible to the user (and to the programmer). It is important to be aware of this behavior and as you program to take account of how events will actually be generated. It is especially important to make sure that the callback does not do any intensive processing; otherwise, it is easy to cause severe performance problems.

6.3 Callbacks

Callbacks are simply functions that are called as the result of an event being generated. Handling arguments, however, can be problematic for beginning Tkinter programmers, and they can be a source of latent bugs, even for seasoned programmers.

The number of arguments depends on the type of event that is being processed and whether you bound a callback directly or indirectly to an event. Here is an example of an indirect binding:

btn = Button(frame, text='OK', command=buttonAction)

command is really a convenience function supplied by the Button widget which calls the buttonAction callback when the widget is activated. This is usually a result of a <Button-Press-1> event, but a <KeyPress-space> is also valid, if the widget has focus. However, be aware that many events have occurred as a result of moving and positioning the mouse before the button was activated.

We could get the same effect by binding directly:

btn.bind('<Button-1>', buttonAction)
btn.bind('<KeyPress-space>', buttonAction)

So what is the difference? Well, apart from the extra line of code to bind the events directly, the real difference is in the invocation of the callback. If the callback is invoked from the event, the event object will be passed as the first (in this case the only) argument of the callback.

Note Event handlers can be a source of latent bugs if you don’t completely test your applications. If an event is bound (intentionally or erroneously) to a callback and the callback does not expect the event object to be passed as an argument, then the application could potentially crash. This is more likely to happen if the event rarely occurs or is difficult to simulate in testing.

If you want to reuse buttonAction and have it called in response to both direct and indirect events, you will have to write the callback so that it can accept variable arguments:

def buttonAction(event=None):
    if event:
        print 'event in: %s' % event.type