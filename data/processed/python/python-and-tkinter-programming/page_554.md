---
source_image: page_554.png
page_number: 554
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.56
tokens: 8710
characters: 2660
timestamp: 2025-12-24T00:47:59.736404
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>padx</td>
    <td>1</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>1</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>sunken</td>
  </tr>
  <tr>
    <td>selectbackground</td>
    <td>SystemHighlight</td>
  </tr>
  <tr>
    <td>selectborderwidth</td>
    <td>0</td>
  </tr>
  <tr>
    <td>selectforeground</td>
    <td>SystemHighlightText</td>
  </tr>
  <tr>
    <td>state</td>
    <td>normal</td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td></td>
  </tr>
  <tr>
    <td>width</td>
    <td>80</td>
  </tr>
  <tr>
    <td>xscrollcommand</td>
    <td></td>
  </tr>
</table>

Options specific to Text

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>exportselection</td>
    <td>Specifies whether or not a selection in the widget should also be the X selection. The value may have any of the forms accepted by Tcl_GetBoolean, such as true, false, 0, 1, yes, or no. If the selection is exported, then selecting in the widget deselects the current X selection, selecting outside the widget deselects any widget selection, and the widget will respond to selection retrieval requests when it has a selection. The default is usually for widgets to export selections.</td>
    <td>boolean</td>
    <td>0 YES</td>
    <td>1</td>
  </tr>
  <tr>
    <td>insertbackground</td>
    <td>Specifies the color to use as background in the area covered by the insertion cursor. This color will normally override either the normal background for the widget or the selection background if the insertion cursor happens to fall in the selection.</td>
    <td>color</td>
    <td>'yellow'</td>
    <td>System-Window-Text</td>
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
    <td>Specifies a non-negative integer value indicating the number of milliseconds the insertion cursor should remain “off” in each blink cycle. If this option is zero then the cursor doesn’t blink: it is on all the time.</td>
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
</table>