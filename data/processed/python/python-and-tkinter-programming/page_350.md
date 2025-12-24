---
source_image: page_350.png
page_number: 350
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.10
tokens: 8437
characters: 2908
timestamp: 2025-12-24T00:41:22.526285
finish_reason: stop
---

The Python documentation for extensions and the API provides an excellent picture of what is entailed, and you want to see a full explanation, I recommend that you study the Python documentation.

Most API functions have a return value of type PyObject *. This is a pointer to an arbitrary Python object. All Python objects have similar base behavior and may be represented by a single C type. You cannot declare a variable of type PyObject; you can only declare PyObject * pointers to the actual storage. All PyObjects have a reference count.

This is where we need to take special care! When an object’s reference count becomes zero, it will be deconstructed. If the object contains references to other objects, then their reference counts are decremented. If their reference count becomes zero, then they too will be deconstructed.

Problems usually occur when the interface extracts an object from a list and then uses that reference for a while (or worse, passes the reference back to the caller). In a similar fashion, a Py_DECREF() call before passing data to the caller will result in disaster.

The Python documentation recommends that extensions use the API functions that have a PyObject, PyNumber, PySequence or PyMapping prefix, since these operations always increment the reference count. It is the caller’s responsibility to call Py_DECREF() when no further reference is required.

Here’s a general rule of thumb: If you are writing a Python extension and you repeatedly get a crash when you either return a value or exit your application, you’ve got the reference counts wrong.

14.7 Embedding Python

When it is necessary to add Python functionality to a C or C++ application, it is possible to embed the Python interpreter. This can be invaluable if you need to create Python objects within a C program or, perhaps, use dictionaries as a data structure. It is also possible to combine extending and embedding within the same application.

The Python documentation provides full documentation for the API, and you should reference this material for details. All you need to use the API is to call Py_Initialize() once from your application before using API calls.

Once the interpreter has been initialized, you may execute Python strings using PyRun_SimpleString() or you may execute complete files with PyRun_SimpleFile(). Alternatively, you can use the Python API to exercise precise control over the interpreter.

Here is a simple example that illustrates a way that Python functionality may be accessed from C. We will access a dictionary created using a simple Python script from C. This provides a powerful mechanism for C programs to perform hashed lookups of data without the need to implement specific code. Most of the code runs entirely in C code, which means that performance is good.

dictionary.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Python.h"