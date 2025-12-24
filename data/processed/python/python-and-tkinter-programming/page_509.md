---
source_image: page_509.png
page_number: 509
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.13
tokens: 8340
characters: 2356
timestamp: 2025-12-24T00:46:03.953615
finish_reason: stop
---

Methods

deselect()
Deselects the checkbutton and sets the associated variable to its off value.

flash()
Flashes the checkbutton. This is accomplished by redisplaying the checkbutton several times, alternating between active and normal colors. At the end of the flash the checkbutton is left in the same normal/active state as when the method was invoked. This method is ignored if the checkbutton’s state is disabled.

invoke()
Does just what would have happened if the user invoked the checkbutton with the mouse: toggles the selection state of the button and invokes the callback associated with the checkbutton, if there is one. The return value is the return value from the callback, or an empty string if no callback is associated with the checkbutton. This method is ignored if the checkbutton’s state is disabled.

select()
Selects the checkbutton and sets the associated variable to its on value.

toggle()
Toggles the selection state of the button, redisplaying it and modifying its associated variable to reflect the new state.

Entry

Description
The Entry class defines a new window and creates an instance of an entry widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the entry such as its colors, font, and relief. The entry method returns the identity of the new widget. At the time this method is invoked, the entry’s parent must exist.

An entry is a widget that displays a one-line text string and allows that string to be edited using methods described below, which are typically bound to keystrokes and mouse actions. When first created, an entry’s string is empty. A portion of the entry may be selected as described below. If an entry is exporting its selection (see the exportSelection option), then it will observe the standard X11 protocols for handling the selection; entry selections are available as type STRING.

Entries also observe the standard Tk rules for dealing with the input focus. When an entry has the input focus it displays an insertion cursor to indicate where new characters will be inserted.

Entries are capable of displaying strings that are too long to fit entirely within the widget’s window. In this case, only a portion of the string will be displayed; commands described below may be used to change the view in the window.