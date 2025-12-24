---
source_image: page_637.png
page_number: 637
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.74
tokens: 8409
characters: 2527
timestamp: 2025-12-24T00:50:04.888523
finish_reason: stop
---

Building Tk

Building Tk is similar to building Tcl. Change directory to the UNIX directory in the Tk directory. In that directory you will find a ReadMe file giving complete details for building Tk. The following is a summary of what you need to do.

1 You should install Tk into the same directory structure as Tcl. If you did change from the default /usr/local then you should use the same path for the configure script.
2 Run the configuration script. This automatically determines the compiler options and system facilities to be used by the build.
    ./configure
3 Run the make utility to create the Tk library.
    make
4 Install the binary and library files.
    make install

We are now ready to build Python.

Building Python

Building Python is quite similar to building Tcl or Tk. A little more work is required to configure the build to add Tkinter, which is not built by default. You’ll find a ReadMe file at the top-level Python directory which gives full details and explains differences between different variants of UNIX. Once again, the following is a summary.

1 We will assume again that the install directory is /usr/local (the default). It does not have to be the same as the Tcl/Tk installation directory, but there is little reason to use a different location.
2 Run the configuration script. This automatically determines the compiler options and system facilities to be used by the build. Note that if you intend to use threading, you will have to add the --with-thread option to configure. Read the ReadMe file for further details and information about platform-specific issues.
    ./configure
3 Copy Modules/Setup.in to Modules/Setup. This file is used to determine which built-in modules will be added to Python. For the moment, we are concerned only with adding Tkinter. You will find many platform-specific modules that may be added or removed from the build.
4 Edit Modules/Setup and locate the line commented as:
    # The _tkinter module.
5 Follow the instructions in the file. The example shown here is appropriate for Solaris 2.5 or 2.6 (the bold sections should not be commented):

# The TKPATH variable is always enabled, to save you the effort.
TKPATH=:lib-tk
# The command for _tkinter is long and site-specific. Please
# uncomment and/or edit those parts as indicated. If you don't have a
# specific extension (e.g. Tix or BLT), leave the corresponding line
# commented out. (Leave the trailing backslashes in! If you
# experience strange errors, you may want to join all uncommented