---
source_image: page_348.png
page_number: 348
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.35
tokens: 8630
characters: 2690
timestamp: 2025-12-24T00:41:28.268936
finish_reason: stop
---

Table 14.1  Format strings for PyArg_ParseTuple( ) (continued)

<table>
  <tr>
    <th>Format unit</th>
    <th>Python type</th>
    <th>C type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>O&</td>
    <td>object</td>
    <td>function, variable</td>
    <td>Convert a Python object to a C variable through a converter function. This takes two arguments: the first is a function, the second is the address of a C variable (of arbitrary type), cast to void *. The converter function is called as follows: status = function(object, variable); where object is the Python object to be converted and variable is the void * argument that was passed to PyArg_ConvertTuple().<br>The returned status should be 1 for a successful conversion and 0 if the conversion has failed. If conversion fails, the function should raise an exception.</td>
  </tr>
  <tr>
    <td>S</td>
    <td>string</td>
    <td>PyStringObject *</td>
    <td>Similar to O, but it expects that the Python object is a string object. It raises a TypeError exception if the object is not a string object.</td>
  </tr>
  <tr>
    <td>(items) sequence</td>
    <td>matching items</td>
    <td></td>
    <td>The object must be a Python sequence whose length is the number of format units in items. The C arguments must correspond to the individual format units in items. Format units for sequences may be nested.</td>
  </tr>
</table>

To return values to the Python program that called the extension, we use Py_BuildValue, which uses similar format strings to PyArg_ParseTuple. Py_BuildValue has a couple of differences. First, the arguments in the call are values, not addresses. Secondly, it does not create a tuple unless there are two or more format units, or if you enclose the empty or single format unit in parentheses.

Table 14.2  Format strings for Py_BuildValue()

<table>
  <tr>
    <th>Format unit</th>
    <th>C type</th>
    <th>Python type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>s</td>
    <td>char *</td>
    <td>string</td>
    <td>Convert a null-terminated C string to a Python object. If the C string pointer is NULL, None is returned.</td>
  </tr>
  <tr>
    <td>s#</td>
    <td>char *, int</td>
    <td>string</td>
    <td>Convert a C string and its length to a Python object. If the C string pointer is NULL, the length is ignored and None is returned.</td>
  </tr>
  <tr>
    <td>z</td>
    <td>char *</td>
    <td>string or None</td>
    <td>Same as "s". If the C string pointer is NULL, None is returned.</td>
  </tr>
  <tr>
    <td>z#</td>
    <td>char *, int</td>
    <td>string or None</td>
    <td>Same as "s#". If the C string pointer is NULL, None is returned.</td>
  </tr>
</table>