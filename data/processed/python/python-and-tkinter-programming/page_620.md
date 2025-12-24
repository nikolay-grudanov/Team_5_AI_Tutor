---
source_image: page_620.png
page_number: 620
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.96
tokens: 8219
characters: 1453
timestamp: 2025-12-24T00:49:20.604230
finish_reason: stop
---

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

Methods
This megawidget has no methods of its own.

ScrolledFrame

Description
This megawidget consists of a scrollable interior frame within a clipping frame. The programmer can create other widgets within the interior frame. If the frame becomes larger than the surrounding clipping frame, the user can position the frame using the horizontal and vertical scrollbars.
    The scrollbars can be dynamic, which means that a scrollbar will only be displayed if it is necessary—if the frame is smaller than the surrounding clipping frame, the scrollbar will be hidden.

Inheritance
ScrolledFrame inherits from Pmw.MegaWidget.

ScrolledFrame options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>borderframe</td>
    <td>A frame widget which snugly fits around the clipper, to give the appearance of a border. It is created with a border so that the clipper, which is created without a border, looks like it has a border.</td>
    <td>widget</td>
    <td>Frame</td>
  </tr>
</table>