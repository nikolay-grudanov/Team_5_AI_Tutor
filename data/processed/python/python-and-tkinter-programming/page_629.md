---
source_image: page_629.png
page_number: 629
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.00
tokens: 8153
characters: 1104
timestamp: 2025-12-24T00:49:33.215509
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

scrolledlist
By default, this component is a Pmw.ScrolledListBox.

separator
If the separatorwidth initialization option is nonzero, the separator component is the line dividing the area between the button box and the child site.

Methods
This megawidget has no methods of its own.