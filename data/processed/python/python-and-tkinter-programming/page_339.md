---
source_image: page_339.png
page_number: 339
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.84
tokens: 8402
characters: 2464
timestamp: 2025-12-24T00:41:01.558359
finish_reason: stop
---

1 When computational demands (intensive numeric operations, for example) make Python code inefficient.
2 Where access to third-party software is required. This might be through some API (Application Program Interface) or a more complex interface.*
3 To provide access to legacy software which does not lend itself to conversion to Python.
4 To control external devices through mechanisms similar to items 2 and 3 above.

Note Writing an extension for Python means that you must have the full source for the Python interpreter and access to a C or C++ compiler (if you are going to work with Windows, I recommend that you use Microsoft’s Visual C++ version 5 or later). Unless you are going to interface a library API or have severe performance problems, you may wish to avoid building an extension altogether. See “Programming for performance” on page 348 for some ideas to improve the performance of Python code.

Let’s begin by looking at a simple example which will link a C API to Python (we will look at C++ later). For the sake of simplicity, let’s assume that the API implements several statistical functions. One of these functions is to determine the minimum, average and maximum values within four supplied real numbers. From the Python code, we are going to supply the values as discrete arguments and return the result as a tuple. Don’t worry if this sounds like a trivial task for Python–this is just a simple example!.
Here’s what we want to do from the Python side:

import statistics
....
minimum, average, maximum = statistics.mavm(1.3, 5.5, 6.6, 8.8)
....

We start by creating the file statisticsmodule.c. The accepted naming-convention for extension modules is modulemodule.c (this will be important later if we want to create dynamic loading modules).
All extension modules must include the Python API by including Python.h. This also includes several standard C-include files such as stdio.h, string.h and stdlib.h. Then we define the C functions that will support our API.
The source code will look something like this:

statisticsmodule1.c

#include "Python.h"
static PyObject *
stats_mavm(self, args)
    PyObject *self, *args;

* If you need to provide a Python interface to a library, you may wish to take a look at SWIG (See “SWIG” on page 625), which provides a very convenient way of building an interface. In some cases it is possible for SWIG to develop an interface from an include file alone. This obviously saves effort and time.