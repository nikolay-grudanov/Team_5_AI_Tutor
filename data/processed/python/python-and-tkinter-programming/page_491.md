---
source_image: page_491.png
page_number: 491
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.90
tokens: 8627
characters: 3700
timestamp: 2025-12-24T00:45:46.551518
finish_reason: stop
---

select_to(tagOrId, index)
Sets the selection to consist of those characters of tagOrId between the selection anchor point and index. The new selection will include the character given by index; it will include the character given by the anchor point only if index is greater than or equal to the anchor point. The anchor point is determined by the most recent select_adjust or select_from call for this widget. If the selection anchor point for the widget isn’t currently in tagOrId, then it is set to the same character given by index. Returns None.

tag_bind(tagOrId, sequence=None, function=None, add=None)
Associates function with all the items given by tagOrId so that whenever the event sequence given by sequence occurs for one of the items, the function will be invoked. This widget method is similar to the bind method except that it operates on items in a canvas rather than entire widgets. If all arguments are specified then a new binding is created, replacing any existing binding for the same sequence and tagOrId (if the first character of function is + then function augments an existing binding rather than replacing it). In this case the return value is an empty string. If function is omitted then the method returns the function associated with tagOrId and sequence (an error occurs if there is no such binding). If both function and sequence are omitted then the method returns a list of all the sequences for which bindings have been defined for tagOrId.

The only events for which bindings may be specified are those related to the mouse and keyboard (such as Enter, Leave, ButtonPress, Motion, and KeyPress) or virtual events. Enter and Leave events trigger for an item when it becomes the current item or ceases to be the current item; note that these events are different than Enter and Leave events for windows.

Mouse-related events are directed to the current item, if any. Keyboard related events are directed to the focus item, if any. If a virtual event is used in a binding, that binding can trigger only if the virtual event is defined by an underlying mouse-related or keyboard-related event. It is possible for multiple bindings to match a particular event. This could occur, for example, if one binding is associated with the item’s ID and another is associated with one of the item’s tags. When this occurs, all of the matching bindings are invoked. A binding associated with the ALL tag is invoked first, followed by one binding for each of the item’s tags (in order), followed by a binding associated with the item’s ID. If there are multiple matching bindings for a single tag, then only the most specific binding is invoked.

A “break” string returned by an event handler terminates that handler and skips any remaining handlers for the event, just as for the bind method. If bindings have been created for a canvas window using the bind method, then they are invoked in addition to bindings created for the canvas’s items using the bind widget call. The bindings for items will be invoked before any of the bindings for the window as a whole.

tag_lower(tagOrId, belowThis)
Moves all of the items given by tagOrId to a new position in the display list just before the item given by belowThis. If tagOrId refers to more than one item then all are moved but the relative order of the moved items will not be changed. belowThis is a tag or ID; if it refers to more than one item then the first (lowest) of these items in the display list is used as the destination location for the moved items.

Note: This method has no effect on window items. Window items always obscure other item types, and the stacking order of window items is determined by the raise and