---
source_image: page_640.png
page_number: 640
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.52
tokens: 8312
characters: 1845
timestamp: 2025-12-24T00:50:02.308830
finish_reason: stop
---

3 In an MS-DOS window, run the nmake utility to create the Tcl library.
    nmake
4 Install the binary and library files.
    nmake install

Assuming that you did not encounter errors, you may go on to build Tk.

Building Tk

Building Tk is similar to building Tcl. Change directory to the win directory in the Tk directory. In that directory you will find a ReadMe file giving complete details for building Tk. The following is a summary of what you need to do.

1 You should install Tk into the same directory structure as a peer of Tcl.
2 Copy MakeFile.vc to MakeFile. Edit MakeFile and change the paths at the beginning of the file, as appropriate for your installation and chosen install location:
    ROOT      = ..
    TOOLS32   = c:\program files\devstudio\vc
    TOOLS32_rc= c:\program files\devstudio\sharedide
    TCLDIR    = ..\..\tcl8.0.5
    INSTALLDIR= c:\tcl
3 Run the nmake utility to create the Tk library.
    nmake
4 Install the binary and library files.
    nmake install

We are now ready to build Python.

Building Python

The current distribution of Python requires you to build with Microsoft Visual C++ 5.x (or 6.x). Once Tcl/Tk has been built, it is quite easy to complete the build.

1 In Explorer, navigate to the PCbuild directory.
2 Open the workspace pcbuild.dsw.
3 Select the Debug or Release setting (using Set Active Configuration... in the Build menu).
4 Select python15 from Select Active Project in the Project menu.
5 Select Build python_15.dll from the Build menu.
6 Select python from Select Active Project in the Project menu.
7 Select Build python.exe from the Build menu.
8 Select pythonw from Select Active Project in the Project menu.
9 Select Build pythonw.exe from the Build menu.
10 Select _tkinter from Select Active Project in the Project menu.
11 Select Build _tkinter.pyd from the Build menu.