---
source_image: page_344.png
page_number: 344
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.25
tokens: 8375
characters: 1861
timestamp: 2025-12-24T00:41:05.719130
finish_reason: stop
---

installed library, the best way to correct it is to delete it from the project and then add it in again.
    Finally, select the Debug or Release configuration and then choose the Build menu option Build statistics.dll to build the dll.

14.2.5 Installing dynamic modules
To install dynamic modules, you can do one of three things. You can place the module.so or module.dll anywhere that is defined in the PYTHONPATH environment variable, you may add its path into the sys.path list at runtime, or you may copy it into the installed .../python/lib/lib-dynload directory. All three methods achieve the same effect, but I usually place *dll* files right with python.exe on Windows and I put .so files in lib-dynload for UNIX. You may make your own choice.

14.2.6 Using dynamic modules
There are no differences in the operation and use of modules that are linked statically with the interpreter and those that are linked dynamically. The only thing that you may experience is a error if you forget to put the files in the right directory or to add the path to PYTHONPATH!

Python 1.5.2b2 (#17, Apr 7 1999, 13:25:13) [C] on sunos5
Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam
>>> import statistics
>>> statistics.mavm(1.3, 5.5, 6.6, 8.8)
(1.3, 5.55, 8.8)
>>>

14.3 Using the Python API in extensions
The mavm routine in the previous example is really rather tame. Let’s change the input to a list and perform the same operations on it.

statisticsmodule2.c

#include "Python.h"

static PyObject *
stats_mavm(self, args)
    PyObject *self, *args;
{
    double total = 0.0;
    double minimum = 1E31;
    double maximum = -1E31;
    int i, len;
    PyObject *idataList = NULL;
    PyFloatObject *f = NULL;
    double df;

    if (!PyArg_ParseTuple (args, "O", &idataList)) ①
        return NULL;

    /* check first to make sure we've got a list */