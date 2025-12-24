---
source_image: page_544.png
page_number: 544
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.57
tokens: 8365
characters: 2427
timestamp: 2025-12-24T00:47:09.533287
finish_reason: stop
---

Radiobutton

Description
The Radiobutton class defines a new window and creates an instance of a radiobutton widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the radiobutton such as its colors, font, text, and initial relief. The radiobutton method returns the identity of the new widget. At the time this command is invoked, the radiobutton’s parent must exist.

A radiobutton is a widget that displays a textual string, bitmap or image and a diamond or circle called an indicator. If text is displayed, it must all be in a single font, but it can occupy multiple lines on the screen (if it contains newlines or if wrapping occurs because of the wrapLength option), and one of the characters may optionally be underlined using the underline option.

A radiobutton has all of the behavior of a simple button: it can display itself in either of three different ways, according to the state option; it can be made to appear raised, sunken, or flat; it can be made to flash; and it invokes a Tcl command whenever mouse button 1 is clicked over the checkbutton. In addition, radiobuttons can be selected.

If a radiobutton is selected, the indicator is normally drawn with a selected appearance, and a Tkinter variable associated with the radiobutton is set to a particular value (normally 1). Under UNIX, the indicator is drawn with a sunken relief and a special color. Under Windows, the indicator is drawn with a round mark inside.

If the radiobutton is not selected, then the indicator is drawn with a deselected appearance, and the associated variable is set to a different value (typically 0). Under UNIX, the indicator is drawn with a raised relief and no special color. Under Windows, the indicator is drawn without a round mark inside.

Typically, several radiobuttons share a single variable and the value of the variable indicates which radiobutton is to be selected. When a radiobutton is selected it sets the value of the variable to indicate that fact; each radiobutton also monitors the value of the variable and automatically selects and deselects itself when the variable’s value changes.

Configuration options may also be used to modify the way the indicator is displayed (or whether it is displayed at all). By default a radiobutton is configured to select itself on button clicks.

Inheritance
Radiobutton inherits from Widget.