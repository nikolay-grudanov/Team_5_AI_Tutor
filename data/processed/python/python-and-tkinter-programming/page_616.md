---
source_image: page_616.png
page_number: 616
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.58
tokens: 8201
characters: 1595
timestamp: 2025-12-24T00:49:16.139434
finish_reason: stop
---

label
If the labelfos option is not None, this component is created as a text label for the mega-widget. See the labelfos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

Methods

add(name, ** kw)
Adds a button to the end of the radio select widget as a component named name, with a default type as specified by buttontype. Any keyword arguments present (except command) will be passed to the constructor when creating the button. If the text keyword argument is not given, the text option of the button defaults to name. The method returns the name component widget.

deleteall()
Deletes all buttons and clears the current selection.

getcurselection()
In single selection mode, returns the name of the currently selected button, or None if no buttons have been selected yet. In multiple selection mode, returns a list of the names of the currently selected buttons.

index(index)
Returns the numerical index of the button corresponding to index. This may be specified in any of the following forms:
• number Specifies the button numerically, where 0 corresponds to the left (or top) button.
• end Indicates the right (or bottom) button.
• name Specifies the button named name.

invoke (index)
Calling this method is the same as clicking on the button specified by index: the buttons are displayed selected or deselected according to the selection mode and command is called. index may have any of the forms accepted by the index() method.

numbuttons ()
Returns the number of buttons in the radio select widget.