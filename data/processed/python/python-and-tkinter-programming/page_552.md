---
source_image: page_552.png
page_number: 552
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.17
tokens: 8500
characters: 2635
timestamp: 2025-12-24T00:47:36.484101
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>repeatinterval</td>
    <td>Used in conjunction with repeatDelay: once auto-repeat begins, this option determines the number of milliseconds between auto repeats.</td>
    <td>integer</td>
    <td>100</td>
    <td>100</td>
  </tr>
  <tr>
    <td>troughcolor</td>
    <td>Specifies the color to use for the rectangular trough areas in widgets such as scrollbars and scales.</td>
    <td>color</td>
    <td>'gray40'</td>
    <td>System-Scroll-bar</td>
  </tr>
</table>

Methods

activate(element)
Marks the element indicated by element as active, which causes it to be displayed as specified by the activeBackground and activeRelief options. The only element values understood by this method are ARROW1, SLIDER, or ARROW2. If any other value is specified then no element of the scrollbar will be active. If element is not specified, the method returns the name of the element that is currently active, or an empty string if no element is active.

delta(deltaX, deltaY)
Returns a real number indicating the fractional change in the scrollbar setting that corresponds to a given change in slider position. For example, if the scrollbar is horizontal, the result indicates how much the scrollbar setting must change to move the slider deltaX pixels to the right (deltaY is ignored in this case). If the scrollbar is vertical, the result indicates how much the scrollbar setting must change to move the slider pixels down. The arguments and the result may be zero or negative.

fraction(x, y)
fraction is a real number between 0 and 1. The widget should adjust its view so that the point given by fraction appears at the beginning of the widget. If fraction is 0 it refers to the beginning of the document. 1.0 refers to the end of the document, 0.333 refers to a point one-third of the way through the document, and so on.

get()
Returns the scrollbar settings in the form of a list whose elements are the arguments to the most recent set widget method.

identify(x, y)
Returns the name of the element under the point given by x and y (such as ARROW1), or an empty string if the point does not lie in any element of the scrollbar. x and y must be pixel coordinates relative to the scrollbar widget.

set(first, last)
This method is invoked by the scrollbar’s associated widget to tell the scrollbar about the current view in the widget. The method takes two arguments, each of which is a real fraction between 0 and 1. The fractions describe the range of the document that is visible in the asso-