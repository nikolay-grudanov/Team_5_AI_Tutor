---
source_image: page_519.png
page_number: 519
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.93
tokens: 8537
characters: 2634
timestamp: 2025-12-24T00:46:32.475894
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
    <td rowspanspan>rowspan</td>
    <td>Insert the slave so that it occupies n rows in the grid.<br>The default is one row.</td>
    <td>integer</td>
    <td>4</td>
    <td>Same row</td>
  </tr>
  <tr>
    <td>sticky</td>
    <td>If a slave’s cell is larger than its requested dimensions, this option may be used to position (or stretch) the slave within its cell. Style is a string that contains zero or more of the characters N, S, E or W. The string can optionally contain spaces or commas, but they are ignored. Each letter refers to a side (north, south, east, or west) that the slave will “stick” to. If both N and S (or E and W) are specified, the slave will be stretched to fill the entire height (or width) of its cavity. The sticky option subsumes the combination of anchor and fill that is used by pack.</td>
    <td>string</td>
    <td>EW</td>
    <td>CENTER</td>
  </tr>
  <tr>
    <td>weight (row/column)</td>
    <td>The weight option sets the relative weight for apportioning any extra spaces among rows/columns. A weight of zero (0) indicates the column will not deviate from its requested size. A column whose weight is two will grow at twice the rate as a column of weight one when extra space is allocated to the layout.</td>
    <td>integer</td>
    <td>2</td>
    <td>0</td>
  </tr>
</table>

Methods

grid(option=value, ...)
Use the grid manager for self.

grid_bbox(column=None, row=None, col2=None, row2=None)
With no arguments, the bounding box (in pixels) of the grid is returned. The return value consists of four integers. The first two are the pixel offset from the master window (x then y) of the top-left corner of the grid, and the second two integers are the width and height of the grid, also in pixels. If a single column and row is specified in the method call, then the bounding box for that cell is returned, where the top left cell is numbered from zero. If both column and row arguments are specified, then the bounding box spanning the rows and columns indicated is returned.

grid_columnconfigure(index, options...)
Queries or sets the column properties of the index column of the geometry master, master. The valid options are minsize, weight and pad.

grid_configure(options...)
The arguments consist of pairs of arguments that specify how to manage the slaves.

grid_forget()
Removes self from grid for its master and unmaps their windows. The slave will no longer be managed by the grid geometry manager. The configuration options for that window are