---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.16
tokens: 8588
characters: 3247
timestamp: 2025-12-24T00:32:40.239585
finish_reason: stop
---

and later at Sun Microsystems. Currently, Tcl/Tk is developed and supported by the Scriptics Corporation, which Ousterhout founded. Tcl/Tk enjoys a significant following with developers in a number of fields, predominantly on UNIX systems, but more recently on Win32 systems and MacOS. Ousterhout’s *Tcl and the Tk Toolkit*, which was the first Tcl/Tk book, is still a viable, though old, reference document for Tcl/Tk. (You will find some excellent newer texts on the subject in the section “References” on page 625 ).

Tcl/Tk was first designed to run under the X Window system and its widgets and windows were made to resemble Motif widgets. The behavior of bindings and controls was also designed to mimic Motif. In recent versions of Tcl/Tk (specifically, release 8.0 and after), the widgets resemble native widgets on the implemented architecture. In fact, many of the widgets *are* native widgets and the trend to add more of them will probably continue.

Like Python extensions, Tcl/Tk is implemented as a C library package with modules to support interpreted scripts, or *applications*. The Tkinter interface is implemented as a Python module, Tkinter.py, which is bound to a C-extension (_tkinter) which utilizes these same Tcl/Tk libraries. In many cases a Tkinter programmer need not be concerned with the implementation of Tcl/Tk since Tkinter can be viewed as a simple extension of Python.

**2.1.2 What about performance?**

At first glance, it is reasonable to assume that Tkinter is not going to perform well. After all, the Python interpreter is utilizing the Tkinter module which, in turn, relies on the _tkinter interface which calls Tcl and Tk libraries and sometimes calls the Tcl interpreter to bind properties to widgets. Well, this is all true, but on modern systems it really does not matter too much. If you follow the guidelines in “Programming for performance” on page 348, you will find that Python and Tkinter have the ability to deliver viable applications. If your reason for using Python/Tkinter is to develop prototypes for applications, then the point is somewhat moot; you *will* develop prototypes quickly in Python/Tkinter.

**2.1.3 How do I use Tkinter?**

Tkinter comprises a number of components. _tkinter, as mentioned before, is the low level interface to the Tk libraries and is linked into Python. Until recently, it was the programmer’s responsibility to add Tkinter to the Python build, but beginning with release 1.5.2 of Python, Tkinter, Tcl and Tk are part of the installation package—at least for the Win32 distribution. For several UNIX variants and Macintosh, it is still necessary to build Python to include Tkinter. However, check to see if a binary version is available for your particular platform.

Once a version of Python has been built and _tkinter has been included, as a shared library, dll or statically linked, the Tkinter module needs to be *imported*. This imports any other necessary modules, such as Tkconstants.

![A Tkinter window with the text 'This has to be the simplest bit of code'](../images/figure_2.1.png)

Figure 2.1 Trivial Example

To create a Tkinter window, type three lines into the Python command line (or enter them into a file and type “python filename.py”).