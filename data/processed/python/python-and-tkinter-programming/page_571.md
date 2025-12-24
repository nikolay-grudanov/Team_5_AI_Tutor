---
source_image: page_571.png
page_number: 571
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.14
tokens: 8182
characters: 1417
timestamp: 2025-12-24T00:48:02.132510
finish_reason: stop
---

label
If the labelfos option is not None, this component is created as a text label for the mega-widget. See the labelfos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

Methods

bind(widget, balloonHelp, statusHelp = None)
Adds balloonHelp to the specified widget. If statusHelp is None, balloonHelp is bound as the status message. If statusHelp is specified, the bind message is bound to the status area for widget. If both balloonHelp and statusHelp are None, bind(widget, None) is equivalent to unbind(widget).

clearstatus()
Removes any existing status message.

showstatus(statusHelp)
If statuscommand is defined, it is called with statusHelp as its argument.

tagbind(widget, tagOrItem, balloonHelp, statusHelp = None)
Similar to bind, this method adds balloonHelp to the item tagOrItem defined within widget.

tagunbind(widget, tagOrItem)
Removes any existing binding for tagOrId within widget.

unbind(widget)
Removes all <Motion>, <Enter>, <Leave> and <ButtonPress> bindings for widget.

ButtonBox

Description
This class creates a manager widget for containing buttons. One of these buttons may be specified as the default and it will be displayed with the platform-specific appearance for a default button. The buttons may be laid out either horizontally or vertically.

Inheritance
ButtonBox inherits from Pmw.MegaWidget.