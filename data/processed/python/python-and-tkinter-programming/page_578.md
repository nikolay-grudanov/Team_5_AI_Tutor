---
source_image: page_578.png
page_number: 578
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.16
tokens: 8381
characters: 2134
timestamp: 2025-12-24T00:48:19.052813
finish_reason: stop
---

Methods
This megawidget has no methods of its own. In addition, methods from the Pmw.ComboBox class are forwarded by this megawidget to the combobox component.

Counter

Description
This class consists of an entry field with arrow buttons to increment and decrement the value in the entry field. Standard counting types include numbers, times and dates. A user-defined counting function may also be supplied for specialized counting.

Counting can be used in combination with the entry field’s validation. The components may be laid out horizontally or vertically.

Each time an arrow button is pressed the value displayed in the entry field is incremented or decremented by the value of the increment option. If the new value is invalid (according to the entry field’s validate option, perhaps due to exceeding minimum or maximum limits), the old value is restored.

When an arrow button is pressed and the value displayed is not an exact multiple of the increment, it is “truncated” up or down to the nearest increment.

Inheritance
Counter inherits from Pmw.MegaWidget.

Counter options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>autorepeat</td>
    <td>If true, the counter will continue to count up or down while an arrow button is held down.</td>
    <td>boolean</td>
    <td>1</td>
  </tr>
  <tr>
    <td>buttonaspect</td>
    <td>Specifies the width of the arrow buttons as a proportion of their height. Values less than 1.0 will produce thin arrow buttons. Values greater than 1.0 will produce fat arrow buttons.</td>
    <td>float</td>
    <td>1.0</td>
  </tr>
  <tr>
    <td>datatype</td>
    <td>Specifies how the counter should count up and down. The most general way to specify the datatype option is as a dictionary. The kind of counting is specified by the counter dictionary field, which may be either a function or the name of one of the standard counters described below. *Any other fields in the dictionary are passed on to the counter function as keyword arguments.</td>
    <td>constant</td>
    <td>'numeric'</td>
  </tr>
</table>