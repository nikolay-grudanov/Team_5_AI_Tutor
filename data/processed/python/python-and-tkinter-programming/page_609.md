---
source_image: page_609.png
page_number: 609
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.28
tokens: 8445
characters: 2141
timestamp: 2025-12-24T00:49:20.540352
finish_reason: stop
---

raised()
Returns the name of the currently active pane.

reBind()
Allows selection of panes by clicking on the tabs.

unBind()
Disallows selection of panes by clicking on the tabs.

OptionMenu

Description
This class creates an option menu which consists of a menu button and an associated menu which pops up when the button is pressed. The text displayed in the menu button is updated whenever an item is selected in the menu. The currently selected value can be retrieved from the megawidget.

Inheritance
OptionMenu inherits from Pmw.MegaWidget.

OptionMenu options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>command</td>
    <td>Specifies a function to call whenever a menu item is selected or the invoke() method is called. The function is called with the currently selected value as its single argument.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>initialitem</td>
    <td>Specifies the initial selected value. This option is treated in the same way as the index argument of the setitems() method.</td>
    <td></td>
    <td>None</td>
  </tr>
  <tr>
    <td>items</td>
    <td>A sequence containing the initial items to be displayed in the menu component.</td>
    <td></td>
    <td>()</td>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labelpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>labelpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
</table>