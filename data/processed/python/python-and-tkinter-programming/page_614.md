---
source_image: page_614.png
page_number: 614
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.27
tokens: 8189
characters: 1576
timestamp: 2025-12-24T00:49:12.487566
finish_reason: stop
---

dialogchildsite
This is the child site for the dialog, which may be used to specialize the megawidget by creating other widgets within it. By default it is created with the options (borderwidth = 1, relief = 'raised').

entryfield
By default, this component is a Pmw.EntryField.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

separator
If the separatorwidth initialization option is nonzero, the separator component is the line dividing the area between the button box and the child site.

Methods

deleteentry(first, last = None)
Removes characters from the entryField starting at first and ending at last. first and last are integer indices. If last is None, first will be deleted.

indexentry(index)
Returns the numerical index of the character corresponding to index.

insertentry(index, text)
Inserts text at the integer position index.

RadioSelect

Description
This class creates a manager widget for containing buttons. The buttons may be laid out either horizontally or vertically. In single selection mode, only one button may be selected at any one time. In multiple selection mode, several buttons may be selected at the same time and clicking on a selected button will deselect it.
The buttons displayed can be either standard buttons, radio buttons or check buttons. When selected, standard buttons are displayed sunken, and radio and check buttons are displayed with the appropriate indicator color and relief.

Inheritance
RadioSelect inherits from Pmw.MegaWidget.