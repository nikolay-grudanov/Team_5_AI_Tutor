---
source_image: page_533.png
page_number: 533
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.12
tokens: 8419
characters: 2158
timestamp: 2025-12-24T00:46:59.039964
finish_reason: stop
---

Options specific to Menubutton

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>direction</td>
    <td>Specifies where the menu is going to pop up. ABOVE tries to pop the menu above the menubutton. BELOW tries to pop the menu below the menubutton. LEFT tries to pop the menu to the left of the menubutton. RIGHT tries to pop the menu to the right of the menu button. FLUSH pops the menu directly over the menubutton.</td>
    <td>constant</td>
    <td>FLUSH<br>"above"</td>
    <td>below</td>
  </tr>
  <tr>
    <td>indicatoron</td>
    <td>Specifies whether or not the indicator should be drawn. Must be a proper boolean value. If FALSE, the relief option is ignored and the widget’s relief is always sunken if the widget is selected; otherwise, it is raised.</td>
    <td>Boolean</td>
    <td>0 TRUE</td>
    <td>0</td>
  </tr>
  <tr>
    <td>menu</td>
    <td>Specifies the pathname of the menu associated with a menubutton. The menu must be a child of the menubutton.</td>
    <td>string</td>
    <td>subMenu-Action</td>
    <td></td>
  </tr>
</table>

Methods

menubutton(options...)
options determine the exact behavior of the menubutton method.

cget(option)
Returns the current value of the configuration option.

configure(options...)
Queries or modifies the configuration options of the widget. If no option is specified, returns a dictionary describing all of the available options for the menubutton. If option is specified with no value, then the command returns a dictionary describing the one named option. If one or more option-value pairs are specified, then the method modifies the given widget option(s) to have the given value(s); in this case the method returns an empty string. options may have any of the values accepted by the menubutton method.

Message

Description
The Message class defines a new window and creates an instance of a message widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the message such as its colors, font, text, and initial