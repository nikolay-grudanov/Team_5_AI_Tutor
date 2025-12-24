---
source_image: page_639.png
page_number: 639
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.04
tokens: 8532
characters: 2999
timestamp: 2025-12-24T00:50:15.619628
finish_reason: stop
---

Building for Windows

Building Python and Tkinter for Windows is relatively straightforward, but it involves a little more editing work when compared to UNIX, particularly if you have additional modules to add to Python. Although it is possible to use Borland’s C compiler to build Tcl/Tk, Python requires Microsoft Visual C++ version 5 or 6.

Obtaining source distributions

Before collecting any source, decide where you are going to store the source files. You are going to have three directories (Python, Tcl and Tk) each with their revision as a suffix. You must arrange for these directories to be at the same relative level on the disk (for example, all in C:\python_source).

Next, visit www.python.org and find the latest version of Python (you will usually find a reference to the current version in the Topics panel). This should point you to the source distribution which is currently a gzipped tar file. While on this page, find out which version of Tcl/Tk was used for the binary distribution of Python. This is the version that you will need to build Tkinter. The source for the Windows (and Macintosh) distribution is identical to the UNIX distribution, although you will probably want to retrieve the zipped version. Retrieve the Python distribution and copy the file to the location you have chosen. Assuming that you have a copy of WinZip, double click on the zip file in Explorer and extract to your chosen location.

Similarly, Tcl/Tk may be obtained from www.scriptics.com/products/tcltk. From this page, you will find a reference to the source distribution for the current patch level for Windows. It is quite likely that you will find a version later than the one used for the binary distribution of Python. Normally the patches represent bug fixes and should not cause any problems. However, do not be tempted into using the very latest release (for example, if Python was originally built with 8.0.5 and there are three later versions (8.0.6, 8.1.0 and 8.2.0) available, select 8.0.6). Retrieve the two zip files and copy them to the location you have chosen. Extract the source to the chosen location using WinZip.

You must now build Tcl, Tk, and Python, in that order.

Building Tcl

Change directory to the win directory in the Tcl directory. In that directory you will find a ReadMe file giving complete details for building Tcl. The following is a summary of what you need to do.

1 Decide where the binary and library files will be installed. By default Tcl installs into C:\Program Files but there is a bug in the makefile which causes the install to fail (because of the embedded space in the directory name). It is suggested that you install into C:\Tcl.
2 Copy MakeFile.vc to MakeFile. Edit MakeFile and change the paths at the beginning of the file, as appropriate for your installation and chosen install location:

ROOT      = ..
TOOLS32   = c:\program files\devstudio\vc
TOOLS32_rc= c:\program files\devstudio\sharedide
TOOLS16   = c:\msvc
INSTALLDIR= c:\Tcl