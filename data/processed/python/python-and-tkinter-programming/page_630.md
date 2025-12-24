---
source_image: page_630.png
page_number: 630
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.96
tokens: 8420
characters: 1824
timestamp: 2025-12-24T00:49:54.492771
finish_reason: stop
---

TextDialog

Description
A TextDialog is a convenience dialog window containing a scrolled text widget. This is used to display multiple lines of text to the user.

Inheritance
TextDialog inherits from Pmw.Dialog.

TextDialog options

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
    <td>10</td>
  </tr>
  <tr>
    <td>bordery</td>
    <td>Specifies the height of the border to the top and bottom of the message area.</td>
    <td>distance</td>
    <td>10</td>
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
    <td>('OK', )</td>
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
</table>