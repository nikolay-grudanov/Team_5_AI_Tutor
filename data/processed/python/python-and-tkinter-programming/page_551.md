---
source_image: page_551.png
page_number: 551
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.96
tokens: 8667
characters: 2593
timestamp: 2025-12-24T00:47:42.032024
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>cursor</td>
    <td></td>
  </tr>
  <tr>
    <td>highlightbackground</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>highlightcolor</td>
    <td>SystemWindowFrame</td>
  </tr>
  <tr>
    <td>highlightthickness</td>
    <td>0</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>sunken</td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td></td>
  </tr>
  <tr>
    <td>width</td>
    <td>16</td>
  </tr>
</table>

<h2>Options specific to Scrollbar</h2>

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activerelief</td>
    <td>Specifies the relief to use when displaying the element that is active, if any. Elements other than the active element are always displayed with a raised relief.</td>
    <td>constant</td>
    <td>SUNKEN</td>
    <td>raised</td>
  </tr>
  <tr>
    <td>elementborderwidth</td>
    <td>Specifies the width of borders drawn around the internal elements of a scrollbar (the two arrows and the slider). The value may have any of the forms acceptable to winfo.pixels. If this value is less than zero, the value of the borderwidth option is used in its place.</td>
    <td>distance</td>
    <td>10 1m</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>jump</td>
    <td>For widgets with a slider that can be dragged to adjust a value, such as scrollbars, this option determines when notifications are made about changes in the value. The option’s value must be a boolean of the form accepted by Tcl_GetBoolean. If the value is false, updates are made continuously as the slider is dragged. If the value is true, updates are delayed until the mouse button is released to end the drag; at that point a single notification is made (the value “jumps” rather than changing smoothly).</td>
    <td>boolean</td>
    <td>TRUE NO</td>
    <td>0</td>
  </tr>
  <tr>
    <td>orient</td>
    <td>For widgets that can lay themselves out with either a horizontal or vertical orientation, such as scrollbars, this option specifies which orientation should be used. Must be either HORIZONTAL or VERTICAL or an abbreviation of one of these.</td>
    <td>constant</td>
    <td>VERTICAL "vertical"</td>
    <td>vertical</td>
  </tr>
  <tr>
    <td>repeatdelay</td>
    <td>Specifies the number of milliseconds a button or key must be held down before it begins to auto-repeat. Used, for example, on the up- and down-arrows in scrollbars.</td>
    <td>integer</td>
    <td>300</td>
    <td>300</td>
  </tr>
</table>