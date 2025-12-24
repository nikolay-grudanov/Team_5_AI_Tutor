---
source_image: page_401.png
page_number: 401
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.67
tokens: 8363
characters: 2266
timestamp: 2025-12-24T00:42:45.191463
finish_reason: stop
---

paths to .../Python/Lib and wherever MyApplication.py is installed. You may not want to modify the user’s environment, but you can do that within your script:

    #!/usr/bin/env python

    import sys
    sys.path.insert(0, '/opt/yourapp/lib')

    import myapplication
    myapplication.main()

    Clearly some refinements can be made, but this scheme works well in practice.

19.3 *Distributing Win32 applications*

I think that this is much more problematic when compared to the UNIX case. You have several alternatives. I will advocate the simplest case, since the others do require interaction with the registry, which really implies that you will use an installation tool such as InstallShield, which automates the process of installing and registering the application components. More important, it perhaps makes provisions to install an *uninstaller* which removes the registry information and the installed files, usually without user intervention.

The decisions that have to be made for Win32 are similar to those for UNIX. The need to use a minimal script to get the application running is still present. The real problem is that Win32 will open an MS-DOS window when launching a Python script from a clickable file. With a little bit of encouragement, this can be avoided.

First, let’s decide how we are going to package the application. For this example we will make a freestanding Win32 application, with everything that we need to support our application installed in a single directory (which can be called anything we wish). We are *not* going to make modifications to the registry and we want a single icon on the desktop which the user double-clicks to start the application.

Let’s first take a look at the contents of the top-level directory, which is shown in figure 19.1. In this directory we have installed the Python executables (python.exe and pythonw.exe), the system dll files (_tkinter.pyd, python15.dll, tcl80.dll and tk80.dll) and the application-specific dll files (such as btrieve.dll and sio.pyd). We also have the standard Python’s Lib directory, which contains Pmw* (and might contain application-specific files).

* Pmw is not part of the standard Python distribution. You must download Pmw from http://www.dscpl.com.au/pmw/.