---
source_image: page_638.png
page_number: 638
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.88
tokens: 8420
characters: 2066
timestamp: 2025-12-24T00:50:05.147327
finish_reason: stop
---

# lines and remove the backslashes -- the backslash interpretation is
# done by the shell's "read" command and it may not be implemented on
# every system.

# *** Always uncomment this (leave the leading underscore in!):
_tkinter _tkinter.c tkappinit.c -DWITH_APPINIT \
# *** Uncomment and edit to reflect where your Tcl/Tk headers are:
-I/usr/local/include \
# *** Uncomment and edit to reflect where your X11 header files are:
# -I/usr/X11R6/include \
# *** Or uncomment this for Solaris:
-I/usr/openwin/include \
# *** Uncomment and edit for Tix extension only:
# -DWITH_TIX -ltix4.1.8.0 \
# *** Uncomment and edit for BLT extension only:
# -DWITH_BLT -I/usr/local/blt/blt8.0-unoff/include -lBLT8.0 \
# *** Uncomment and edit for PIL (TkImaging) extension only:
# -DWITH_PIL -I../Extensions/Imaging/libImaging tkImaging.c \
# *** Uncomment and edit for TOGL extension only:
# -DWITH_TOGL togl.c \
# *** Uncomment and edit to reflect where your Tcl/Tk libraries are:
-L/usr/local/lib \
# *** Uncomment and edit to reflect your Tcl/Tk versions:
-ltk8.0 -ltcl8.0 \
# *** Uncomment and edit to reflect where your X11 libraries are:
# -L/usr/X11R6/lib \
# *** Or uncomment this for Solaris:
-L/usr/openwin/lib \
# *** Uncomment these for TOGL extension only:
# -lGL -lGLU -lXext -lXmu \
# *** Uncomment for AIX:
# -lld \
# *** Always uncomment this; X11 libraries to link with:
-lX11

6 If you wish to build modules as shared objects, uncomment the line which contains *shared*. All subsequent modules will be built as separate shared objects.
7 Save Modules/Setup. You may wish to save a copy of Modules/Setup so that you will be able to identify your chosen configuration in later versions of Python.
8 Run the make utility to create the Python executable and library.
    make
9 Install the binary and library files.
    make install
10 Define environment variables to reflect your chosen installation locations:
    PATH= .....:/usr/local/bin:.......
    PYTHONPATH=/usr/local/lib/python1.5
    TCL_LIBRARY=/usr/local/lib/tcl8.0
    TK_LIBRARY=/usr/local/lib/tk8.0