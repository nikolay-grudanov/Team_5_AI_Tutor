---
source_image: page_524.png
page_number: 524
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.78
tokens: 8338
characters: 2247
timestamp: 2025-12-24T00:46:32.275927
finish_reason: stop
---

Methods

activate(index)
Sets the active element to the one indicated by index. If index is outside the range of elements in the listbox then the closest element is activated. The active element is drawn with an underline when the widget has the input focus, and its index may be retrieved with the index active.

bbox(index)
Returns a list of four numbers describing the bounding box of the text in the element given by index. The first two elements of the list give the x and y coordinates of the upper-left corner of the screen area covered by the text (specified in pixels relative to the widget) and the last two elements give the width and height of the area, in pixels. If no part of the element given by index is visible on the screen, or if index refers to a non-existent element, then the result is None; if the element is partially visible, the result gives the full area of the element, including any parts that are not visible.

curselection()
Returns a list containing the numerical indices of all of the elements in the listbox that are currently selected. If no elements are selected in the listbox then an empty string is returned.

delete(first, last=None)
Deletes one or more elements of the listbox. first and last are indices specifying the first and last elements in the range to delete. If last isn’t specified it defaults to first, for example, a single element is deleted.

get(first, last=None)
If last is omitted, returns the contents of the listbox element indicated by first, or an empty string if first refers to a non-existent element. If last is specified, the method returns a list whose elements are all of the listbox elements between first and last, inclusive. Both first and last may have any of the standard forms for indices.

index(index)
Adjusts the view in the window so that the element given by index is displayed at the top of the window.

insert(index, *elements)
Inserts zero or more new elements in the list just before the element given by index. If index is specified as END then the new elements are added to the end of the list. Returns None.

nearest(y)
Given a y-coordinate within the listbox window, this method returns the index of the (visible) listbox element nearest to that y-coordinate.