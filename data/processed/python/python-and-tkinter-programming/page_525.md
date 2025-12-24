---
source_image: page_525.png
page_number: 525
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.88
tokens: 8378
characters: 2400
timestamp: 2025-12-24T00:46:35.534603
finish_reason: stop
---

scan_dragto(x, y)
This method computes the difference between its x and y arguments (which are typically mouse coordinates) and the x and y arguments to the last scan_mark call for the widget. It then adjusts the view by 10 times the difference in coordinates. This method is typically associated with mouse motion events in the widget, to produce the effect of dragging the list at high speed through its window. The return value is an empty string.

scan_mark(x, y)
Records x and y and the listbox’s current view; used in conjunction with later scan_dragto calls. Typically this method is associated with a mouse button press in the widget and x and y are the coordinates of the mouse. It returns None.

see(index)
Adjusts the view in the listbox so that the element given by index is visible. If the element is already visible then the method has no effect; if the element is near one edge of the window then the listbox scrolls to bring the element into view at the edge; otherwise the listbox scrolls to center the element.

selection_anchor(index)
Sets the selection anchor to the element given by index.

selection_clear(first, last=None)
If any of the elements between first and last (inclusive) are selected, they are deselected. The selection state is not changed for elements outside this range.

selection_includes(index)
Returns TRUE if the element indicated by index is currently selected, FALSE if it isn’t.

selection_set(first, last=None)
Selects all of the elements in the range between first and last, inclusive, without affecting the selection state of elements outside that range.

size()
Returns an integer indicating the total number of elements in the listbox.

xview_moveto(fraction)
Adjusts the view in the window so that fraction of the the total width of the listbox is off-screen to the left. fraction is a fraction between 0 and 1.

xview_scroll(number, what)
This command shifts the view in the window left or right according to number and what. number must be an integer. what must be either UNITS or PAGES or an abbreviation of one of these. If what is UNITS, the view adjusts left or right by number character units (the width of the 0 character) on the display; if it is PAGES then the view adjusts by number screenfuls. If number is negative then characters farther to the left become visible; if it is positive then characters farther to the right become visible.