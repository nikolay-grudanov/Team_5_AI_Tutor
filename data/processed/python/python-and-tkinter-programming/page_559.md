---
source_image: page_559.png
page_number: 559
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.29
tokens: 8390
characters: 2479
timestamp: 2025-12-24T00:47:37.916880
finish_reason: stop
---

the last newline instead. If there is a single chars argument and no tagList, then the new text will receive any tags that are present on both the character before and the character after the insertion point; if a tag is present on only one of these characters then it will not be applied to the new text.

If tagList is specified then it consists of a list of tag names; the new characters will receive all of the tags in this list and no others, regardless of the tags present around the insertion point. If multiple chars-tagList argument pairs are present, they produce the same effect as if a separate insert widget method had been issued for each pair, in order. The last tagList argument may be omitted.

mark_gravity(markName, direction=None)
If direction is not specified, returns LEFT or RIGHT to indicate which of its adjacent characters markName is attached to. If direction is specified, it must be LEFT or RIGHT; the gravity of markName is set to the given value.

mark_names()
Returns a tuple whose elements are the names of all windows currently embedded in window.

mark_set(markName, index)
Sets the mark named markName to a position just before the character at index. If markName already exists, it is moved from its old position; if it doesn’t exist, a new mark is created.

mark_unset(mark)
Removes the mark corresponding to mark. The removed mark will not be usable in indices and will not be returned by future calls to mark_names calls. This method returns None.

scan_dragto(x, y)
Computes the difference between its x and y arguments and the x and y arguments to the last scan_mark call for the widget. It then adjusts the view by 10 times the difference in coordinates. This command is typically associated with mouse motion events in the widget, to produce the effect of dragging the text at high speed through the window. The return value is an empty string.

scan_mark(x, y)
Records x and y and the current view in the text window, for use in conjunction with later scan_dragto commands. Typically this command is associated with a mouse button press in the widget. It returns None.

see(index)
Adjusts the view in the window so that the character given by index is completely visible. If index is already visible then the method does nothing. If index is a short distance out of view, the method adjusts the view just enough to make index visible at the edge of the window. If index is far out of view, then the method centers index in the window.