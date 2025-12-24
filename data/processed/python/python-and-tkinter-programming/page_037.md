---
source_image: page_037.png
page_number: 37
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.06
tokens: 8148
characters: 1164
timestamp: 2025-12-24T00:32:13.746061
finish_reason: stop
---

CHAPTER 2

Tkinter

2.1 The Tkinter module 12
2.2 Mapping Tcl/Tk to Tkinter 14
2.3 Win32 and Unix GUIs 15
2.4 Tkinter class hierarchy 16
2.5 Tkinter widget appearance 17

This chapter describes the structure of the Tkinter module and its relationship to Tcl/Tk. The mapping with Tcl/Tk constructs to Tkinter is explained in order to assist Tcl/Tk programmers in converting to Tkinter from Tcl/Tk. Native GUIs for UNIX, Win32 and Macintosh implementations will be discussed and key architectural differences will be highlighted. Font and color selection will be introduced, and I’ll cover this topic in more detail in “Tkinter widgets” on page 31. For readers who are unfamiliar with Tkinter, this chapter illustrates its importance to Python applications.

2.1 The Tkinter module

2.1.1 What is Tkinter?

Tkinter provides Python applications with an easy-to-program user interface. Tkinter supports a collection of Tk widgets that support most application needs. Tkinter is the Python interface to Tk, the GUI toolkit for Tcl/Tk. Tcl/Tk is the scripting and graphics facility developed by John Ousterhout, who was originally at University of California at Berkeley