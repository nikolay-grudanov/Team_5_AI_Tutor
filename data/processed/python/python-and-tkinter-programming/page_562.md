---
source_image: page_562.png
page_number: 562
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.37
tokens: 8421
characters: 2653
timestamp: 2025-12-24T00:47:47.827123
finish_reason: stop
---

tag_raise(tagName, aboveThis=None)
Changes the priority of tag tagName so that it is just higher in priority than the tag whose name is aboveThis. If aboveThis is omitted, then tagName’s priority is changed to make it the highest priority of all tags.

tag_ranges(tagName)
Returns a tuple describing all of the ranges of text that have been tagged with tagName. The first two elements of the tuple describe the first tagged range in the text, the next two elements describe the second range, and so on. The first element of each pair contains the index of the first character of the range, and the second element of the pair contains the index of the character just after the last one in the range. If no characters are tagged with tag then an empty string is returned.

tag_remove(tagName, index1, index2=None)
Removes the tag tagName from all of the characters starting at index1 and ending just before index2 (the character at index2 isn’t affected). A single call may contain any number of index1index2 pairs. If the last index2 is omitted then the single character at index1 is tagged. If there are no characters in the specified range (e.g. index1 is past the end of the file or index2 is less than or equal to index1) then the method has no effect. This method returns None.

tag_unbind(tagName, sequence, funcid=None)
Removes the association of the event sequence with the event handler funcId for all the items given by tagOrId. If funcId is supplied the handler will be destroyed.

tk_textBackspace()
tk_textIndexCloser(a, b, c)
tk_textResetAnchor(index)
tk_textSelectTo(index)

These four methods are really only useful if you are writing your own event handling for text. Their function is to set the text appearance as if the default actions had occurred. They may also be useful in simulating user interaction with a GUI.

window_cget(index, option)
Returns the value of a configuration option for an embedded window. index identifies the embedded window, and option specifies a particular configuration option.

window_configure(index, options...)
Queries or modifies the configuration options for an embedded window. If no option is specified, it returns a dictionary describing all of the available options for the embedded window at index. If option is specified with no value, then the method returns a dictionary describing the one named option (this dictionary will be identical to the corresponding dictionary of the value returned if no option is specified).

If one or more option-value pairs are specified, then the method modifies the given option(s) to have the given value(s); in this case the method returns an empty string.