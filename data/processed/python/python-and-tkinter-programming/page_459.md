---
source_image: page_459.png
page_number: 459
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.61
tokens: 8341
characters: 2267
timestamp: 2025-12-24T00:44:39.703823
finish_reason: stop
---

much longer. The method returns id which may be used as the argument to after_cancel to cancel the callback.

after_cancel(id)
Cancels the specified after callback.

after_idle(function, *args)
Registers a callback function which is called when the system is idle (no more events in the event queue). The callback is called once for each call to after_idle.

bell(displayof=0)
Rings the bell on the display for the window and returns None. If the displayof option is omitted, the display of the application’s main window is used by default. The method uses the current bell-related settings for the display, which may be modified with programs such as xset. This method also resets the screen saver for the screen. Some screen savers will ignore this, but others will reset so that the screen becomes visible again.

bind(sequence=None, function=None, add=None)
Associates event handlers with events. If add is + the binding is added to the current bindings; the default is to replace the existing binding.

bind_all(sequence=None, function=None, add=None)
Associates event handlers with events at the application level. If add is + the binding is added to the current bindings; the default is to replace the existing binding.

bind_class(className, sequence=None, function=None, add=None)
Associates event handlers with events for the specified widget class. If add is + the binding is added to the current bindings; the default is to replace the existing binding.

bindtags(tagList=None)
If bindtags is invoked without an argument, then the current set of binding tags for the widget is returned as a tuple. If the tagList argument is specified to bindtags, then it must be a proper tuple; the tags for window are changed to the elements of the list. The elements of tagList may be arbitrary strings; however, any tag starting with a dot is treated as the name of a Tk window. If no window by that name exists at the time an event is processed, then the tag is ignored for that event. The order of the elements in tagList determines the order in which binding scripts are executed in response to events.

cget(key)
Returns the current value of the configuration option given by key.

clipboard_append(string)
Appends string to the clipboard on the window’s display.