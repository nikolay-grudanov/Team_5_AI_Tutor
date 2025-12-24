---
source_image: page_502.png
page_number: 502
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.48
tokens: 8222
characters: 1438
timestamp: 2025-12-24T00:45:46.936638
finish_reason: stop
---

Methods

create_polygon(x0, y0, x1, y1, ..., xn, yn, *options)
The arguments x0 through yn specify the coordinates for three or more points that define a closed polygon. The first and last points may be the same; whether they are or not, Tk will draw the polygon as a closed polygon. After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure method calls to change the item’s configuration.

delete(item)
Deletes a polygon item.

coords(item, x0, y0, x1, y1, ..., xn, yn)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more polygon items.

Canvas rectangle

Description
Items of type rectangle appear as rectangular regions on the display. Each rectangle may have an outline, a fill, or both.

Inheritance
Inherits from Widget, Canvas.

Shared options

<table>
  <tr>
    <th>Option</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>fill</td>
    <td>transparent</td>
  </tr>
  <tr>
    <td>width</td>
    <td>1</td>
  </tr>
</table>