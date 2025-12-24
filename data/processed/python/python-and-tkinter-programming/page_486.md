---
source_image: page_486.png
page_number: 486
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.21
tokens: 8495
characters: 2602
timestamp: 2025-12-24T00:45:26.019894
finish_reason: stop
---

find_above(tagOrId)
Finds the item just after (above) the one given by tagOrId in the display list. If tagOrId denotes more than one item, then the last (top-most) of these items in the display list is used.

find_all()
Returns a list containing the identities of all the items in the canvas.

find_below(tagOrId)
Returns the item just before (below) the one given by tagOrId in the display list. If tagOrId denotes more than one item, then the first (lowest) of these items in the display list is used.

find_closest(x, y, halo=None, start=None)
Returns the item closest to the point given by x and y. If more than one item is at the same closest distance (meaning two items overlap the point), then the top-most of these items (the last one in the display list) is used. If halo is specified, then it must be a non-negative value. Any item closer than halo to the point is considered to overlap it. The start argument may be used to step circularly through all the closest items. If start is specified, it names an item using a tag or ID (if by tag, it selects the first item in the display list with the given tag). Instead of selecting the top-most closest item, this form will select the top-most closest item that is below start in the display list; if no such item exists, then the selection behaves as if the start argument had not been specified. This method will always return an item if there are one or more items on the canvas.

find_enclosed(x1, y1, x2, y2)
Returns a list containing the identities of all the items completely enclosed within the rectangular region given by x1, y1, x2, and y2. x1 must be no greater then x2 and y1 must be no greater than y2.

find_overlapping(x1, y1, x2, y2)
Returns a list containing the identities of all the items that overlap or are enclosed within the rectangular region given by x1, y1, x2, and y2. x1 must be no greater then x2 and y1 must be no greater than y2.

find_withtag(tagOrId)
Returns a list containing the identities of all the items given by tagOrId.

focus(tagOrId)
Sets the keyboard focus for the canvas widget to the item given by tagOrId. If tagOrId refers to several items, then the focus is set to the first such item in the display list that supports the insertion cursor. If tagOrId doesn’t refer to any items, or if none of them support the insertion cursor, then the focus isn’t changed. If tagOrId is an empty string, then the focus item is reset so that no item has the focus. If tagOrId is not specified then the method returns the ID for the item that currently has the focus, or an empty string if no item has the focus.