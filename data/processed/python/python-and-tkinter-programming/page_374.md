---
source_image: page_374.png
page_number: 374
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.57
tokens: 8308
characters: 2021
timestamp: 2025-12-24T00:41:55.645557
finish_reason: stop
---

17.1.1 Program organization

You can do a number of things to make sure that your application performs well. Let’s start with how you organize your code. Regardless of how you start your application and whether it is intended to run on UNIX, Win32 or MacOS, you need to make sure that the first bit of Python code is short. If you invoke the Python interpreter (on UNIX) using:

    #! /usr/bin/env python

as the first line of a script on UNIX, all of the subsequent lines will be parsed and compiled every time you run your application. Although the script is translated to bytecode, no bytecode (.pyc or .pyo) file will be created. This means that you have to go through the parser each time you invoke your program. So, you must construct your application so that you parse the minimum number of Python statements each time you invoke the application. Let’s suppose you have constructed your application to have a structure something like this:

from Tkinter import *
from tkSimpleDialog import Dialog
import tkMessageBox
import Pmw

class MyClass(Dialog):
    def body(self, master):
        ...

def amethod(self):
    ...

root = Tk()
instance = MyClass(root)

Sure, there aren’t too many lines of code here, but your application might have thousands of lines. So, let’s name the module myApplicationReal.py and change the last two lines to look like this:

def myApplicationReal():
    root = Tk()
    instance = MyClass(root)

Then, create a short Python script called myApplication, and insert the following lines:

#! /usr/bin/env python
import myApplicationReal
myApplicationReal.myApplicationReal()

This will use either myApplicationReal.pyc or myApplicationReal.pyo if they exist, or it will create them if they do not. This guarantees an improvement in start-up time for any large application. Incidentally, you can use the same file for Win32 also. If you construct a batch file called myApp.bat that contains the following lines, you can use the same module for UNIX and Win32:

    python myApplication