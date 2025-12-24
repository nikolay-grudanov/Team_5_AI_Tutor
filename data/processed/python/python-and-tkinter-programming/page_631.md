---
source_image: page_631.png
page_number: 631
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.39
tokens: 8351
characters: 1876
timestamp: 2025-12-24T00:49:48.981894
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

dialogchildsite
This is the child site for the dialog, which may be used to specialize the megawidget by creating other widgets within it. By default it is created with the options (borderwidth = 1, relief = 'raised').

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

scrolledtext
By default, this component is a Pmw.ScrolledText.

separator
If the separatorwidth initialization option is nonzero, the separator component is the line dividing the area between the button box and the child site.

Methods
This megawidget has no methods of its own.