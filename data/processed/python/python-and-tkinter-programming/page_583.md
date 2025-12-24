---
source_image: page_583.png
page_number: 583
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.49
tokens: 8562
characters: 2531
timestamp: 2025-12-24T00:48:32.176590
finish_reason: stop
---

indexentry(index)
Returns the numerical index of the item corresponding to index.

insertentry(index, text)
Inserts text at the integer position index.

Dialog

Description
This class creates a toplevel window composed of a button box and a child site area. The child site area can be used to specialize the megawidget by creating other widgets within it. This can be done by using this class directly or by deriving from it.

Inheritance
Dialog inherits from Pmw.MegaToplevel.

Dialog options

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
    <td>buttonboxpos</td>
    <td>Specifies on which side of the dialog window to place the button box. Must be one of N, S, E or W.</td>
    <td>anchor</td>
    <td>S</td>
  </tr>
  <tr>
    <td>buttons</td>
    <td>This must be a tuple or a list. It specifies the names on the buttons in the button box.</td>
    <td>(string, ('OK', ...))</td>
    <td></td>
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
    <td>separatorwidth</td>
    <td>If this is greater than 0, a separator line with the specified width will be created between the button box and the child site, as a component named separator. Since the default border of the button box and child site is raised, this option does not usually need to be set for there to be a visual separation between the button box and child site.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
</table>