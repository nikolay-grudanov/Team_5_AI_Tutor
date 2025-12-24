---
source_image: page_508.png
page_number: 508
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.02
tokens: 8576
characters: 2338
timestamp: 2025-12-24T00:46:17.787369
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>underline</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>width</td>
    <td>0</td>
  </tr>
  <tr>
    <td>wraplength</td>
    <td>0</td>
  </tr>
</table>

<h2>Options specific to Checkbutton</h2>

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>indicatoron</td>
    <td>Specifies whether or not the indicator should be drawn. Must be a proper boolean value. If FALSE, the relief option is ignored and the widget’s relief is always sunken if the widget is selected and raised otherwise.</td>
    <td>Boolean</td>
    <td>0 TRUE</td>
    <td>1</td>
  </tr>
  <tr>
    <td>offvalue</td>
    <td>Specifies the value to store in the widgets’s associated variable whenever this button is deselected. Defaults to 0.</td>
    <td>string</td>
    <td>0 off</td>
    <td>0</td>
  </tr>
  <tr>
    <td>onvalue</td>
    <td>Specifies the value to store in the widget’s associated variable whenever this button is selected. Defaults to 1.</td>
    <td>string</td>
    <td>1 On</td>
    <td>1</td>
  </tr>
  <tr>
    <td>selectcolor</td>
    <td>Specifies a background color to use when the widget (usually a check or radio button) is selected. If indicatoron is TRUE then the color applies to the indicator. Under Windows, this color is used as the background for the indicator regardless of the select state. If indicatoron is FALSE, this color is used as the background for the entire widget, in place of background or activeBackground, whenever the widget is selected. If specified as an empty string then no special color is used for displaying when the widget is selected.</td>
    <td>color</td>
    <td>"red"</td>
    <td>System-Window</td>
  </tr>
  <tr>
    <td>selectimage</td>
    <td>Specifies an image to display (in place of the image option) when the widget (typically a checkbutton) is selected. This option is ignored unless the image option has been specified.</td>
    <td>image</td>
    <td>"red-cross"</td>
    <td></td>
  </tr>
  <tr>
    <td>variable</td>
    <td>Specifies name of a Tkinter variable to contain the content and set the content of the widget.</td>
    <td>variable</td>
    <td>myVariable</td>
    <td></td>
  </tr>
</table>