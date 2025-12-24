---
source_image: page_535.png
page_number: 535
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.69
tokens: 8362
characters: 2064
timestamp: 2025-12-24T00:47:01.024688
finish_reason: stop
---

Options specific to Message

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>aspect</td>
    <td>Specifies a non-negative integer value indicating the desired aspect ratio for the text. The aspect ratio is specified as 100*width/height. 100 means the text should be as wide as it is tall, 200 means the text should be twice as wide as it is tall, 50 means the text should be twice as tall as it is wide, and so on. Used to choose line length for text if the width option isn’t specified. Defaults to 150.</td>
    <td>integer</td>
    <td>50 75</td>
    <td>150</td>
  </tr>
</table>

Methods

message(options...)
options determine the exact behavior of the message method.

cget(option)
Returns the current value of the configuration option.

configure(options...)
Queries or modifies the configuration options of the widget. If no option is specified, returns a dictionary describing all of the available options for the menubutton. If option is specified with no value, then the command returns a dictionary describing the one named option. If one or more option-value pairs are specified, then the method modifies the given widget option(s) to have the given value(s); in this case the method returns an empty string. options may have any of the values accepted by the message method.

OptionMenu class

Description
This class instantiates an option menubutton with an associated menu. Together they allow the user to select one of the values given by the value arguments. The current value will be stored in the Tkinter variable whose name is given in the constructor and it will also be displayed as the label in the option menubutton. The user can click on the menubutton to display a menu containing all of the values and thereby select a new value. Once a new value is selected, it will be stored in the variable and appear in the option menubutton. The current value can also be changed by setting the variable.

Inheritance
Inherits from Menubutton.