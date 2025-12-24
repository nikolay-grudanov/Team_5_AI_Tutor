---
source_image: page_335.png
page_number: 335
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.57
tokens: 8124
characters: 1124
timestamp: 2025-12-24T00:40:37.286500
finish_reason: stop
---

WM_SAVE_YOURSELF is less commonly encountered and is usually sent before a WM_DELETE_WINDOW is sent. WM_TAKE_FOCUS may be used by an application to allow special action to be taken when focus is gained (perhaps a polling cycle is executed more frequently when a window has focus, for example).

13.6 Miscellaneous wm methods

There are several window manager methods, many of which you may never need to look at. They are documented in “Inherited methods” on page 433. However, you might find a few of them useful.

To raise or lower a window in the window stack, use lift and lower (you cannot use “raise” since that is a Python keyword):

self.top.lift()                # Bring to top of stack
self.top.lift(name)             # Lift on top of 'name'
self.top.lower(self.spam)       # Lower just below self.spam

To find which screen your window is on (this is really only useful for X Window), use:

screen = self.root.screen()
print screen
    :0.1

Note Win32 readers The numbers returned refer to the display and screen within that display. X window is capable of supporting multiple display devices on the same system.