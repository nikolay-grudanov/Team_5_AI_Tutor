---
source_image: page_346.png
page_number: 346
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.50
tokens: 8245
characters: 1858
timestamp: 2025-12-24T00:41:03.843939
finish_reason: stop
---

Because of the great variability of each architecture’s C++ compilers, I am not going to try to provide a cookbook to solve the various problems. However, I am going to present some code fragments that have worked for Solaris.

To get a module to compile with C++, you need to define the Python API as a C segment to the C++ compiler:

    extern "C" {
    #include "Python.h"
    }

    Then, the init function must be given the same treatment:

extern "C" {
    DL_EXPORT(void)
    initstatistics()
    {
        Py_InitModule("statistics", statistics_methods);
    }
}

14.5 *Format strings*

Format strings provide a mechanism to specify the conversion of Python types passed as arguments to the extension routines. The items in the string must match, in number and type, the addresses supplied in the PyArg_ParseTuple() call. Although the type of the arguments is checked with the format string, the supplied addresses are not checked. Consequently, errors here can have a disastrous effect on your application.

Since Python supports long integers of arbitrary length, it is possible that the values cannot be stored in c long integers; in all cases where the receiving field is too small to store the value, the most significant bits are silently truncated.

The characters |, :, and ; have special meaning in format strings.
"| " This indicates that the remaining arguments in the Python argument list are optional. The C variables corresponding to optional arguments must be initialized to their default value since PyArg_ParseTuple leaves the variables corresponding to absent arguments unchanged.
": " The list of format units ends here; the string after the colon is used as the function name in error messages.
"; " The list of format units ends here; the string after the colon is used as the error message instead of the default error message.