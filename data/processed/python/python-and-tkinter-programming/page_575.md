---
source_image: page_575.png
page_number: 575
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.77
tokens: 8448
characters: 2117
timestamp: 2025-12-24T00:48:13.545342
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>labelpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
  <tr>
    <td>listheight</td>
    <td>The height, in pixels, of the dropdown listbox.</td>
    <td>height</td>
    <td>150</td>
  </tr>
  <tr>
    <td>selectioncommand</td>
    <td>The function to call when an item is selected.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>Pmw:unique</td>
    <td>If both unique and history are true, the current value of the entry field is not added to the listbox if it is already in the list.</td>
    <td>boolean</td>
    <td>1</td>
  </tr>
</table>

Components

arrowbutton
In a dropdown combobox, this is the button to pop up the listbox.

entryfield
The entry field where the current selection is displayed.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelpos option is not None, this component is created as a text label for the megawidget. See the labelpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

popup
In a dropdown combobox, this is the dropdown window.

scrolledlist
The scrolled listbox which displays the items to select.

Methods

get(first = None, last = None)
This is the same as the get() method of the scrolledlist component, except that if neither first nor last are specified, the value of the entry field is returned.