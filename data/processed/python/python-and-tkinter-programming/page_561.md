---
source_image: page_561.png
page_number: 561
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.83
tokens: 8428
characters: 2707
timestamp: 2025-12-24T00:47:47.866040
finish_reason: stop
---

returns a dictionary describing the one named option (this dictionary will be identical to the corresponding dictionary of the value returned if no option is specified).

If one or more option-value pairs are specified, then the method modifies the given option(s) to have the given value(s) in tagName; in this case the command returns an empty string.

tag_delete(*tagNames)
Deletes all tag information for each of the tagName arguments. The method removes the tags from all characters in the file and also deletes any other information associated with the tags, such as bindings and display information.

tag_lower(tagName, belowThis=None)
Changes the priority of tag tagName so that it is just lower in priority than the tag whose name is belowThis. If belowThis is omitted, then tagName’s priority is changed to make it the lowest priority of all tags.

tag_names(index=None)
Returns a tuple whose elements are the names of all the tags that are active at the character position given by index. If index is omitted, then the return value will describe all of the tags that exist for the text (this includes all tags that have been named in a tag widget method call but haven’t been deleted by a tag_delete method call, even if no characters are currently marked with the tag). The tuple will be sorted in order from lowest priority to highest priority.

tag_nextrange(tagName, index1, index2=None)
Searches the text for a range of characters tagged with tagName where the first character of the range is no earlier than the character at index1 and no later than the character just before index2 (a range starting at index2 will not be considered). If several matching ranges exist, the first one is chosen. The method’s return value is a list containing two elements, which are the index of the first character of the range and the index of the character just after the last one in the range.
If no matching range is found then the return value is an empty string. If index2 is not given then it defaults to the end of the text.

tag_prevrange(tagName, index1, index2=None)
Searches the text for a range of characters tagged with tagName where the first character of the range is before the character at index1 and no earlier than the character at index2 (a range starting at index2 will be considered). If several matching ranges exist, the one closest to index1 is chosen. The method’s return value is a list containing two elements, which are the index of the first character of the range and the index of the character just after the last one in the range.
If no matching range is found then the return value is an empty string. If index2 is not given then it defaults to the beginning of the text.