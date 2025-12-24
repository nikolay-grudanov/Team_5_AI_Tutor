---
source_image: page_506.png
page_number: 506
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.79
tokens: 8409
characters: 2590
timestamp: 2025-12-24T00:46:04.014642
finish_reason: stop
---

Methods

create_window(x, y, *options)
The arguments x and y specify the coordinates of a point used to position the window on the display. After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure method calls to change the item’s configuration.

delete(item)
Deletes a window item.

coords(item, x0, y0)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more window items.

Checkbutton

Description
The Checkbutton class defines a new window and creates an instance of a checkbutton widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the checkbutton such as its colors, font, text, and initial relief. The checkbutton method returns the identity of the new widget. At the time this method is invoked, the checkbutton’s parent must exist.

A checkbutton is a widget that displays a textual string, bitmap, or image and a square called an indicator. If text is displayed, it must all be in a single font, but it can occupy multiple lines on the screen (if it contains newlines or if wrapping occurs because of the wrapLength option) and one of the characters may optionally be underlined using the underline option. A checkbutton has all of the behavior of a simple button, including the following: it can display itself in either of three different ways, according to the state option; it can be made to appear raised, sunken, or flat; it can be made to flash; and it invokes a callback whenever mouse button 1 is clicked over the checkbutton. In addition, checkbuttons can be selected. If a checkbutton is selected then the indicator is normally drawn with a selected appearance, and a Tkinter variable associated with the checkbutton is set to a particular value (normally 1). Under UNIX, the indicator is drawn with a sunken relief and a special color. Under Windows, the indicator is drawn with a check markinside.

If the checkbutton is not selected, then the indicator is drawn with a deselected appearance, and the associated variable is set to a different value (typically 0). Under UNIX, the indi-