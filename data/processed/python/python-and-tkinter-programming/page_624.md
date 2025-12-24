---
source_image: page_624.png
page_number: 624
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.22
tokens: 8583
characters: 2630
timestamp: 2025-12-24T00:49:52.334622
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
    <td>labelmargin</td>
    <td>If the labelfpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>labelpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelfpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
  <tr>
    <td>scrollmargin</td>
    <td>The distance between the scrollbars and the listbox widget.</td>
    <td>distance</td>
    <td>2</td>
  </tr>
  <tr>
    <td>selectioncommand</td>
    <td>This specifies a function to call when mouse button 1 is single clicked over an entry in the listbox component.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>usehullsize</td>
    <td>If true, the size of the megawidget is determined solely by the width and height options of the hull component. Otherwise, the size of the megawidget is determined by the width and height of the listbox component, along with the size and/or existence of the other components, such as the label, the scrollbars and the scrollmargin option. All of these affect the overall size of the megawidget.</td>
    <td>boolean</td>
    <td>0</td>
  </tr>
  <tr>
    <td>vscrollmode</td>
    <td>The vertical scroll mode. If none, the vertical scrollbar will never be displayed. If static, the scrollbar will always be displayed. If dynamic, the scrollbar will be displayed only if necessary.</td>
    <td>constant</td>
    <td>'dynamic'</td>
  </tr>
</table>

Components

horizscrollbar
The horizontal scrollbar. Its component group is Scrollbar.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

listbox
The listbox widget which is scrolled by the scrollbars.