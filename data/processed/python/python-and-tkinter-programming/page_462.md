---
source_image: page_462.png
page_number: 462
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.55
tokens: 8333
characters: 2275
timestamp: 2025-12-24T00:44:44.348344
finish_reason: stop
---

grab_status()
Returns None if no grab is currently set on window, local if a local grab is set on window, and global if a global grab is set.

image_names()
Returns a list containing the names of all existing images.

image_types()
Returns a list of all image types that have been created.

keys()
Returns a tuple containing the names of the options available for this widget. Use self.cget to obtain the current value for each option.

lower(belowThis=None)
Changes the widget’s position in the stacking order. If the belowThis argument is omitted then the method lowers the window so that it is below all of its siblings in the stacking order (it will be obscured by any siblings that overlap it and will not obscure any siblings). If belowThis is specified then it must be the identity of a window that is either a sibling of window or the descendant of a sibling of window. In this case the lower method will insert the window into the stacking order just below belowThis (or the ancestor of belowThis that is a sibling of window); this could end up either raising or lowering the window.

mainloop
Starts processing the event loop. Nothing will be updated until this method is called and this method does not return until the quit method is called.

nametowidget(name)
Returns the widget identity corresponding to name.

option_add(pattern, value, priority = None)
Allows you to add entries to the Tk option database. pattern contains the option being specified, and it consists of names and/or classes separated by asterisks or dots, in the usual X format. value contains a text string to associate with pattern; this is the value that will be returned in calls to Tkinter (Tk_GetOption) or by invocations of the option_get method. If priority is specified, it indicates the priority level for this option; it defaults to interactive.

option_clear()
Clears the Tk option database. Default options (from the RESOURCE_MANAGER property or the .Xdefaults file) will be reloaded automatically the next time an option is added to the database or removed from it.

option_get(name, className)
Returns the value of the option specified for self under name and class. If several entries in the option database match name and class, then the method returns whichever was created