---
source_image: page_547.png
page_number: 547
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.87
tokens: 8472
characters: 2346
timestamp: 2025-12-24T00:47:19.550182
finish_reason: stop
---

select()
Selects the radiobutton and sets the associated variable to the value corresponding to this widget.

Scale

Description
The Scale class defines a new window and creates an instance of a scale widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the scale such as its colors, orientation, and relief. The scale method returns the identity of the new widget. At the time this command is invoked, the scale’s parent must exist.

A scale is a widget that displays a rectangular trough and a small slider. The trough corresponds to a range of real values (determined by the from, to, and resolution options), and the position of the slider selects a particular real value. The slider’s position (and hence the scale’s value) may be adjusted with the mouse or keyboard. Whenever the scale’s value is changed, a callback is invoked (using the command option) to notify other interested widgets of the change. In addition, the value of the scale can be linked to a Tkinter variable (using the variable option), so that changes in either are reflected in the other.

Three annotations may be displayed in a scale widget: a label appearing at the top right of the widget (top left for horizontal scales), a number displayed just to the left of the slider (just above the slider for horizontal scales), and a collection of numerical tick marks just to the left of the current value (just below the trough for horizontal scales). Each of these three annotations may be enabled or disabled using the configuration options.

Inheritance
Scale inherits from Widget.

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
    <td>2</td>
  </tr>
  <tr>
    <td>command</td>
    <td></td>
  </tr>
  <tr>
    <td>cursor</td>
    <td></td>
  </tr>
  <tr>
    <td>font</td>
    <td>(('MS', 'Sans', 'Serif'), '8')</td>
  </tr>
  <tr>
    <td>foreground (fg)</td>
    <td>SystemButtonText</td>
  </tr>
  <tr>
    <td>highlightbackground</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>highlightcolor</td>
    <td>SystemWindowFrame</td>
  </tr>
</table>