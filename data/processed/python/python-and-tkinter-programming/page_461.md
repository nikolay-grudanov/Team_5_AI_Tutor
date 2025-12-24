---
source_image: page_461.png
page_number: 461
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.86
tokens: 8327
characters: 2183
timestamp: 2025-12-24T00:44:41.411747
finish_reason: stop
---

focus_force()
Sets the focus of the widget’s display to self, even if the application doesn’t currently have the input focus for the display. This method should be used sparingly, if at all. In normal usage, an application should not claim the focus for itself; instead, it should wait for the window manager to give it the focus.

focus_get()
If the application currently has the input focus on the widget’s display, this method returns the identity of the window with focus.

focus_lastfor()
Returns the identity of the most recent window to have the input focus among all the windows in the same top-level as self. If no window in that top-level has ever had the input focus, or if the most recent focus window has been deleted, then the ID of the top-level is returned. The return value is the window that will receive the input focus the next time the window manager gives the focus to the top-level.

focus_set()
If the application currently has the input focus on the widget’s display, this method resets the input focus for the widget’s display to self. If the application doesn’t currently have the input focus on the widget’s display, self will be remembered as the focus for its top-level; the next time the focus arrives at the top-level, Tk will redirect it to self.

getboolean(string)
Converses string to a boolean using Tcl’s conventions.

getvar(name='PY_VAR')
Returns the value of the variable name.

grab_current()
Returns the identity of the current grab window in this application for window’s display, or None if there is no such window.

grab_release()
Releases the grab on self if there is one; otherwise it does nothing.

grab_set()
Sets a grab on all events for the current application to self. If a grab was already in effect for this application on the widget’s display then it is automatically released. If there is already a grab on self then the method does nothing.

grab_set_global()
Sets a grab on all events for the entire screen to self. If a grab was already in effect for this application on the widget’s display then it is automatically released. If there is already a grab on self then the method does nothing. Be careful if you use this grab.