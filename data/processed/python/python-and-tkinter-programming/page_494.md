---
source_image: page_494.png
page_number: 494
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.26
tokens: 8457
characters: 2202
timestamp: 2025-12-24T00:45:43.079936
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>stipple</td>
    <td>Indicates that the arc should be filled in a stipple pattern; bitmap specifies the stipple pattern to use.</td>
    <td>bitmap</td>
    <td>'gray25'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>style</td>
    <td>Specifies how to draw the arc. If type is PIESLICE (the default) then the arc’s region is defined by a section of the oval’s perimeter plus two line segments, one each between the center of the oval and each end of the perimeter section. If type is CHORD then the arc’s region is defined by a section of the oval’s perimeter plus a single line segment connecting the two end points of the perimeter section. If type is ARC then the arc’s region consists of a section of the perimeter alone. In this last case the fill option is ignored.</td>
    <td>constant</td>
    <td>CHORD 'arc'</td>
    <td>PIESLICE</td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item.</td>
    <td>tuple</td>
    <td>('tag1', 'arc')</td>
    <td>None</td>
  </tr>
</table>

Methods

create_arc(x0, y0, x1, y1, *options)
The arguments x0, y0, x1, and y1 give the coordinates of two diagonally opposite corners of a rectangular region enclosing the oval that defines the arc. After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure method calls to change the item’s configuration.

delete(item)
Deletes an arc item.

coords(item, x0, y0, x1, y1)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more arc items.