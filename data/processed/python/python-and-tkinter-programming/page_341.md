---
source_image: page_341.png
page_number: 341
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.24
tokens: 8361
characters: 2314
timestamp: 2025-12-24T00:41:00.152112
finish_reason: stop
---

7 All interface modules must define a methods table, whose function is to associate Python function names with their equivalent C functions

static PyMethodDef statistics_methods[] = {
    {"mavm",     stats_mavm, METH_VARARGS,   "Min, Avg, Max"},
    {NULL, NULL} };
METH_VARARGS defines how the arguments are to be presented to the parser. The documentation field is optional. Notice the naming convention for the methods table. Although this can take any name, it is usually a good idea to follow the convention.

8 The methods table must be registered with the interpreter in an initialization function. When the module is first imported, the initstatistics() function is called.

DL_EXPORT(void) initstatistics()
{
    Py_InitModule("statistics", statistics_methods);
}

Again, the naming convention must be followed, because Python will attempt to call initmodulename for each module imported.

14.2 Building Python extensions

Before you can use the Python extension, you have to compile and link it. Here, you have several choices, depending on whether the target system is UNIX or Windows (sorry, I am not covering Macintosh extensions).

Basically, we can make the module a permanent part of the Python interpreter so that it is always available, or we can link it dynamically. Dynamic linking is not available on all systems, but it works well for many UNIX systems and for Windows. The advantage to loading dynamically is that you do not need to modify the interpreter to extend Python.

14.2.1 Linking an extension statically in UNIX

Linking an extension statically in UNIX is quite simple to do. If you have not already configured and built Python, do so as described in “Building and installing Python, Tkinter” on page 610. Copy your module (in this case, statisticsmodule.c) to the Modules directory. Then, add on line at the end of Modules/Setup.local (you may add some comments, too, if you wish):

*static*
statistics statisticsmodule.c

If your module requires additional libraries, such as an API, add -lxxx flags at the end of the line. Note that the *static* flag is really only required if the preceding modules have been built as shared modules by including the *shared* flag.

Now, simply invoke make in the top-level Python directory to rebuild the python executable in that directory.