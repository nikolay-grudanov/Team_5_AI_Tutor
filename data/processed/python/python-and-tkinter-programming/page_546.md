---
source_image: page_546.png
page_number: 546
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.94
tokens: 8467
characters: 2369
timestamp: 2025-12-24T00:47:17.406877
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
    <td>selectcolor</td>
    <td>Specifies a background color to use when the widget (usually a check or radiobutton) is selected. If indicatoron is TRUE then the color applies to the indicator. Under Windows, this color is used as the background for the indicator regardless of the select state. If indicatoron is FALSE, this color is used as the background for the entire widget, in place of background or activeBackground, whenever the widget is selected. If specified as an empty string then no special color is used for displaying when the widget is selected.</td>
    <td>color</td>
    <td>"red"</td>
    <td>SystemWindow</td>
  </tr>
  <tr>
    <td>selectimage</td>
    <td>Specifies an image to display (in place of the image option) when the widget (typically a checkbutton) is selected. This option is ignored unless the image option has been specified.</td>
    <td>image</td>
    <td>"redcross"</td>
    <td></td>
  </tr>
  <tr>
    <td>value</td>
    <td>Specifies the value to store in the button’s associated Tkinter variable whenever this button is selected.</td>
    <td>string</td>
    <td>0 "Power"</td>
    <td></td>
  </tr>
  <tr>
    <td>variable</td>
    <td>Specifies the name of a Tkinter variable to contain the content and set the content of the widget.</td>
    <td>variable</td>
    <td>myVariable</td>
    <td>selectedButton</td>
  </tr>
</table>

Methods

deselect()
Deselects the radiobutton and sets the associated variable to an empty string. If this radiobutton was not currently selected, the method has no effect.

flash()
Flashes the radiobutton. This is accomplished by redisplaying the radiobutton several times, alternating between active and normal colors. At the end of the flash the radiobutton is left in the same normal/active state as when the method was invoked. This method is ignored if the radiobutton’s state is disabled.

invoke()
Does just what would have happened if the user invoked the radiobutton with the mouse: selects the button and invokes its associated callback, if there is one. The return value is the return value from the callback, or an empty string if no callback is associated with the radiobutton. This method is ignored if the radiobutton’s state is disabled.