---
source_image: page_340.png
page_number: 340
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.57
tokens: 8305
characters: 1753
timestamp: 2025-12-24T00:40:55.308132
finish_reason: stop
---

{
    double value[4], total;
    double minimum = 1E32;
    double maximum = -1E32;
    int i;

    if (!PyArg_ParseTuple (args, "dddd", &value[0], &value[1],
                           &value[2], &value[3]))
        return NULL;

    for (i=0; i<4; i++)
    {
        if (value[i] < minimum)
            minimum = value[i];
        if (value[i] > maximum)
            maximum = value[i];
        total = total + value[i];
    }

    return Py_BuildValue("(ddd)", minimum, total/4, maximum) ;
}

static PyMethodDef statistics_methods[] = {
    {"mavm",     stats_mavm, METH_VARARGS,   "Min, Avg, Max"},
    {NULL, NULL} };
DL_EXPORT(void)
initstatistics()
{
    Py_InitModule("statistics", statistics_methods);
}

Code comments

1 As mentioned earlier, all extension modules must include the Python API definitions.
2 All interface items are Python objects, so we define the function to return a PyObject.
3 Similarly, the instance and arguments, args, are PyObject.
4 The Python API provides a function to parse the arguments, converting Python objects into C entities:
if (!PyArg_ParseTuple (args, "dddd", &value[0], &value[1],
                       &value[2], &value[3]))
    return NULL;
    PyArg_ParseTuple parses the args object using the supplied format string. The available options are explained in “Format strings” on page 321. Note that you must supply the address of the variables into which parsed values are to be placed.
5 Here we process our data. As you will note, this is really difficult!
6 In a manner similar to PyArg_ParseTuple, Py_BuildValue creates Python objects from C entities. The formats have the same meaning.
return Py_BuildValue("(ddd)", minimum, total/4, maximum)
In this case, we create a tuple as our return object.