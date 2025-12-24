---
source_image: page_558.png
page_number: 558
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.92
tokens: 8439
characters: 2865
timestamp: 2025-12-24T00:47:41.522086
finish_reason: stop
---

dlineinfo(index)
Returns a tuple with five elements describing the area occupied by the display line containing index. The first two elements of the list give the x and y coordinates of the upper-left corner of the area occupied by the line, the third and fourth elements give the width and height of the area, and the fifth element gives the position of the baseline for the line, measured down from the top of the area. All of this information is measured in pixels.

If the current wrap mode is None and the line extends beyond the boundaries of the window, the area returned reflects the entire area of the line, including the portions that are out of the window. If the line is shorter than the full width of the window then the area returned reflects just the portion of the line that is occupied by characters and embedded windows. If the display line containing index is not visible on the screen then the return value is an empty list.

get(index1, index2=None)
Returns a range of characters from the text. The return value will be all the characters in the text starting with the one whose index is index1 and ending just before the one whose index is index2 (the character at index2 will not be returned). If index2 is omitted then the single character at index1 is returned. If there are no characters in the specified range (e.g. index1 is past the end of the file or index2 is less than or equal to index1) then an empty string is returned. If the specified range contains embedded windows, no information about them is included in the returned string.

image_cget(index, option)
Returns the value of a configuration option for an embedded image. index identifies the embedded image, and option specifies a particular configuration option.

image_configure(index, options...)
Queries or modifies the configuration options for an embedded image. If no option is specified, returns a dictionary describing all of the available options for the embedded image at index. If option is specified with no value, then the method returns a dictionary describing the one named option (this dictionary will be identical to the corresponding sublist of the value returned if no option is specified).

If one or more option-value pairs are specified, then the command modifies the given option(s) to have the given value(s); in this case the command returns an empty string.

image_names()
Returns a tuple whose elements are the names of all windows currently embedded in window.

index(index)
Returns the position corresponding to index in the form line.char where line is the line number and char is the character number.

insert(index, chars, tagList, chars, tagList...)
Inserts all of the chars arguments just before the character at index. If index refers to the end of the text (the character after the last new line) then the new text is inserted just before