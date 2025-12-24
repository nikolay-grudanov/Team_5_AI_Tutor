---
source_image: page_132.png
page_number: 132
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.56
tokens: 8407
characters: 2470
timestamp: 2025-12-24T00:35:09.495883
finish_reason: stop
---

Unfortunately this doesn’t work, because the event is bound at the application level. The widget still has a binding for BACKSPACE, so after the application level has been invoked and \h has been inserted into the widget, the event is propagated to the class level and the h is removed.

There is a simple solution: return “break” from the last event handler that you want to propagate events from and the superior levels don’t get the event. So, the callback looks like this:

def dobackspace(event):
    event.widget.insert(END, '\\\h')
    return "break"

6.6 Timers and background procedures

The mainloop supports callbacks which are not generated from events. The most important result of this is that it is easy to set up timers which call callbacks after a predetermined delay or whenever the GUI is idle. Here is a code snippet from an example later in the book:

if self.blink:
    self.frame.after(self.blinkrate * 1000, self.update)

def update(self):
    # Code removed
    self.canvas.update_idletasks()
    if self.blink:
        self.frame.after(self.blinkrate * 1000, self.update)

This code sets up to call self.update after self.blinkrate * 1000 milliseconds. The callback does what it does and then sets up to call itself again (these timers are called once only—if you want them to repeat you must set them up again).

For more information on timers, see “Common options” on page 425.

6.7 Dynamic callback handlers

A single callback is frequently bound to an event for the duration of an application. However, there are many cases where we need to change the bindings to the widget to support application requirements. One example might be attaching a callback to remove reverse video (that was applied as the result of a validation error) on a field when a character is input.

Getting dynamic callbacks to work is simply a matter of binding and unbinding events. We saw examples of this in Example_6_3.py on page 105, and there are other examples in the source code.

Note If you find that you are constantly binding and unbinding events in your code, it may be a good idea to review the reasons why you are doing this. Remember that events can be generated in rapid succession—mouse movement, for example, generates a slew of events. Changing bindings during an event storm may have unpredictable results and can be very difficult to debug. Of course, we burn CPU cycles as well, so it can have a considerable effect on application performance.