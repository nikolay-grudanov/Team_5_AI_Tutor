---
source_image: page_576.png
page_number: 576
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.90
tokens: 8418
characters: 1956
timestamp: 2025-12-24T00:48:10.981747
finish_reason: stop
---

**invoke()**
If it’s a dropdown combobox, displays the dropdown listbox. In a simple combobox, selects the currently selected item in the listbox, calls the selectioncommand and returns the result.

**selectitem(index, setentry = 1)**
Selects the item in the listbox specified by index which may be either one of the items in the listbox or the integer index of one of the items in the listbox.

**size()**
This method is explicitly forwarded to the scrolledlist component’s size() method. Without this explicit forwarding, the size() method (aliased to grid_size()) of the hull would be invoked, which is probably not what the programmer intended.

**ComboBoxDialog**

**Description**
A ComboBoxDialog is a convenience dialog window with a simple combobox. This is used to request the user to enter a value or make a selection from the combobox list.

**Inheritance**
ComboBoxDialog inherits from Pmw.Dialog.

**ComboBoxDialog options**

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activatecommand</td>
    <td>If this is callable, it will be called whenever the megawidget is activated by a call to activate().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>borderx</td>
    <td>Specifies the width of the border to the left and right of the message area.</td>
    <td>distance</td>
    <td>10</td>
  </tr>
  <tr>
    <td>bordery</td>
    <td>Specifies the height of the border to the top and bottom of the message area.</td>
    <td>distance</td>
    <td>10</td>
  </tr>
  <tr>
    <td>buttonboxpos</td>
    <td>Specifies on which side of the dialog window to place the button box. Must be one of N, S, E or W.</td>
    <td>anchor</td>
    <td>S</td>
  </tr>
  <tr>
    <td>buttons</td>
    <td>This must be a tuple or a list. It specifies the names on the buttons in the button box.</td>
    <td>(string, ('OK', ...)</td>
    <td></td>
  </tr>
</table>