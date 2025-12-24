---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.12
tokens: 8194
characters: 1483
timestamp: 2025-12-24T00:35:01.455661
finish_reason: stop
---

3 Where validation requires complex calculations and access to servers and databases, etc., the processing load can be high. This could be a source of performance problems in certain environments.

To circumvent these and other problems you may use alternative approaches. Of course, your application may not use Pmw widgets, so yet another approach may be required.

Note Personally, I prefer not to use the built-in validation in Pmw widgets. If the action of formatting the content of the widget requires a redraw, you may observe annoying display glitches, particularly if the system is heavily loaded; these may distract the user. The following method avoids these problems.

To avoid validating every keystroke (which is how the Pmw EntryField manages data input), we will arrange for validation to be done in the following cases:

1 When the user moves the mouse pointer out of the current field.
2 When the focus is moved from the field using the TAB key.
3 When the ENTER key is pressed.

Validating this way means that you don’t get false errors as an input string is built up. In figure 6.3, for example, entering 192.311.40.10 would only raise a validation error when the field was left or if RETURN was pressed, thereby reducing operator confusion and CPU overhead..

![Figure 6.3 Data verification: error dialogs](https://i.imgur.com/3Q5z5QG.png)

Figure 6.3 Data verification: error dialogs

Example_6_8.py

import string
from Tkinter import *
from validation import *