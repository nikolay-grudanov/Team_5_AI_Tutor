---
source_image: page_625.png
page_number: 625
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.78
tokens: 8187
characters: 1535
timestamp: 2025-12-24T00:49:28.368953
finish_reason: stop
---

vertscrollbar
The vertical scrollbar. Its component group is Scrollbar.

Methods

bbox(index)
This method is explicitly forwarded to the listbox component’s bbox() method. Without this explicit forwarding, the bbox() method (aliased to grid_bbox()) of the hull would be invoked, which is probably not what the programmer intended.

get(first = None, last = None)
This is the same as the get() method of the listbox component, except that if neither first nor last are specified, all list elements are returned.

getcurselection()
Returns the currently selected items of the listbox. This returns the text of the selected items, rather than their indexes as returned by curselection().

setlist(items)
Replaces all the items of the listbox component with those specified by the item’s sequence.

size()
This method is explicitly forwarded to the listbox component’s size() method. Without this explicit forwarding, the size() method (aliased to grid_size()) of the hull would be invoked, which is probably not what the programmer intended.

ScrolledText

![Screenshot of ScrolledText widget showing a block of text with a vertical scrollbar](../images/appendix_c_600.png)

Description
This megawidget consists of a standard text widget with optional scrollbars which can be used to scroll the text widget. The scrollbars can be dynamic, which means that a scrollbar will only be displayed if it is necessary—if the text widget does not contain enough text (either horizontally or vertically), the scrollbar will be automatically hidden.