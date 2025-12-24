---
source_image: page_463.png
page_number: 463
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.43
tokens: 8335
characters: 2338
timestamp: 2025-12-24T00:44:46.259520
finish_reason: stop
---

with the highest priority level. If there are several matching entries at the same priority level, then it returns whichever entry was most recently entered into the option database. If there are no matching entries, then the empty string is returned.

option_readfile(fileName, priority = None)
Reads fileName, which should have the standard format for an X resource database such as .Xdefaults, and it adds all the options specified in that file to the option database. If priority is specified, it indicates the priority level at which to enter the options; priority defaults to interactive.

quit()
Exits the mainloop.

selection_clear()
Clears the selection if it is currently in this widget. If the selection isn’t in this widget then the method has no effect.

selection_get()
Retrieves the value of selection from the window’s display and returns it as a result.

selection_handle(handler)
Creates a handler for selection requests, such that handler will be executed whenever selection is owned by the window and someone attempts to retrieve it in the form given by type (e.g. type is specified in the selection_get method). selection defaults to PRIMARY, type defaults to STRING, and format defaults to STRING. If handler is empty then any existing handler for the window, type and selection is removed.

selection_own()
Causes self to become the new owner of selection on the window’s display, returning an empty string as a result. The existing owner, if any, is notified that it has lost the selection.

selection_own_get()
Returns the identity of the window in this application that owns selection on the display containing self, or an empty string if no window in this application owns the selection. selection defaults to PRIMARY and window defaults to the root window.

send(interp, cmd, *args)
Arranges for cmd (and args) to be executed in the application named by interp. It returns the result or error from that command execution. interp may be the name of any application whose main window is on the display containing the sender’s main window; it need not be within the same process. If no args arguments are present, then the command to be executed is contained entirely within the cmd argument. If one or more args are present, they are concatenated to form the command to be executed, just as for the eval command.