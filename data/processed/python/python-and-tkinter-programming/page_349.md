---
source_image: page_349.png
page_number: 349
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.80
tokens: 8792
characters: 2957
timestamp: 2025-12-24T00:41:35.899345
finish_reason: stop
---

Table 14.2  Format strings for Py_BuildValue() (continued)

<table>
  <tr>
    <th>Format unit</th>
    <th>C type</th>
    <th>Python type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>i</td>
    <td>int</td>
    <td>integer</td>
    <td>Convert a plain C int to a Python integer object.</td>
  </tr>
  <tr>
    <td>b</td>
    <td>char</td>
    <td>integer</td>
    <td>Same as i.</td>
  </tr>
  <tr>
    <td>h</td>
    <td>short int</td>
    <td>integer</td>
    <td>Same as i.</td>
  </tr>
  <tr>
    <td>l</td>
    <td>long int</td>
    <td>integer</td>
    <td>Convert a C long int to a Python integer object.</td>
  </tr>
  <tr>
    <td>c</td>
    <td>char</td>
    <td>string of length 1</td>
    <td>Convert a C int representing a character to a Python string of length 1.</td>
  </tr>
  <tr>
    <td>d</td>
    <td>double</td>
    <td>float</td>
    <td>Convert a C double to a Python floating point number.</td>
  </tr>
  <tr>
    <td>f</td>
    <td>float</td>
    <td>float</td>
    <td>Same as d.</td>
  </tr>
  <tr>
    <td>O</td>
    <td>PyObject *</td>
    <td>object</td>
    <td>Pass a Python object incrementing its reference count. If the object passed in is a NULL pointer, it is assumed that this was caused because the call producing the argument found an error and set an exception. Therefore, Py_BuildValue() will return NULL but it does not raise an exception. If no exception has been raised, PyExc_SystemError is set.</td>
  </tr>
  <tr>
    <td>S</td>
    <td>PyObject *</td>
    <td>object</td>
    <td>Same as O.</td>
  </tr>
  <tr>
    <td>N</td>
    <td>PyObject *</td>
    <td>object</td>
    <td>Similar to O, except that the reference count is not incremented.</td>
  </tr>
  <tr>
    <td>O&</td>
    <td>function, variable</td>
    <td>object</td>
    <td>Convert variable to a Python object through a converter function. The function is called with variable (which should be compatible with void *) as its argument and it should return a new Python object, or NULL if an error occurred.</td>
  </tr>
  <tr>
    <td>(items) matching items</td>
    <td></td>
    <td>tuple</td>
    <td>Convert a sequence of C values to a Python tuple with the same number of items.</td>
  </tr>
  <tr>
    <td>[items] matching items</td>
    <td></td>
    <td>list</td>
    <td>Convert a sequence of C values to a Python list with the same number of items.</td>
  </tr>
  <tr>
    <td>{items} matching items</td>
    <td></td>
    <td>dictionary</td>
    <td>Convert a sequence of C values to a Python dictionary. Each consecutive pair of C values adds one item to the dictionary, using the first value as the key and the second as the value.</td>
  </tr>
</table>

14.6 Reference counts

You may have noticed a couple of mentions of reference counts in the previous format string descriptions: If you are new to Python, and especially if you are new to extension writing and the Python API, this may be an important area to study.