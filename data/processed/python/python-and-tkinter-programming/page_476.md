---
source_image: page_476.png
page_number: 476
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.63
tokens: 8384
characters: 2656
timestamp: 2025-12-24T00:45:08.685281
finish_reason: stop
---

window managers ignore program-requested sizes and ask the user to manually size the window; if user is specified then the window manager should give the window its specified size without asking the user for assistance.

If who is specified as an empty string, then the current size source is cancelled. If who is specified, then the method returns an empty string. Otherwise it returns user or window to indicate the source of the window’s current size, or an empty string if no source has been specified yet. Most window managers interpret no source as equivalent to program.

state()
Specifies one of three states for the button: NORMAL, ACTIVE, or DISABLED. In NORMAL state the button is displayed using the foreground and background options. ACTIVE state is typically used when the pointer is over the button. In active state the button is displayed using the activeForeground and activeBackground options. DISABLED state means that the button should be insensitive: the default bindings will refuse to activate the widget and will ignore mouse button presses. In this state the disabledForeground and background options determine how the button is displayed.

title(string=None)
If string is specified, then it will be passed to the window manager for use as the title for window (the window manager should display this string in window’s title bar). If string isn’t specified then the method returns the current title for the window. The title for a window defaults to its name.

transient(master=None)
If master is specified, then the window manager is informed that window is a transient window (such as a pull-down menu) working on behalf of master (where master is the identity for a top-level window). Some window managers will use this information to manage window specially. If master is specified as an empty string then window is marked as not being a transient window any more. If master is specified, then the method returns an empty string. Otherwise the method returns the path name of window’s current master or an empty string if window isn’t currently a transient window.

withdraw()
Arranges for the window to be withdrawn from the screen. This causes the window to be unmapped and forgotten about by the window manager. If the window has never been mapped, then this method causes the window to be mapped in the withdrawn state. Not all window managers appear to know how to handle windows that are mapped in the withdrawn state.

Note: It sometimes seems to be necessary to withdraw a window and then re-map it (such as with wm deiconify) to get some window managers to pay attention to changes in window attributes such as group.