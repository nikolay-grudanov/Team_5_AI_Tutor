---
source_image: page_505.png
page_number: 505
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.88
tokens: 8345
characters: 1678
timestamp: 2025-12-24T00:45:57.210693
finish_reason: stop
---

delete(item)
Deletes a text item.

coords(item, x0, y0)
Queries or modifies the coordinates that define an item. If no coordinates are specified, this command returns a list whose elements are the coordinates of the item named by item. If coordinates are specified, then they replace the current coordinates for the named item. If item refers to multiple items, then the first one in the display list is used.

itemconfigure(item, *options)
Modifies the options for one or more text items.

Canvas window

Description
Items of type window cause a particular window to be displayed at a given position on the canvas.

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
    <td>height</td>
    <td>window height</td>
  </tr>
  <tr>
    <td>width</td>
    <td>window width</td>
  </tr>
</table>

Options specific to Window

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', 'win')</td>
    <td>None</td>
  </tr>
  <tr>
    <td>window</td>
    <td>Specifies the window to associate with this item. The window specified must either be a child of the canvas widget or a child of some ancestor of the canvas widget. The window may not refer to a top-level window.</td>
    <td>window</td>
    <td>mywin</td>
    <td>None</td>
  </tr>
</table>