---
source_image: page_581.png
page_number: 581
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.81
tokens: 8437
characters: 1989
timestamp: 2025-12-24T00:48:22.863997
finish_reason: stop
---

uparrow
The arrow button used for incrementing the counter. Depending on the value of orient, it will appear on the right or above the entry field. Its component group is Arrow.

Methods

decrement()
Decrements the counter once, as if the down arrow had been pressed.

increment()
Increments the counter once, as if the up arrow had been pressed.

CounterDialog

Description
A CounterDialog is a convenience dialog window with a simple counter. This is used to request the user to select a value using the up or down buttons.

Inheritance
CounterDialog inherits from Pmw.Dialog.

CounterDialog options

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
    <td>('OK', )</td>
  </tr>
  <tr>
    <td>command</td>
    <td>Specifies a function to call whenever a button in the button box is invoked or the window is deleted by the window manager. The function is called with a single argument, which is the name of the button which was invoked, or None if the window was deleted by the window manager.</td>
    <td>function</td>
    <td>None</td>
  </tr>
</table>