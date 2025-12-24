---
source_image: page_590.png
page_number: 590
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.32
tokens: 8154
characters: 1158
timestamp: 2025-12-24T00:48:32.356512
finish_reason: stop
---

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

ring
This component acts as the enclosing ring around the groupchildsite. The default border-width is 2 and the default relief is groove.

tag
The identifying tag displayed over the top edge of the enclosing ring. If this is None, no tag is displayed.

Methods

interior()
Returns the frame within which the programmer may create widgets. This is the same as component('groupchildsite').

LabeledWidget

Description
This megawidget consists of an interior frame with an associated label which can be positioned on any side of the frame. The programmer can create other widgets within the interior frame.

Inheritance
LabeledWidget inherits from Pmw.MegaWidget.

LabeledWidget options

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
</table>