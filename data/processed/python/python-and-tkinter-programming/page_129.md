---
source_image: page_129.png
page_number: 129
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.36
tokens: 8358
characters: 2321
timestamp: 2025-12-24T00:34:55.001025
finish_reason: stop
---

self.kw = kw

    def __call__(self, *args, **kw):
        args = self.args + args
        kw.update(self.kw)
        apply(self.func, args, kw)

Then, you define the callback like this:

Button(text='label', command=Command(function, arg [, moreargs...]) )

The reference to the function and arguments (including keywords) that are passed to the Command class are stored by its constructor and then passed on to the function when the callback is activated. This format for defining the callbacks may be a little easier to read and maintain than the lambda expression. At least there are alternatives!

6.5 Binding events and callbacks

The examples so far have demonstrated how to bind an event handler to an instance of a widget so that its behavior on receiving an event will not be inherited by other instances of the widget. Tkinter provides the flexibility to bind at several levels:

1 At the application level, so that the same binding is available in all windows and widgets in the application, so long as one window in the application has focus.
2 At the class level, so that all instances of widgets have the same behavior, at least initially.
3 At the shell (Toplevel or root) level.
4 At the instance level, as noted already.

Binding events at the application and class level must be done carefully, since it is quite easy to create unexpected behavior in your application. In particular, indiscriminate binding at the class level may solve an immediate problem, but cause new problems when new functionality is added to the application.

Note It is generally good practice to avoid creating highly nonstandard behavior in widgets or interfaces with which the user is familiar. For example, it is easy to create bindings which allow an entry field to fill in reverse (so typing 123 is displayed as 321), but this is not typical entry behavior and it might be confusing to the user.

6.5.1 Bind methods

You will find more information on bind and unbind methods in “Common options” on page 425, so in this section, I will just illustrate bind methods in the context of the four binding levels.

Application level
Applications frequently use F1 to deliver help. Binding this keysym at the application level means that pressing F1, when any of the application’s windows have focus, will bring up a help screen.