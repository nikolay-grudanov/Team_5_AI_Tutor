---
source_image: page_622.png
page_number: 622
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.33
tokens: 8361
characters: 1999
timestamp: 2025-12-24T00:49:30.950872
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
    <td>vertfraction</td>
    <td>The fraction of the height of the clipper frame to scroll the interior frame when the user clicks on the vertical scrollbar arrows.</td>
    <td>distance</td>
    <td>0.05</td>
  </tr>
  <tr>
    <td>vscrollmode</td>
    <td>The vertical scroll mode. If none, the vertical scrollbar will never be displayed. If static, the scrollbar will always be displayed. If dynamic, the scrollbar will be displayed only if necessary.</td>
    <td>constant</td>
    <td>'dynamic'</td>
  </tr>
</table>

Components

borderframe
A frame widget which snugly fits around the clipper, to give the appearance of a border. It is created with a border so that the clipper, which is created without a border, looks like it has a border.

clipper
The frame which is used to provide a clipped view of the frame component. If the borderframe option is true, this is created with a borderwidth of 0 to overcome a known problem with using place to position widgets: if a widget (in this case, the frame component) is placed inside a frame (in this case the clipper component) and it extends across one of the edges of the frame, then the widget obscures the border of the frame. Therefore, if the clipper has no border, then this overlapping does not occur.

frame
The frame within the clipper to contain the widgets to be scrolled.

horizscrollbar
The horizontal scrollbar. Its component group is Scrollbar.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

vertscrollbar
The vertical scrollbar. Its component group is Scrollbar.