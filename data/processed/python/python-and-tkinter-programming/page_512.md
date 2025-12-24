---
source_image: page_512.png
page_number: 512
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.69
tokens: 8342
characters: 2041
timestamp: 2025-12-24T00:46:13.695566
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
    <td>show</td>
    <td>If this option is specified, then the true contents of the entry are not displayed in the window. Instead, each character in the entry’s value will be displayed as the first character in the value of this option, such as *. This is useful, for example, if the entry is to be used to enter a password. If characters in the entry are selected and copied elsewhere, the information copied will be what is displayed, not the true contents of the entry.</td>
    <td>character</td>
    <td>"*"</td>
    <td></td>
  </tr>
</table>

Methods

delete(first, last=None)
Deletes one or more elements of the entry. first is the index of the first character to delete, and last is the index of the character just after the last one to delete. If last isn’t specified it defaults to first+1, meaning a single character is deleted. This method returns None.

get()
Returns the entry’s string.

icursor(index)
Arranges for the insertion cursor to be displayed just before the character given by index. Returns None.

index(index)
Adjusts the view in the window so that the character given by index is displayed at the left edge of the window.

insert(index, string)
Inserts the characters of string just before the character indicated by index. Returns None.

scan_dragto(x)
Computes the difference between its x argument and the x argument to the last scan_mark method call for the widget. It then adjusts the view left or right by 10 times the difference in x-coordinates. This command is typically associated with mouse motion events in the widget, to produce the effect of dragging the entry at high speed through the window. The return value is an empty string.

scan_mark(x)
Records x and the current view in the entry window; it is used in conjunction with later scan_dragto method. Typically this command is associated with a mouse button press in the widget. It returns an empty string.