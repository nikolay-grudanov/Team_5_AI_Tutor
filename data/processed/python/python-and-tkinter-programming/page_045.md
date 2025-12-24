---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.81
tokens: 8435
characters: 2671
timestamp: 2025-12-24T00:32:39.786861
finish_reason: stop
---

Code comments

1 We begin by defining convenience functions to make the creation of frame and button widgets more compact. These functions use the pack geometry manager and use generally useful values for widget behavior. It is always a good idea to collect common code in compact functions (or classes, as appropriate) since this makes readability and maintenance much easier.

2 We call the Frame constructor to create the toplevel shell and an enclosing frame. Then, we set titles for the window and icon.

3 Next, we create the display at the top of the calculator and define a Tkinter variable which provides access to the widget’s contents:

    display = StringVar()
    Entry(self.master, relief=SUNKEN,
        textvariable=variable).pack(side=TOP, expand=YES,
            fill=BOTH)

4 Remember that character strings are sequences of characters in Python, so that each of the subsequences is really an array of characters over which we can iterate:

    for key in ("123", "456", "789", "-0.") :
        keyF = frame(self, TOP)
        for char in key:
            We create a frame for each row of keys.

5 We use the convenience function to create a button, passing the frame, pack option, label and callback:

    button(keyF, LEFT, char,
        lambda w=display, c=char: w.set(w.get() + c))

Don’t worry about the lambda form of the callback yet, I will cover this in more detail later. Its purpose is to define an inline function definition.

6 The = key has an alternate binding to the other buttons since it calls the calc method when the left mouse button is released:

    btn.bind('<ButtonRelease-1>',
        lambda e, s=self, w=display: s.calc(w))

7 The calc method attempts to evaluate the string contained in the display and then it replaces the contents with the calculated value or an ERROR message:

    display.set(`eval(display.get())`)

Personally, I don’t like the calculator, even though it demonstrates compact code and will be quite easy to extend to provide more complete functionality. Perhaps it is the artist in me, but it doesn’t look like a calculator!

Let’s take a look at a partly-finished example application which implements a quite sophisticated calculator. It has been left unfinished so that curious readers can experiment by adding functionality to the example (by the time you have finished reading this book, you will be ready to build a Cray Calculator!). Even though the calculator is unfinished, it can still be put to some use. As we will discover a little later, some surprising features are hidden in the reasonably short source code.

Let’s start by taking a look at some of the key features of the calculator.