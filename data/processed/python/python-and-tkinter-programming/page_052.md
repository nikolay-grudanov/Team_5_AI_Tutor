---
source_image: page_052.png
page_number: 52
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.48
tokens: 8270
characters: 1976
timestamp: 2025-12-24T00:32:45.975948
finish_reason: stop
---

Because we are maintaining a local namespace, it is possible to set up an interactive Python session that can do some useful work. Figure 3.5 shows how we are able to set variables within the namespace and manipulate the data with built-ins.

Figure 3.5 Variables and built-in functions

Figure 3.6 is yet another example of our ability to gain access to the interpreter from an interactive shell. While the examples have been restricted to operations that fit within the limited space of the calculator’s display, they do illustrate a potential for more serious applications. Note how Python allows you to create and use variables within the current namespace.

Figure 3.6 Using the math module

Note When developing applications, I generally hide a button or bind a “secret” key sequence to invoke a GUI which allows me to execute arbitrary Python so that I can examine the namespace or modify objects within the running system. It is really a miniature debugger that I always have access to during development when something unusual happens. Sometimes restarting the application for a debug session just does not get me to the solution. An example of one of these tools is found in “A Tkinter explorer” on page 334.

3.3 Examining the application structure

The calculator example derives its compact code from the fact that Tkinter provides much of the structure for the application. Importing Tkinter establishes the base objects for the system and it only requires a little extra code to display a GUI. In fact, the minimal Tkinter code that can be written is just four lines:

from Tkinter import *
aWidget = Label(None, text='How little code does it need?')
aWidget.pack()
aWidget.mainloop()

In this fragment, the label widget is realized with the pack method. A mainloop is necessary to start the Tkinter event loop. In our calculator example, the application structure is a little more complex:

from Tkinter import *
...
define helper classes
...
class Calculator: