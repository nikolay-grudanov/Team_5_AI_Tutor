---
source_image: page_484.png
page_number: 484
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.72
tokens: 8573
characters: 2935
timestamp: 2025-12-24T00:45:26.204802
finish_reason: stop
---

addtag_closest(newtag, x, y, halo=None, start=None)
Adds newtag to the item closest to the point given by x and y. If more than one item is at the same closest distance (meaning two items overlap the point), then the top-most of these items (the last one in the display list) is used. If halo is specified, then it must be a non-negative value. Any item closer than halo to the point is considered to overlap it. The start argument may be used to step circularly through all the closest items. If start is specified, it names an item using a tag or id (if by tag, it selects the first item in the display list with the given tag). Instead of selecting the top-most closest item, this form will select the top-most closest item that is below start in the display list; if no such item exists, then the selection behaves as if the start argument had not been specified.

addtag_enclosed(newtag, x1, y1, x2, y2)
Adds newtag to all the items completely enclosed within the rectangular region given by x1, y1, x2, and y2. x1 must be no greater than x2 and y1 must be no greater than y2.

addtag_overlapping(newtag, x1, y1, x2, y2)
Adds newtag to all the items that overlap or are enclosed within the rectangular region given by x1, y1, x2, and y2. x1 must be no greater than x2 and y1 must be no greater than y2.

addtag_withtag(newtag, tagOrId)
Adds newtag to all the items given by tagOrId.

bbox(tagOrId), bbox()
Returns a tuple with four elements giving an approximate bounding box for all the items named by the tagOrId arguments. The tuple is in the order x1, y1, x2, y2 such that the drawn areas of all the named elements are within the region bounded by x1 on the left, x2 on the right, y1 on the top, and y2 on the bottom. The return value may overestimate the actual bounding box by a few pixels. If no items match any of the tagOrId arguments or if the matching items have empty bounding boxes (i.e. they have nothing to display) then an empty string is returned.

canvasx(screenx, gridspacing=None)
Given a window x-coordinate in the canvas screenx, this method returns the canvas x-coordinate that is displayed at that location. If gridspacing is specified, then the canvas coordinate is rounded to the nearest multiple of gridspacing units.

canvasy(screeny, gridspacing=None)
Given a window y-coordinate in the canvas screeny, this method returns the canvas y-coordinate that is displayed at that location. If gridspacing is specified, then the canvas coordinate is rounded to the nearest multiple of gridspacing units.

coords(tagOrId, x0, y0, x1, y1, ..., xn, yn)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this method returns a tuple whose elements are the coordinates of the item named by tagOrId. If coordinates are specified, then they replace the current coordinates for the named item. If tagOrId refers to multiple items, then the first one in the display list is used.