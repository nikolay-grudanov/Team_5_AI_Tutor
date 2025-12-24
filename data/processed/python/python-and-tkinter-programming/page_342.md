---
source_image: page_342.png
page_number: 342
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.75
tokens: 8313
characters: 1851
timestamp: 2025-12-24T00:40:55.682106
finish_reason: stop
---

14.2.2 Linking an extension statically in Windows

Linking an extension statically in Windows is a little more involved than the case for UNIX, but it is quite easy if you follow the steps. If you have not yet built Python, do so as described in “Building and installing Python, Tkinter” on page 610.

First, edit PC/config.c. You will find a comment:

/* -- ADDMODULE MARKER 1 -- */
extern void PyMarshal_Init();
extern void initimp();
extern void initstatistics();
extern void initwprint();

Add an extern reference for the init function. Then locate the second comment:

/* -- ADDMODULE MARKER 2 -- */
    /* This module "lives in" with marshal.c */
    {"marshal", PyMarshal_Init},
    /* This lives it with import.c */
    {"imp", initimp},
    /* Statistics module (P-Tk-P) */
    {"statistics", initstatistics},
    /* Window Print module */
    {"wprint", initwprint},

Add the module name and its init function.
Next, edit PC/python15.dsp. Near the end you should find an entry for typeobject.c:

SOURCE=..\Objects\typeobject.c
# End Source File
#
# Begin Source File
SOURCE=..\Modules\statisticsmodule.c
# End Source File
#
# Begin Source File
SOURCE=..\Modules\wprintmodule.c
# End Source File

Insert the lines for statisticsmodule.c.
Lastly, open the workspace PCbuild/pcbuild.dsw in VC++, select the appropriate configuration (see “Building and installing Python, Tkinter” on page 610) and build the projects.

14.2.3 Building a dynamic module in UNIX

There are several styles of generating dynamically-loadable modules. I’m just going to present a method that works for Solaris, but all UNIX systems derived from SVR4 should provide similar interfaces. All the work is done in the makefile, so no code changes should be needed. As with static linking, build and install Python first so that libraries and other such items are in place.