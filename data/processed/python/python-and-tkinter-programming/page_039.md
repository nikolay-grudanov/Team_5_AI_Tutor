---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.32
tokens: 8393
characters: 2410
timestamp: 2025-12-24T00:32:30.906650
finish_reason: stop
---

from Tkinter import Label, mainloop
Label(text='This has to be the\nsimplest bit of code').pack()
mainloop()

Code comments

1 First, we import components from the Tkinter module. By using from module import Label, mainloop we avoid having to reference the module to access attributes and methods contained in the module.
2 We create a Label containing two lines of text and use the Pack geometry manager to realize the widget.
3 Finally, we call the Tkinter mainloop to process events and keep the display activated. This example does not react to any application-specific events, but we still need a mainloop for it to be displayed; basic window management is automatic.

What you will see is shown in figure 2.1. Now, it really cannot get much simpler than that!

2.1.4 Tkinter features

Tkinter adds object-oriented interfaces to Tk. Tcl/Tk is a command-oriented scripting language so the normal method of driving Tk widgets is to apply an operation to a widget identifier. In Tkinter, the widget references are objects and we drive the widgets by using object methods and their attributes. As a result, Tkinter programs are easy to read and understand, especially for C++ or Java programmers (although that is entirely another story!).

One important feature that Tk gives to any Tkinter application is that, with a little care in selecting fonts and other architecture-dependent features, it will run on numerous flavors of UNIX, Win32 and Macintosh without modification. Naturally, there are some intrinsic differences between these architectures, but Tkinter does a fine job of providing an architecture-independent graphics platform for applications.

It is the object-oriented features, however, that really distinguish Tkinter as an ideal platform for developing application frameworks. You will see many examples in this book where relatively little code will support powerful applications.

2.2 Mapping Tcl/Tk to Tkinter

Mapping of Tcl/Tk commands and arguments to Tkinter is really quite a simple process. After writing Tkinter code for a short time, it should be easy for a Tcl/Tk programmer to make the shift—maybe he will never go back to Tcl/Tk! Let’s look at some examples.

Commands in Tk map directly to class constructors in Tkinter.

<table>
  <tr>
    <th>Tcl/Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>label .myLabel</td>
    <td>myLabel = Label(master)</td>
  </tr>
</table>