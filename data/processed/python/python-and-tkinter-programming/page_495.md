---
source_image: page_495.png
page_number: 495
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.63
tokens: 8313
characters: 1538
timestamp: 2025-12-24T00:45:37.635362
finish_reason: stop
---

Canvas bitmap

Description
Items of type bitmap appear on the display as images with two colors, foreground and background.

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
  <tr>
    <td>background</td>
    <td>transparent</td>
  </tr>
  <tr>
    <td>foreground</td>
    <td>"black"</td>
  </tr>
</table>

Options specific to Bitmap

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>bitmap</td>
    <td>Specifies the bitmap to display in the item. bitmap may have any of the forms accepted by Tkinter (Tk_GetBitmap).</td>
    <td>bitmap</td>
    <td>'info'</td>
    <td></td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', None 'bit-map')</td>
    <td></td>
  </tr>
</table>

Methods

create_bitmap(x, y, *options)
The arguments x and y specify the coordinates of a point used to position the bitmap on the display (using the anchor option). After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure calls to change the item’s configuration.

delete(item)
Deletes a bitmap item