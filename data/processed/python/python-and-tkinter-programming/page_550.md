---
source_image: page_550.png
page_number: 550
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.85
tokens: 8385
characters: 2204
timestamp: 2025-12-24T00:47:27.938692
finish_reason: stop
---

identify(x, y)
Returns a string indicating what part of the scale lies under the coordinates given by x and y.
A return value of SLIDER means that the point is over the slider; TROUGH1 means that the point is over the portion of the slider above or to the left of the slider; and TROUGH2 means that the point is over the portion of the slider below or to the right of the slider. If the point isn’t over one of these elements, an empty string is returned.

set(value)
This method is invoked to change the current value of the scale, and hence the position at which the slider is displayed. Value gives the new value for the scale. The method has no effect if the scale is disabled.

Scrollbar

Description
The Scrollbar class defines a new window and creates an instance of a scrollbar widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the scrollbar such as its colors, orientation, and relief. The scrollbar method returns the identity of the new widget. At the time this command is invoked, the scrollbar’s parent must exist.

A scrollbar is a widget that displays two arrows, one at each end of the scrollbar, and a slider in the middle portion of the scrollbar. It provides information about what is visible in an associated window that displays a document of some sort (such as a file being edited or a drawing). The position and size of the slider indicate which portion of the document is visible in the associated window.

For example, if the slider in a vertical scrollbar covers the top third of the area between the two arrows, it means that the associated window displays the top third of its document. Scrollbars can be used to adjust the view in the associated window by clicking or dragging with the mouse.

Inheritance
Scrollbar inherits from Widget.

Shared options

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activebackground</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>background (bg)</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>borderwidth (bd)</td>
    <td>0</td>
  </tr>
  <tr>
    <td>command</td>
    <td></td>
  </tr>
</table>