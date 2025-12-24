---
source_image: page_601.png
page_number: 601
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.18
tokens: 8636
characters: 2554
timestamp: 2025-12-24T00:49:18.164607
finish_reason: stop
---

MessageDialog

Description
A MessageDialog is a convenience dialog window containing a message widget. This is used to display multiple lines of text to the user in a transient window.

Inheritance
MessageDialog inherits from Pmw.Dialog.

MessageDialog options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activatecommand</td>
    <td>If this is callable, it will be called whenever the megawidget is activated by a call to activate().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>borderx</td>
    <td>Specifies the width of the border to the left and right of the message area.</td>
    <td>distance</td>
    <td>20</td>
  </tr>
  <tr>
    <td>bordery</td>
    <td>Specifies the height of the border to the top and bottom of the message area.</td>
    <td>distance</td>
    <td>20</td>
  </tr>
  <tr>
    <td>buttonboxpos</td>
    <td>Specifies on which side of the dialog window to place the button box. Must be one of N, S, E or W.</td>
    <td>anchor</td>
    <td>S</td>
  </tr>
  <tr>
    <td>buttons</td>
    <td>This must be a tuple or a list. It specifies the names on the buttons in the button box.</td>
    <td>(string, ...)</td>
    <td>('OK', ...)</td>
  </tr>
  <tr>
    <td>command</td>
    <td>Specifies a function to call whenever a button in the button box is invoked or the window is deleted by the window manager. The function is called with a single argument, which is the name of the button which was invoked, or None if the window was deleted by the window manager.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>deactivatecommand</td>
    <td>If this is callable, it will be called whenever the megawidget is deactivated by a call to deactivate().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>defaultbutton</td>
    <td>Specifies the default button in the button box. If the RETURN key is hit when the dialog has focus, the default button will be invoked. If defaultbutton is None, there will be no default button and hitting the RETURN key will have no effect.</td>
    <td>index</td>
    <td>None</td>
  </tr>
  <tr>
    <td>iconmargin</td>
    <td>Specifies the space to be left around the icon, if present.</td>
    <td>distance</td>
    <td>20</td>
  </tr>
  <tr>
    <td>iconpos</td>
    <td>Determines the placement of the icon if it is to be displayed. Value must be either one of the letters N, S, E and W or None.</td>
    <td>distance</td>
    <td>None</td>
  </tr>
</table>