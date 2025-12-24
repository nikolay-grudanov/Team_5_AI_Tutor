---
source_image: page_577.png
page_number: 577
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.37
tokens: 8502
characters: 2433
timestamp: 2025-12-24T00:48:26.216948
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
    <td>If this is greater than 0, a separator line with the specified width will be created between the button box and the child site, as a component named separator. Since the default border of the button box and child site is raised, this option does not usually need to be set for there to be a visual separation between the button box and the child site.</td>
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

Components

buttonbox
This is the button box containing the buttons for the dialog. By default it is created with the options (hull_borderwidth = 1, hull_relief = 'raised').

combobox
The widget used as the selection widget. By default, this component is a Pmw.ComboBox.

dialogchildsite
This is the child site for the dialog, which may be used to specialize the megawidget by creating other widgets within it. By default it is created with the options (borderwidth = 1, relief = 'raised').

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

separator
If the separatorwidth initialization option is nonzero, the separator component is the line dividing the area between the button box and the child site.