---
source_image: page_610.png
page_number: 610
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.65
tokens: 8262
characters: 1836
timestamp: 2025-12-24T00:49:10.062326
finish_reason: stop
---

Components

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

menu
The popup menu displayed when the menu button is pressed.

menubutton
The menu button displaying the currently selected value.

Methods

get()
Returns the currently selected value.

index(index)
Returns the numerical index of the menu item corresponding to index. This may be specified in any of the following forms:

• end   Indicates the last menu item.
• name  Specifies the menu item labelled name.
• None  Specifies the currently selected menu item.

invoke (index = None)
Calling this method is the same as selecting the menu item specified by index, meaning the text displayed by the menubutton component is updated and the function specified by the command option is called. index may have any of the forms accepted by the index() method.

setitems (items, index = None)
Replaces all the items in the menu component with those specified by the items sequence. If index is not None, it sets the selected value to index, which may have any of the forms accepted by the index() method. If index is None and the textvariable option of the menubutton component is the empty string, it sets the selected value to the first value in items. If items is empty, it sets the selected value to the empty string.

If index is None and the textvariable option of the menubutton component is not the empty string, then do not set the selected value. This assumes that the variable is already (or will be) set to the desired value.