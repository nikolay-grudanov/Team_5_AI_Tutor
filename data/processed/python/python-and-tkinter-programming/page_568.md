---
source_image: page_568.png
page_number: 568
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.45
tokens: 8798
characters: 3046
timestamp: 2025-12-24T00:48:28.733411
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activatecommand</td>
    <td>If this is callable, it will be called whenever the mega-widget is activated by a call to activate().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>applicationname</td>
    <td>Sets the application name displayed by AboutDialog.</td>
    <td>string</td>
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
    <td>Specifies on which side of the dialog window to place the button box. Must be one of N, S, E, or W.</td>
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
    <td>If this is callable, it will be called whenever the mega-widget is deactivated by a call to deactivate().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>defaultbutton</td>
    <td>Specifies the default button in the button box. If the Return key is pressed when the dialog has focus, the default button will be invoked. If defaultbutton is None, there will be no default button and pressing the Return key will have no effect.</td>
    <td>index</td>
    <td>0</td>
  </tr>
  <tr>
    <td>iconmargin</td>
    <td>Specifies the space to be left around the icon, if present.</td>
    <td>distance</td>
    <td>20</td>
  </tr>
  <tr>
    <td>iconpos</td>
    <td>Determines the placement of the icon if it is to be displayed. Value must be either one of the letters N, S, E, and W or None.</td>
    <td>anchor</td>
    <td>W</td>
  </tr>
  <tr>
    <td>separatorwidth</td>
    <td>If this is greater than 0, a separator line with the specified width will be created between the button box and the child site, as a component-named separator. Since the default border of the button box and child site is raised, this option does not usually need to be set for there to be a visual separation between the button box and child site.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>title</td>
    <td>This is the title that the window manager displays in the title bar of the window.</td>
    <td>string</td>
    <td>None</td>
  </tr>
</table>