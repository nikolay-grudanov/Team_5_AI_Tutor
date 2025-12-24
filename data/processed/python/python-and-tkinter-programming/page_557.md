---
source_image: page_557.png
page_number: 557
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.19
tokens: 8513
characters: 2858
timestamp: 2025-12-24T00:47:47.796426
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>yscrollcommand</td>
    <td>Specifies the prefix for a command used to function communicate with vertical scrollbars. This option is treated in the same way as the xScrollCommand option, except that it is used for vertical scrollbars and is provided by widgets that support vertical scrolling. See the description of xScrollCommand for details on how this option is used.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

Methods

bbox(index)
Returns a list of four elements describing the screen area of the character given by index. The first two elements of the list give the x and y coordinates of the upper-left corner of the area occupied by the character, and the last two elements give the width and height of the area. If the character is only partially visible on the screen, then the return value reflects just the visible part. If the character is not visible on the screen then the return value is an empty list.

compare(index1, op, index2)
Compares the indices given by index1 and index2 according to the relational operator given by op, and returns TRUE if the relationship is satisfied and FALSE if it isn’t. op must be one of the operators <, <=, ==, >=, >, or !=. If op is == then TRUE is returned if the two indices refer to the same character; if op is < then TRUE is returned if index1 refers to an earlier character in the text than index2, and so on.

debug(boolean=None)
If boolean is specified, then it must have one of the true or false values accepted by Tcl_GetBoolean. If the value is a true one then internal consistency checks will be turned on in the B-tree code associated with text widgets. If boolean has a false value then the debugging checks will be turned off. In either case the method returns a boolean indicating whether debug is enabled. If boolean is not specified then the method returns on or off to indicate whether or not debugging is turned on. There is a single debugging switch shared by all text widgets: turning debugging on or off in any widget turns it on or off for all widgets. For widgets with large amounts of text, the consistency checks may cause a noticeable slowdown.

delete(index1, index2=None)
Deletes a range of characters from the text. If both index1 and index2 are specified, then deletes all the characters starting with the one given by index1 and stopping just before index2 (i.e. the character at index2 is not deleted). If index2 doesn’t specify a position later in the text than index1 then no characters are deleted. If index2 isn’t specified then the single character at index1 is deleted.
It is not allowable to delete characters in a way that would leave the text without a newline as the last character. Returns None.