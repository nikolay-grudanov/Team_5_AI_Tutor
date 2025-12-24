---
source_image: page_584.png
page_number: 584
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.50
tokens: 8278
characters: 1745
timestamp: 2025-12-24T00:48:11.214761
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

separator
If the separatorwidth initialization option is nonzero, the separator component is the line dividing the area between the button box and the child site.

Methods

interior()
Returns the child site for the dialog. This is the same as component ('dialogchildsite').

invoke(index = 'default')
Invokes the command specified by the command option as if the button specified by index had been pressed. index may have any of the forms accepted by the Pmw.ButtonBox index() method.

EntryField

Description
This class consists of an entry widget with optional validation of various kinds. Built-in validation may be used, such as integer, real, time or date, or an external validation function may be supplied. If valid text is entered, it will be displayed with the normal background. If invalid text is entered, it is not displayed and the previously displayed text is restored. If partially valid text is entered, it