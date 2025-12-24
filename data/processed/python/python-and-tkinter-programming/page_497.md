---
source_image: page_497.png
page_number: 497
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.75
tokens: 8167
characters: 1244
timestamp: 2025-12-24T00:45:32.463396
finish_reason: stop
---

Methods

create_image(x, y, *options)
The arguments x and y specify the coordinates of a point used to position the image on the display (using the anchor option). After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure calls to change the item’s configuration.

delete(item)
Deletes an image item.

coords(item, x, y)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more image items.

Canvas line

Description
Items of type line appear on the display as one or more connected line segments or curves.

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
    <td>"black"</td>
  </tr>
  <tr>
    <td>width</td>
    <td>1</td>
  </tr>
</table>