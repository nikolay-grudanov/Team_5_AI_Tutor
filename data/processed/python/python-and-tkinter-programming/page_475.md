---
source_image: page_475.png
page_number: 475
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.18
tokens: 8527
characters: 3342
timestamp: 2025-12-24T00:45:15.936117
finish_reason: stop
---

positionfrom(who=None)
If who is specified, it must be either program or user, or an abbreviation of one of these two. It indicates whether window’s current position was requested by the program or by the user. Many window managers ignore program-requested initial positions and ask the user to manually position the window; if user is specified then the window manager should position the window at the given place without asking the user for assistance.

If who is specified as an empty string, then the current position source is cancelled. If who is specified, then the method returns an empty string. Otherwise it returns user or window to indicate the source of the window’s current position, or an empty string if no source has been specified yet. Most window managers interpret no source as equivalent to program. Tk will automatically set the position source to user when a wm_geometry method is invoked, unless the source has been set explicitly to program.

protocol(name=None, function=None)
This method is used to manage window manager protocols such as WM_DELETE_WINDOW. Name is the name of an atom corresponding to a window manager protocol, such as WM_DELETE_WINDOW or WM_SAVE_YOURSELF or WM_TAKE_FOCUS. If both name and function are specified, then function is associated with the protocol specified by name. name will be added to window’s WM_PROTOCOLS property to tell the window manager that the application has a protocol handler for name, and function will be invoked in the future whenever the window manager sends a message to the client for that protocol. In this case the method returns an empty string.

If name is specified but function isn’t, then the current function for name is returned, or an empty string is returned if there is no handler defined for name. If function is specified as an empty string then the current handler for name is deleted and it is removed from the WM_PROTOCOLS property on window; an empty string is returned.

Lastly, if neither name nor function is specified, the method returns a list of all the protocols for which handlers are currently defined for window. Tk always defines a protocol handler for WM_DELETE_WINDOW, even if you haven’t asked for one with wm protocol. If a WM_DELETE_WINDOW message arrives when you haven’t defined a handler, then Tk handles the message by destroying the window for which it was received.

resizable(width=None, height=None)
This method controls whether or not the user may interactively resize a top level window. If width and height are specified, they are boolean values that determine whether the width and height of window may be modified by the user. In this case the method returns an empty string. If width and height are omitted then the method returns a list with two FALSE/TRUE elements that indicate whether the width and height of window are currently resizable. By default, windows are resizable in both dimensions. If resizing is disabled, then the window’s size will be the size from the most recent interactive resize or wm_geometry call. If there has been no such operation then the window’s natural size will be used.

sizefrom(who=None)
If who is specified, it must be either program or user, or an abbreviation of one of these two. It indicates whether window’s current size was requested by the program or by the user. Some