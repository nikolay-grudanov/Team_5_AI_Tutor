---
source_image: page_560.png
page_number: 560
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.68
tokens: 8511
characters: 3252
timestamp: 2025-12-24T00:47:56.638086
finish_reason: stop
---

tag_add(tagName, index1, index2=None)
Associates the tag tagName with all of the characters starting with index1 and ending just before index2 (the character at index2 isn’t tagged). A single method may contain any number of index1index2 pairs. If the last index2 is omitted then the single character at index1 is tagged. If there are no characters in the specified range (e.g. index1 is past the end of the file or index2 is less than or equal to index1) then the command has no effect.

tag_bind(tagName, sequence, function, add=None)
Associates function with the tag given by tagName. Whenever the event sequence given by sequence occurs for a character that has been tagged with tagName, the function will be invoked.
This widget command is similar to the bind method except that it operates on characters in a text rather than entire widgets.
If all arguments are specified then a new binding is created, replacing any existing binding for the same sequence and tagName (if the first character of function is + then function augments an existing binding rather than replacing it). In this case the return value is an empty string. If function is omitted then the command returns the function associated with tagName and sequence (an error occurs if there is no such binding).
If both function and sequence are omitted then the command returns a list of all the sequences for which bindings have been defined for tagName.
The only events for which bindings may be specified are those related to the mouse and keyboard (such as Enter, Leave, ButtonPress, Motion, and KeyPress) or virtual events. Event bindings for a text widget use the CURRENT mark. An Enter event triggers for a tag when the tag first becomes present on the current character, and a Leave event triggers for a tag when it ceases to be present on the current character. Enter and Leave events can happen either because the CURRENT mark moved or because the character at that position changed.
Note that these events are different than Enter and Leave events for windows. Mouse and keyboard events are directed to the current character. If a virtual event is used in a binding, that binding can trigger only if the virtual event is defined by an underlying mouse-related or keyboard-related event. It is possible for the current character to have multiple tags, and for each of them to have a binding for a particular event sequence. When this occurs, one binding is invoked for each tag, in order from lowest priority to highest priority.
If there are multiple matching bindings for a single tag, then the most specific binding is chosen. The tag bindings will be invoked first, followed by general bindings.

tag_cget(tagName, option)
Returns the current value of the option named option associated with the tag given by tagName. option may have any of the values accepted by tag_configure.

tag_configure(tagName, options...)
This command is similar to the configure_widget method except that it modifies options associated with the tag given by tagName instead of modifying options for the overall text widget. If no option is specified, the command returns a dictionary describing all of the available options for tagName. If option is specified with no value, then the command