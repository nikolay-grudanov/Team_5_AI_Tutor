---
source_image: page_496.png
page_number: 496
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.92
tokens: 8263
characters: 1399
timestamp: 2025-12-24T00:45:32.904213
finish_reason: stop
---

coords(item, x, y)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more bitmap items.

Canvas image

Description
Items of type image are used to display images on a canvas.

Inheritance
Inherits from Widget, Canvas.

Shared options

<table>
  <tr>
    <th>Option</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>anchor</td>
    <td>CENTER</td>
  </tr>
</table>

Options specific to Image

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>image</td>
    <td>Specifies the name of the image to display in the item. This image must have been created previously with the create_image method.</td>
    <td>image</td>
    <td>'scene.gif'</td>
    <td></td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', 'img')</td>
    <td>None</td>
  </tr>
</table>