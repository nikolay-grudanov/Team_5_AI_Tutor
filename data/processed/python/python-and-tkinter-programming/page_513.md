---
source_image: page_513.png
page_number: 513
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.81
tokens: 8353
characters: 2351
timestamp: 2025-12-24T00:46:13.799209
finish_reason: stop
---

selection_adjust(index)
Locates the end of the selection nearest to the character given by index, and adjusts that end of the selection to be at index (meaning including but not going beyond index). The other end of the selection is made the anchor point for future select to commands. If the selection isn’t currently in the entry, then a new selection is created to include the characters between index and the most recent selection anchor point, inclusive. Returns an empty string.

selection_clear()
Clears the selection if it is in this widget. If the selection isn’t in this widget then the method has no effect. Returns None.

selection_from(index)
Sets the selection anchor point to just before the character given by index. Doesn’t change the selection. Returns None.

selection_present()
Returns TRUE if characters are selected in the entry, FALSE if nothing is selected.

selection_range(start, end)
Sets the selection to include the characters starting with the one indexed by start and ending with the one just before end. If end refers to the same character as start or an earlier one, then the entry’s selection is cleared.

selection_to(index)
If index is before the anchor point, sets the selection to the characters from index up to but not including the anchor point. If index is the same as the anchor point, does nothing. If index is after the anchor point, sets the selection to the characters from the anchor point up to but not including index. The anchor point is determined by the most recent select from or select adjust command in this widget. If the selection isn’t in this widget then a new selection is created using the most recent anchor point specified for the widget. Returns None.

xview(index)
Adjusts the view in the window so that the character given by index is displayed at the left edge of the window.

xview_moveto(fraction)
Adjusts the view in the window so that the character fraction of the way through the text appears at the left edge of the window. fraction must be a fraction between 0 and 1.

xview_scroll(number, what)
Shifts the view in the window left or right according to number and what. number must be an integer. what must be either UNITS or PAGES or an abbreviation of one of these. If what is UNITS, the view adjusts left or right by number average-width characters on the display; if it is