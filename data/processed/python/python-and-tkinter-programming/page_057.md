---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.64
tokens: 8327
characters: 1868
timestamp: 2025-12-24T00:32:53.244312
finish_reason: stop
---

you need to look up a particular method or option, refer to appendix B. Each widget also has references to the corresponding section in the appendix.

With the exception of the first example, the code examples have been stripped of the boilerplate code necessary to import and initialize Tkinter. The constant code is shown bolded in the first example. Note that most of the examples have been coded as functions, rather than classes. This helps to keep the volume of code low. The full source code for all of the displays is available online.

4.1.1 Toplevel

The Toplevel widget provides a separate container for other widgets, such as a Frame. For simple, single-window applications, the root Toplevel created when you initialize Tk may be the only shell that you need. There are four types of toplevels shown in figure 4.1:

1 The main toplevel, which is normally referred to as the root.
2 A child toplevel, which acts independently to the root, unless the root is destroyed, in which case the child is also destroyed.
3 A transient toplevel, which is always drawn on top of its parent and is hidden if the parent is iconified or withdrawn.
4 A Toplevel which is undecorated by the window manager can be created by setting the overrideredirect flag to a nonzero value. This creates a window that cannot be resized or moved directly.

![Four windows showing different types of Toplevel widgets](https://i.imgur.com/3Q5z5QG.png)

Figure 4.1
Toplevel widgets

from Tkinter import *
root = Tk()
root.option_readfile('optionDB')
root.title('Toplevel')

Label(root, text='This is the main (default) Toplevel').pack(pady=10)
t1 = Toplevel(root)
Label(t1, text='This is a child of root').pack(padx=10, pady=10)
t2 = Toplevel(root)
Label(t2, text='This is a transient window of root').pack(padx=10, pady=10)
t2.transient(root)
t3 = Toplevel(root, borderwidth=5, bg='blue')