---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.58
tokens: 8398
characters: 2445
timestamp: 2025-12-24T00:41:09.866497
finish_reason: stop
---

if (!PyList_Check(idataList))
{
    PyErr_SetString(PyExc_TypeError,
        "input argument must be a list");
    return NULL;
}
len = PyList_Size(idataList);
for (i=0; i<len; i++)
{
    f = (PyFloatObject *)PyList_GetItem(idataList, i);
    df = PyFloat_AsDouble(f);
    if (df < minimum)
        minimum = df;
#---------------------------------------------Remaining code removed-----------------

Code comments

1 We need to define a Python object for the list that is being passed in as an argument and a PyFloatObject (a subtype of PyObject) to receive the items in the list.
2 We are now receiving a single object (as opposed to discrete values in the previous example).
3 We check that the object is indeed a list. This actually introduces a shortcoming—we cannot pass a tuple containing the values. If there is an error, we use PyErr_SetString to generate PyExc_TypeError with a specific error message.
4 List objects have a length attribute, so we get it.
5 We get each item in the list.
6 For each item we convert the PyFloat to a C double. The rest of the code has been removed; you have seen it before.

This example only scratches the surface of what can be done with the Python API. A good place to find examples of its use is in the Modules directory in the Python source. One reason that this topic is important is that Python is very good at creating and manipulating strings, especially if they involve lists, tuples, or dictionaries. A very realistic scenario is the ability to use Python to create such data structures and then to use use C to further process the entries, using API calls inside an iterator. In this way, C can provide the speed for critical operations and Python can provide the power to handle data succinctly.

14.4 Building extensions in C++

Python is a C-based interpreter. Although it’s possible to adjust the source so that it would compile as C++, it would be a large undertaking. This means that calling C++ functions from this C base introduces some special problems. However, if you are able to link Python with the C++ compiler (linker), the problems are reduced.

Clearly, many C++ class libraries can support Python systems. The trick is to leave Python essentially unchanged and provide a wrapper which gives access to the class library. If you can use dynamic linking for extension modules, this is quite a painless experience. If you must link statically, you may be facing some challenges.