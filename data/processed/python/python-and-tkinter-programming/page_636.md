---
source_image: page_636.png
page_number: 636
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.68
tokens: 8445
characters: 2535
timestamp: 2025-12-24T00:50:04.680303
finish_reason: stop
---

must arrange for these directories to be at the same relative level on the disk (for example, all in /python_source).

Next, visit www.python.org and find the latest version of Python (you will usually find a reference to the current version in the Topics panel). This should point you to the source distribution which is currently a gzipped tar file. While on this page, find out which version of Tcl/Tk was used for the binary distribution of Python. This is the version that you will need to build Tkinter. Retrieve the Python distribution and copy the file to the location you have chosen. Extract the source as follows (substitute the current version number for the bolded version).

gunzip -c py152.tgz | tar xf -

Tcl/Tk may be obtained from www.scriptics.com/products/tcltk. From this page, you will find a reference to the source distribution for the current patch level. You do not have to build Tcl/Tk if you do not want to; binary distributions of Tcl/Tk are available which include libraries that may be used to build Tkinter. It is quite likely that you will find a version later than the one used for the binary distribution of Python. Normally the patches represent bug fixes and should not cause any problems. However, do not be tempted into using the very latest release (for example, if Python was originally built with 8.0.5 and there are three later versions (8.0.6, 8.1.0 and 8.2.0 available, select 8.0.6). Retrieve the two gzipped tar files and copy them to the location you have chosen. Extract the source as follows (substitute the current version number for the bolded version).

gunzip -c tcl8.0.5.tar.gz | tar xf -
gunzip -c tk8.0.5.tar.gz | tar xf -

You must now build Tcl, Tk and Python, in that order.

Building Tcl

Change directory to the UNIX directory in the Tcl directory. In that directory you will find a ReadMe file giving complete details for building Tcl. The following is a summary of what you need to do. Of course, certain UNIX systems have special issues, so you may need to read all of the ReadMe file or consult the web.

1 Decide where the binary and library files will be installed. We will assume that the install directory is /usr/local (the default).
2 Run the configuration script. This automatically determines the compiler options and system facilities to be used by the build.
   ./configure
3 Run the make utility to create the Tcl library.
   make
4 Install the binary and library files.
   make install

Assuming that you did not encounter errors, you may go on to build Tk.