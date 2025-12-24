---
source_image: page_569.png
page_number: 569
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.96
tokens: 8117
characters: 1185
timestamp: 2025-12-24T00:47:56.652207
finish_reason: stop
---

Components

buttonbox
This is the button box containing the buttons for the dialog. By default, it is created with the options (hull_borderwidth = 1, hull_relief = 'raised').

dialogchildsite
This is the child site for the dialog, which may be used to specialize the megawidget by creating other widgets within it. By default it is created with the options (borderwidth = 1, relief = 'raised').

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

icon
This is the icon to display alongside the message.

message
This widget contains the text displayed within the dialog.

separator
If the separatorwidth initialization option is nonzero, the separator component is the line dividing the area between the button box and the child site.

Methods
There are no AboutDialog methods, other than inherited methods from the base classes.

Functions

aboutversion(value)
Sets the version displayed by the AboutDialog to value.

aboutcopyright(value)
Sets the copyright string displayed by the AboutDialog to value.

aboutcontact(value)
Sets the contact information displayed by the AboutDialog to value.