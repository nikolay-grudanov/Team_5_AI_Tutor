---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.10
tokens: 8813
characters: 2951
timestamp: 2025-12-24T00:41:35.517941
finish_reason: stop
---

Table 14.1  Format strings for PyArg_ParseTuple( )

<table>
  <tr>
    <th>Format unit</th>
    <th>Python type</th>
    <th>C type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>s</td>
    <td>string</td>
    <td>char *</td>
    <td>Convert a Python string to a C pointer to a character string. The address you pass must be a character pointer; you do not supply storage. The C string is null-terminated. The Python string may not contain embedded nulls and it cannot be None. If it does or is, a TypeError exception is raised.</td>
  </tr>
  <tr>
    <td>s#</td>
    <td>string</td>
    <td>char *, int</td>
    <td>Stores into two C variables, the first one being a pointer to a character string, the second one being its length. The Python string may have embedded nulls.</td>
  </tr>
  <tr>
    <td>z</td>
    <td>string or None</td>
    <td>char *</td>
    <td>Similar to s, but the Python object may also be None, in which case the C pointer is set to NULL.</td>
  </tr>
  <tr>
    <td>z#</td>
    <td>string or None</td>
    <td>char *, int</td>
    <td>Similar to s#.</td>
  </tr>
  <tr>
    <td>b</td>
    <td>integer</td>
    <td>char</td>
    <td>Convert a Python integer to a tiny int, stored in a C char.</td>
  </tr>
  <tr>
    <td>h</td>
    <td>integer</td>
    <td>short int</td>
    <td>Convert a Python integer to a C short int.</td>
  </tr>
  <tr>
    <td>i</td>
    <td>integer</td>
    <td>int</td>
    <td>Convert a Python integer to a plain C int.</td>
  </tr>
  <tr>
    <td>l</td>
    <td>integer</td>
    <td>long int</td>
    <td>Convert a Python integer to a C long int.</td>
  </tr>
  <tr>
    <td>c</td>
    <td>string of length 1</td>
    <td>char</td>
    <td>Convert a Python character, represented as a string of length 1, to a C char.</td>
  </tr>
  <tr>
    <td>f</td>
    <td>float</td>
    <td>float</td>
    <td>Convert a Python floating point number to a C float.</td>
  </tr>
  <tr>
    <td>d</td>
    <td>float</td>
    <td>double</td>
    <td>Convert a Python floating point number to a C double.</td>
  </tr>
  <tr>
    <td>D</td>
    <td>complex</td>
    <td>Py_complex</td>
    <td>Convert a Python complex number to a C Py_complex structure.</td>
  </tr>
  <tr>
    <td>O</td>
    <td>object</td>
    <td>PyObject *</td>
    <td>Store a Python object (without conversion) in a C object pointer. The C interface receives the actual object that was passed. The object's reference count is not increased.</td>
  </tr>
  <tr>
    <td>O!</td>
    <td>object</td>
    <td>typeobject, PyObject *</td>
    <td>Store a Python object in a C object pointer. This is similar to O, but it takes two C arguments: the first is the address of a Python-type object specifying the required type, and the second is the address of the C variable (of type PyObject *) into which the object pointer is stored. If the Python object does not have the required type, a TypeError exception is raised.</td>
  </tr>
</table>