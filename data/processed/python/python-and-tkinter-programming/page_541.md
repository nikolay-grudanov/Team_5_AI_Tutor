---
source_image: page_541.png
page_number: 541
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.77
tokens: 8446
characters: 2354
timestamp: 2025-12-24T00:47:09.534000
finish_reason: stop
---

Place geometry manager

Description
The Placer is a geometry manager for Tk. It provides simple fixed placement of windows, where you specify the exact size and location of one window, called the slave, within another window, called the master. The Placer also provides rubber-sheet placement, where you specify the size and location of the slave in terms of the dimensions of the master, so that the slave changes size and location in response to changes in the size of the master. Lastly, the Placer allows you to mix these styles of placement so that, for example, the slave has a fixed width and height but it is centered inside the master.

Inheritance
Inherits from None. Place does not inherit from anything.

Shared options
None.

Options specific to Place

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>anchor</td>
    <td>Value specifies which point of window is to be positioned at the (x,y) location selected by the x, y, relx, and rely options. The anchor point is in terms of the outer area of the window including its border, if any. Thus if where is SE then the lower-right corner of window’s border will appear at the given (x,y) location in the master.</td>
    <td>constant</td>
    <td>N SE</td>
    <td>NW</td>
  </tr>
  <tr>
    <td>bordermode</td>
    <td>mode determines the degree to which borders within the master are used in determining the placement of the slave. The default and most common value is INSIDE. In this case the Placer considers the area of the master to be the innermost area of the master, inside any border: an option of × 0 corresponds to an x-coordinate just inside the border and an option of relwidth 1.0 means the window will fill the area inside the master’s border. If mode is OUTSIDE then the Placer considers the area of the master to include its border; this mode is typically used when placing the window outside its master, as with the options x 0 y 0 anchor NE. Lastly, mode may be specified as IGNORE, in which case borders are ignored: the area of the master is considered to be its official X area, which includes any internal border but no external border. A bordermode of ignore is probably not very useful.</td>
    <td>constant</td>
    <td>OUTSIDE</td>
    <td>INSIDE</td>
  </tr>
</table>