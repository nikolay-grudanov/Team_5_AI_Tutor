---
source_image: page_482.png
page_number: 482
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.63
tokens: 8685
characters: 2871
timestamp: 2025-12-24T00:45:29.406240
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>closeenough</td>
    <td>Specifies a floating-point value indicating how close the mouse cursor must be to an item before it is considered to be “inside” the item. Defaults to 1.0.</td>
    <td>float</td>
    <td>0.5</td>
    <td>1</td>
  </tr>
  <tr>
    <td>confine</td>
    <td>Specifies a boolean value that indicates whether or not it should be allowable to set the canvas’s view outside the region defined by the scrollregion argument. Defaults to TRUE, which means that the view will be constrained within the scroll region.</td>
    <td>boolean</td>
    <td>FALSE</td>
    <td>1</td>
  </tr>
  <tr>
    <td>insertbackground</td>
    <td>Specifies the color to use as background in the area covered by the insertion cursor. This color will normally override either the normal background for the widget (or the selection background if the insertion cursor happens to fall in the selection).</td>
    <td>color</td>
    <td>'yellow'</td>
    <td>SystemButtonText</td>
  </tr>
  <tr>
    <td>insertborderwidth</td>
    <td>Specifies a non-negative value indicating the width of the 3-D border to draw around the insertion cursor. The value may have any of the forms acceptable to Tkinter (Tk_GetPixels).</td>
    <td>pixel</td>
    <td>2</td>
    <td>0</td>
  </tr>
  <tr>
    <td>insertofftime</td>
    <td>Specifies a non-negative integer value indicating the number of milliseconds the insertion cursor should remain “off” in each blink cycle. If this option is zero then the cursor doesn’t blink—it is on all the time.</td>
    <td>integer</td>
    <td>250</td>
    <td>300</td>
  </tr>
  <tr>
    <td>insertontime</td>
    <td>Specifies a non-negative integer value indicating the number of milliseconds the insertion cursor should remain “on” in each blink cycle.</td>
    <td>integer</td>
    <td>175</td>
    <td>600</td>
  </tr>
  <tr>
    <td>insertwidth</td>
    <td>Specifies a value indicating the total width of the insertion cursor. The value may have any of the forms acceptable to Tkinter (Tk_GetPixels). If a border has been specified for the insertion cursor (using the insertBorderWidth option), the border will be drawn inside the width specified by the insertWidth option.</td>
    <td>pixel</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>scrollregion</td>
    <td>Specifies a list with four coordinates describing the left, top, right, and bottom coordinates of a rectangular region. This region is used for scrolling purposes and is considered to be the boundary of the information in the canvas. Each of the coordinates may be specified in any of the forms given in the COORDINATES section below.</td>
    <td>list</td>
    <td>(10,10,200,250)</td>
    <td></td>
  </tr>
</table>