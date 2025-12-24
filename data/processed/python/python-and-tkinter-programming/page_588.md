---
source_image: page_588.png
page_number: 588
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.59
tokens: 8305
characters: 2030
timestamp: 2025-12-24T00:48:35.433171
finish_reason: stop
---

function. The stringtovalue function for the standard number validators convert the string to a number. Those for the standard alpha validators return the length of the string. Those for the standard time and date validators return the number of seconds and the Julian Day Number, respectively. See Pmw.stringtoreal(), Pmw.timestringtoseconds() and Pmw.datestringtojdn().

If the validator has been specified as a function and no stringtovalue field is given, then it defaults to the standard Python len() function.

If validator is None, no validation is performed. However, minimum and maximum checking may be performed, according to the stringtovalue function. For example, to limit the entry text to a maximum of five characters:

Pmw.EntryField(validate = {'max' : 5})

The validator functions for each of the standard validators can be accessed this way:

Pmw.numericvalidator
Pmw.integervalidator
Pmw.hexadecimalvalidator
Pmw.realvalidator
Pmw.alphabeticvalidator
Pmw.alphanumericvalidator
Pmw.timevalidator
Pmw.datevalidator

Whenever the validate option is configured, the text currently displayed in the entry widget is revalidated. If it is not valid, the errorbackground color is set and the invalidcommand function is called. However, the displayed text is not modified.

Components

entry
The widget where the user may enter text. Long text may be scrolled horizontally by dragging with the middle mouse button.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

Methods

checkentry()
Checks the validity of the current contents of the entry widget. If the text is not valid, sets the background to errorbackground and calls the invalidcommand function. If a variable is