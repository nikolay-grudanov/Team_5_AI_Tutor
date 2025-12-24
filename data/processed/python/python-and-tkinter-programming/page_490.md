---
source_image: page_490.png
page_number: 490
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.87
tokens: 8480
characters: 2671
timestamp: 2025-12-24T00:45:37.175141
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Value (type)</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>y</td>
    <td>position (integer)</td>
    <td>Specifies the y-coordinate of the top edge of the area of the canvas that is to be printed, in canvas coordinates, not window coordinates. Defaults to the coordinate of the top edge of the window.</td>
  </tr>
</table>

scale(tagOrId, xOrigin, yOrigin, xSc)
Rescale all of the items given by tagOrId in canvas coordinate space. XOrigin and yOrigin identify the origin for the scaling operation and xScale and yScale identify the scale factors for x- and y-coordinates, respectively (a scale factor of 1.0 implies no change to that coordinate). For each of the points defining each item, the x-coordinate is adjusted to change the distance from xOrigin by a factor of xScale. Similarly, each y-coordinate is adjusted to change the distance from yOrigin by a factor of yScale. This method returns None.

scan_dragto(x, y)
Computes the difference between its x and y arguments (which are typically mouse coordinates) and the x and y arguments to the last scan_mark call for the widget. It then adjusts the view by 10 times the difference in coordinates. This method is typically associated with mouse motion events in the widget, to produce the effect of dragging the canvas at high speed through its window. The return value is an empty string.

scan_mark(x, y)
Records x and y and the canvas’s current view; used in conjunction with later scan_dragto calls. Typically this method is associated with a mouse button press in the widget and x and y are the coordinates of the mouse. It returns None.

select_adjust(tagOrId, index)
Locates the end of the selection in tagOrId nearest to the character given by index, and adjusts that end of the selection to be at index (i.e. including but not going beyond index). The other end of the selection is made the anchor point for future select_to calls. If the selection isn’t currently in tagOrId then this method behaves the same as the select_to widget method. Returns None.

select_clear()
Clears the selection if it is in this widget. If the selection isn’t in this widget then the method has no effect. Returns None.

select_from(tagOrId, index)
Sets the selection anchor point for the widget to be just before the character given by index in the item given by tagOrId. This method doesn’t change the selection; it just sets the fixed end of the selection for future select_to calls. Returns None.

select_item()
Returns the ID of the selected item, if the selection is in an item in this canvas. If the selection is not in this canvas then an empty string is returned.