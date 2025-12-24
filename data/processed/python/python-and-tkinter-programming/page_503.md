---
source_image: page_503.png
page_number: 503
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.62
tokens: 8472
characters: 2339
timestamp: 2025-12-24T00:46:04.133648
finish_reason: stop
---

Options specific to Rectangle

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
    <td>color specifies a color to use for drawing the rectangle’s outline. If color is an empty string then no outline will be drawn for the rectangle.</td>
    <td>color</td>
    <td>RED<br>'black'</td>
    <td>'black'</td>
  </tr>
  <tr>
    <td>stipple</td>
    <td>Indicates that the rectangle should be filled in a stipple pattern; bitmap specifies the stipple pattern to use. If the fill option hasn’t been specified then this option has no effect. If bitmap is an empty string (the default), then filling is done in a solid fashion.</td>
    <td>bitmap</td>
    <td>'gray25'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', 'rect')</td>
    <td>None</td>
  </tr>
</table>

Methods

create_rectangle(x0, y0, x1, y1, *options)
The arguments x0, y0, x1, and y1 give the coordinates of two diagonally opposite corners of the rectangle (the rectangle will include its upper and left edges but not its lower or right edges). After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure method calls to change the item’s configuration.

delete(item)
Deletes a rectangle item.

coords(item, x0, y0, x1, y1)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more rectangle items.

Canvas text

Description
A text item displays a string of characters on the screen in one or more lines. Text items support indexing and selection, along with the following text-related canvas widget methods: dchars, focus, icursor, index, insert, and select.