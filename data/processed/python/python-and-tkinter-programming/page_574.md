---
source_image: page_574.png
page_number: 574
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.58
tokens: 8445
characters: 2061
timestamp: 2025-12-24T00:48:11.226353
finish_reason: stop
---

will be no default button. index may have any of the forms accepted by the index() method.

ComboBox

Description
This class creates an entry field and an associated scrolled listbox. When an item in the listbox is selected, it is displayed in the entry field. Optionally, the user may also edit the entry field directly.
For a simple combobox, the scrolled listbox is displayed beneath the entry field. For a dropdown combobox (the default), the scrolled listbox is displayed in a window which pops up beneath the entry field when the user clicks on an arrow button on the right of the entry field. Either style allows an optional label.

Inheritance
ComboBox inherits from Pmw.MegaWidget.

ComboBox options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>autoclear</td>
    <td>If both autoclear and history are true, clear the entry field whenever RETURN is pressed, after adding the value to the history list.</td>
    <td>boolean</td>
    <td>0</td>
  </tr>
  <tr>
    <td>buttonaspect</td>
    <td>The width of the arrow button as a proportion of the height. The height of the arrow button is set to the height of the entry widget.</td>
    <td>float</td>
    <td>1.0</td>
  </tr>
  <tr>
    <td>dropdown</td>
    <td>Specifies whether the combobox megawidget should be dropdown or simple.</td>
    <td>boolean</td>
    <td>1</td>
  </tr>
  <tr>
    <td>fliparrow</td>
    <td>If true, the arrow button is drawn upside down when the listbox is being displayed. Used only in dropdown megawidgets.</td>
    <td>boolean</td>
    <td>0</td>
  </tr>
  <tr>
    <td>history</td>
    <td>When RETURN is pressed in the entry field, the current value of the entry field is appended to the listbox if history is true.</td>
    <td>boolean</td>
    <td>1</td>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labelpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
</table>