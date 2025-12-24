---
source_image: page_499.png
page_number: 499
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.55
tokens: 8367
characters: 1895
timestamp: 2025-12-24T00:45:46.960033
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
    <td>stipple</td>
    <td>Indicates that the line should be filled in a stipple pattern; bitmap specifies the stipple pattern to use, in any of the forms accepted by Tkinter (Tk_GetBitmap). If bitmap is an empty string (the default), then filling is done in a solid fashion.</td>
    <td>bitmap</td>
    <td>'gray25'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', 'line')</td>
    <td>None</td>
  </tr>
</table>

Methods

create_line(x0, y0, x1, y1, ..., xn, yn, *options)
The arguments x0 through yn give the coordinates for a series of two or more points that describe a series of connected line segments. After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure calls to change the item’s configuration.

delete(item)
Deletes a line item.

coords(item, x0, y0, x1, y1, ..., xn, yn)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more line items.

Canvas oval

Description
Items of type oval appear as circular or oval regions on the display. Each oval may have an outline, a fill, or both.

Inheritance
Inherits from Widget, Canvas.