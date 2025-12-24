---
source_image: page_500.png
page_number: 500
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.19
tokens: 8526
characters: 2370
timestamp: 2025-12-24T00:45:57.266204
finish_reason: stop
---

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

Options specific to Oval

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>outline</td>
    <td>color specifies a color to use for drawing the oval’s outline. If color is an empty string then no outline will be drawn for the oval.</td>
    <td>color</td>
    <td>RED<br>'black'</td>
    <td>'black'</td>
  </tr>
  <tr>
    <td>stipple</td>
    <td>Indicates that the oval should be filled in a stipple pattern; bitmap specifies the stipple pattern to use. If the fill option hasn’t been specified then this option has no effect. If bitmap is an empty string (the default), then filling is done in a solid fashion.</td>
    <td>bitmap</td>
    <td>'gray25'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', 'oval')</td>
    <td>None</td>
  </tr>
</table>

Methods

create_oval(x0, y0, x1, y1, *options)
The arguments x0, y0, x1, and y1 give the coordinates of two diagonally opposite corners of a rectangular region enclosing the oval. The oval will include the top and left edges of the rectangle, not the lower or right edges. If the region is square then the resulting oval is circular; otherwise it is elongated in shape. After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure method calls to change the item’s configuration.

delete(item)
Deletes an oval item.

coords(item, x0, y0, x1, y1)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more oval items.