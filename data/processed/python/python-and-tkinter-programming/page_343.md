---
source_image: page_343.png
page_number: 343
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.57
tokens: 8389
characters: 2256
timestamp: 2025-12-24T00:41:05.868951
finish_reason: stop
---

makefile_dyn

SRCS=        statisticsmodule.c
CFLAGS=      -DHAVE_CONFIG_H
C=           cc

# Symbols used for using shared libraries
SO=          .so
LDSHARED=    ld -G

OJBS=        statisticsmodule.o
PYTHON_INCLUDE=   -I/usr/local/include/python1.5 \
                  -I/usr/local/lib/python1.5/config
statistics:  $(OJBS)
             $(LDSHARED) $(OJBS)
             -Bdynamic -o statisticsmodule.so

statisticsmodule.o:    statisticsmodule.c
             $(C) -c $(CFLAGS) $(PYTHON_INCLUDE) \
             statisticsmodule.c

Code comments

① CFLAGS defines HAVE_CONFIG_H (among other things, this defines the mode of dynamic loading). Not all architectures need this, but define it anyway.
② LDSHARED defines the ld command line needed to generate shared libraries. This will vary with different architectures.
③ PYTHON_INCLUDE defines the path for Python.h and the installed config.h.
④ The target for the link might need libraries to be supplied for more complex modules. The -lxxx flags would be placed right after the $(OJBS).
⑤ The compile rule is quite simple; just add the CFLAGS and PYTHON_INCLUDE variables.

14.2.4 Building a dynamic module in Windows

Once again, building a dynamic module in Windows is quite involved. It does require you to edit some files which contain comments such as DO NOT EDIT, but despite that, it works! As with static linking, build and install Python first so that libraries and other such items are in place.

First, create a directory in the top-level Python directory, at the same level as Modules, Parser and so on. Give it the same name as your module.

Next, copy all of the files necessary to support your module into this directory; for our example, we need only statisticsmodule.c.

Then, in the PC directory of the standard Python distribution, you will find a directory called example_nt. Copy example.def, example.dsp, example.dsw and example.mak into the module directory, renaming the files with your module name as the prefix.

Edit each of these files, changing the references to example to your module name. You will need to make over 50 changes to the make file. As you make the changes, note the paths to the Python library (which is python15.lib in this case). If this does not match your