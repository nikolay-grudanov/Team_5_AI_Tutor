---
source_image: page_619.png
page_number: 619
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.12
tokens: 8414
characters: 2130
timestamp: 2025-12-24T00:49:28.788502
finish_reason: stop
---

interior()
Returns the canvas widget within which the programmer should create graphical items and child widgets. This is the same as component('canvas').

resizescrollregion()
Resizes the scrollregion of the canvas component to be the bounding box covering all the items in the canvas plus a margin on all sides, as specified by the canvasmargin option.

ScrolledField

Description
This megawidget displays a single line of text. If the text is wider than the widget the user can scroll to the left and right by dragging with the middle mouse button. The text is also selectable by clicking or dragging with the left mouse button.
    This megawidget can be used instead of a Label widget when displaying text of unknown width such as application status messages.

Inheritance
    ScrolledField inherits from Pmw.MegaWidget.

ScrolledField options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labelfpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>labelfpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelfpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
  <tr>
    <td>text</td>
    <td>Specifies the text to display in the scrolled field.</td>
    <td>string</td>
    <td>None</td>
  </tr>
</table>

Components

entry
This is used to display the text and it allows the user to scroll and select the text. The state of this component is set to disabled, so that the user is unable to modify the text.