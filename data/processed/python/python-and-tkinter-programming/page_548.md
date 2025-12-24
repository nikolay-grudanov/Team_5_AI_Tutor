---
source_image: page_548.png
page_number: 548
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.01
tokens: 8735
characters: 2776
timestamp: 2025-12-24T00:47:31.634935
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>highlightthickness</td>
    <td>2</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>flat</td>
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
    <td>15</td>
  </tr>
</table>

<h2>Options specific to Scale</h2>

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>bigincrement</td>
    <td>Some interactions with the scale widget cause its value to change by “large” increments; this option specifies the size of the large increments. If specified as 0, the large increments default to 1/10 the range of the scale.</td>
    <td>integer</td>
    <td>60</td>
    <td>0</td>
  </tr>
  <tr>
    <td>digits</td>
    <td>An integer specifying how many significant digits should be retained when converting the value of a scale widget to a string. If the number is less than or equal to zero, then the scale picks the smallest value that guarantees that every possible slider position prints as a different string.</td>
    <td>integer</td>
    <td>2</td>
    <td>0</td>
  </tr>
  <tr>
    <td>from_</td>
    <td>A real value corresponding to the left or top end of the scale widget.</td>
    <td>float</td>
    <td>0.0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>label</td>
    <td>A string to display as a label for a scale widget. For vertical scales the label is displayed just to the right of the top end of the scale. For horizontal scales the label is displayed just above the left end of the scale. If the option is specified as an empty string, no label is displayed.</td>
    <td>string</td>
    <td>Power Level</td>
    <td></td>
  </tr>
  <tr>
    <td>length</td>
    <td>Specifies the desired long dimension of the scale in screen units (i.e. any of the forms acceptable to winfo.pixels). For vertical scales this is the scale’s height; for horizontal scales it is the scale’s width.</td>
    <td>distance</td>
    <td>150 1i</td>
    <td>100</td>
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