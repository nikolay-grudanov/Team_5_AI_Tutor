---
source_image: page_200.png
page_number: 200
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.34
tokens: 8364
characters: 2298
timestamp: 2025-12-24T00:36:57.360010
finish_reason: stop
---

8.5 Browsers

Browsers have become a popular motif for navigating information that is, or can be, organized as a hierarchy. Good examples of browsers include the Preferences editor in Netscape and Windows Explorer. The advantage of browsers is that branches of the typical tree display can be expanded and collapsed, resulting in an uncluttered display, even though the volume of data displayed can be quite high.

As an example, we are going to develop a simple image browser which will display all of the images in a particular directory. Tk, and therefore Tkinter, supports three image formats: GIF, PPM (truecolor), and XBM. To extend the capability of the example, we will use PIL from Secret Labs A.B. to build the images. This does not add a great deal of complexity to the example, as you will see when we examine the source code.

The browser uses several icons to represent various file types; for the purpose of this example we are using a mixture of icons created for this application. They are similar in style to those found in most current window systems.

The tree browser class is quite general and can readily be made into a base class for other browsers.

Example_8_10.py

from Tkinter import *
import Pmw
import os
import AppShell
import Image, ImageTk

path = "./icons/"
imgs = "./images/"

class Node:
    def __init__(self, master, tree, icon=None,
                 openicon=None, name=None, action=None):
        self.master, self.tree = master, tree
        self.icon = PhotoImage(file=icon)
        if openicon:
            self.openicon = PhotoImage(file=openicon)
        else:
            self.openicon = None

        self.width, self.height = 1.5*self.icon.width(), \
                                  1.5*self.icon.height()
        self.name = name
        self.var = StringVar()  # 3
        self.var.set(name)
        self.text = Entry(tree, textvariable=self.var, bg=tree.bg,
                          bd=0, width=len(name)+2, font=tree.font,
                          fg=tree.textcolor, insertwidth=1,
                          highlightthickness=1,
                          highlightbackground=tree.bg,
                          selectbackground="#044484",
                          selectborderwidth=0,
                          selectforeground='white')  # 4