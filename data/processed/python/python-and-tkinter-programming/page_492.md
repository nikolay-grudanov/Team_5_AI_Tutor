---
source_image: page_492.png
page_number: 492
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.98
tokens: 8494
characters: 2734
timestamp: 2025-12-24T00:45:40.715003
finish_reason: stop
---

lower methods, not the raise and lower widget methods for canvases. This method returns None.

tag_raise(tagOrId, aboveThis)
Moves all of the items given by tagOrId to a new position in the display list just after the item given by aboveThis. If tagOrId refers to more than one item then all are moved but the relative order of the moved items will not be changed. aboveThis is a tag or ID; if it refers to more than one item then the last (topmost) of these items in the display list is used as the destination location for the moved items.

Note: This method has no effect on window items. Window items always obscure other item types, and the stacking order of window items is determined by the raise and lower methods, not the raise and lower widget methods for canvases. This method returns None.

tag_unbind(tagOrId, sequence, funcId=None)
Removes the association of the event sequence with the event handler funcId for all the items given by tagOrId. If funcId is supplied the handler will be destroyed.

type(tagOrId)
Returns the type of the item given by tagOrId, such as rectangle or text. If tagOrId refers to more than one item, then the type of the first item in the display list is returned. If tagOrId doesn’t refer to any items at all then an empty string is returned.

xview_moveto(fraction)
Adjusts the view in the window so that fraction of the total width of the canvas is off-screen to the left. Fraction is a fraction between 0 and 1.

xview_scroll(number, what)
This command shifts the view in the window left or right according to number and what. number must be an integer. what must be either UNITS or PAGES. If what is UNITS, the view adjusts left or right in units of the xScrollIncrement option, if it is greater than zero, or in units of one-tenth the window’s width otherwise. If what is PAGES then the view adjusts in units of nine-tenths the window’s width. If number is negative, information farther to the left becomes visible; if it is positive, then information farther to the right becomes visible.

yview_moveto(fraction)
Adjusts the view in the window so that fraction of the canvas’s area is off-screen to the top. fraction is a fraction between 0 and 1.

yview_scroll(number, what)
Adjusts the view in the window up or down according to number and what. number must be an integer. what must be either UNITS or PAGES. If what is UNITS, the view adjusts up or down in units of the yScrollIncrement option, if it is greater than zero, or in units of one-tenth the window’s height otherwise. If what is PAGES then the view adjusts in units of nine-tenths the window’s height. If number is negative then higher information becomes visible; if it is positive then lower information becomes visible.