---
source_image: page_618.png
page_number: 618
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.25
tokens: 8298
characters: 1836
timestamp: 2025-12-24T00:49:25.505593
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
    <td>vscrollmode</td>
    <td>The vertical scroll mode. If none, the vertical scrollbar will never be displayed. If static, the scrollbar will always be displayed. If dynamic, the scrollbar will be displayed only if necessary.</td>
    <td>constant</td>
    <td>'dynamic'</td>
  </tr>
</table>

Components

borderframe
A frame widget which snugly fits around the canvas, to give the appearance of a canvas border. It is created with a border so that the canvas, which is created without a border, looks like it has a border.

canvas
The canvas widget which is scrolled by the scrollbars. If the borderframe option is true, this is created with a borderwidth of 0 to overcome a known problem with canvas widgets—if a widget inside a canvas extends across one of the edges of the canvas, then the widget obscures the border of the canvas. Therefore, if the canvas has no border, then this overlapping does not occur.

horizscrollbar
The horizontal scrollbar. Its component group is Scrollbar.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

vertscrollbar
The vertical scrollbar. Its component group is Scrollbar.

Methods

bbox(* args)
This method is explicitly forwarded to the canvas component’s bbox() method. Without this explicit forwarding, the bbox() method (aliased to grid_bbox()) of the hull would be invoked, which is probably not what the programmer intended.