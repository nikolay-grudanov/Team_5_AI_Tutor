---
source_image: page_487.png
page_number: 487
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.60
tokens: 8478
characters: 2853
timestamp: 2025-12-24T00:45:35.285570
finish_reason: stop
---

Once the focus has been set to an item, the item will display the insertion cursor and all keyboard events will be directed to that item. The focus item within a canvas and the focus window on the screen (set with the focus method) are totally independent; a given item doesn’t actually have the input focus unless (a) its canvas is the focus window and (b) the item is the focus item within the canvas. In most cases it is advisable to follow the focus widget method with the focus method to set the focus window to the canvas (if it wasn’t there already).

gettags(tagOrId)
Returns a list whose elements are the tags associated with the item given by tagOrId. If tagOrId refers to more than one item, then the tags are returned from the first such item in the display list. If tagOrId doesn’t refer to any items, or if the item doesn’t contain tags, then an empty string is returned.

icursor(tagOrId, index)
Sets the position of the insertion cursor for the item(s) given by tagOrId to just before the character whose position is given by index. If some or all of the items given by tagOrId don’t support an insertion cursor then this method has no effect on them.
Note: The insertion cursor is only displayed in an item if that item currently has the keyboard focus (see the widget method focus, below), but the cursor position may be set even when the item doesn’t have the focus. This method returns None.

index(tagOrId, Index)
Returns an integer giving the numerical index within tagOrId corresponding to index. index gives a textual description of the desired position (such as end). The return value is guaranteed to lie between 0 and the number of characters within the item, inclusive. If tagOrId refers to multiple items, then the index is processed in the first of these items that supports indexing operations (in display list order).

insert(tagOrId, beforeThis, string)
For each of the items given by tagOrId, if the item supports text insertion then string is inserted into the item’s text just before the character whose index is beforeThis. This method returns None.

itemcget(tagOrId, option)
Returns the current value of the configuration option for the item given by tagOrId whose name is option. This method is similar to the cget widget method except that it applies to a particular item rather than the widget as a whole. option may have any of the values accepted by the create widget method when the item was created. If tagOrId is a tag that refers to more than one item, the first (lowest) such item is used.

itemconfigure(tagOrId, options)
This method is similar to the configure widget method except that it modifies item-specific options for the items given by tagOrId instead of modifying options for the overall canvas widget. If no option is specified, it returns a dictionary describing all of the available options