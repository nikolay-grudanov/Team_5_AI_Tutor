---
source_image: page_485.png
page_number: 485
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.23
tokens: 8259
characters: 1487
timestamp: 2025-12-24T00:45:15.935211
finish_reason: stop
---

The following methods create canvas *items* but are documented as separate “widgets” to allow their attributes and behavior to be addressed more fully, although they are not discrete widgets in reality.

**create_arc(*)**
See “Canvas Arc” on page 468.

**create_bitmap(*)**
See “Canvas Arc” on page 468.

**create_image(*)**
See “Canvas Arc” on page 468.

**create_line(*)**
See “Canvas line” on page 472.

**create_oval(*)**
See “Canvas Arc” on page 468.

**create_polygon(*)**
See “Canvas Arc” on page 468.

**create_rectangle(*)**
See “Canvas Arc” on page 468.

**create_text(*)**
See “Canvas Arc” on page 468.

**create_window(*)**
See “Canvas Arc” on page 468.

**dchars(tagOrId, first=0, last=first)**
For each item given by tagOrId, deletes the characters in the range given by first and last, inclusive. If some of the items given by tagOrId don’t support text operations, then they are ignored. first and last are indices of characters within the item(s) as described in INDICES above. If last is omitted, it defaults to first. This method returns None.

**delete(tagOrId)**
Deletes each of the items given by each tagOrId, and returns an empty string.

**dtag(tagOrId, tagToDelete)**
For each of the items given by tagOrId, deletes the tag given by tagToDelete from the list of those associated with the item. If an item doesn’t have the tag tagToDelete then the item is unaffected by the method. If tagToDelete is omitted then it defaults to tagOrId. This method returns None.