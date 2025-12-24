---
source_image: page_518.png
page_number: 518
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.25
tokens: 8818
characters: 3175
timestamp: 2025-12-24T00:46:53.569973
finish_reason: stop
---

Description
Grid is used to communicate with the grid geometry manager that arranges widgets in rows and columns inside of another window, called the geometry master (or master window).

Shared options
None.

Options specific to Grid

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>column</td>
    <td>Insert the slave so that it occupies the nth column in the grid. Column numbers start with 0. If this option is not supplied, then the slave is arranged just to the right of previous slave specified on this call to grid, or column 0 if it is the first slave. For each x that immediately precedes the slave, the column position is incremented by one. Thus the x represents a blank column for this row in the grid.</td>
    <td>integer</td>
    <td>1 4</td>
    <td>0</td>
  </tr>
  <tr>
    <td>columnspan</td>
    <td>Insert the slave so that it occupies n columns in the grid.</td>
    <td>integer</td>
    <td>2</td>
    <td>1</td>
  </tr>
  <tr>
    <td>in_</td>
    <td>Insert the slave(s) in the master window supplied.</td>
    <td>widget</td>
    <td>myWin</td>
    <td>None</td>
  </tr>
  <tr>
    <td>ipadx</td>
    <td>The amount specifies how much horizontal internal padding to leave on each side of the slave(s). This space is added inside the slave(s) border. The amount must be a valid screen distance, such as 2 or .5c.</td>
    <td>distance</td>
    <td>5m</td>
    <td>0</td>
  </tr>
  <tr>
    <td>ipady</td>
    <td>The amount specifies how much vertical internal padding to leave on on the top and bottom of the slave(s). This space is added inside the slave(s) border.</td>
    <td>distance</td>
    <td>3m</td>
    <td>0</td>
  </tr>
  <tr>
    <td>minsize (row, column)</td>
    <td>The minsize option sets the minimum size, in screen units, that will be permitted for this row/column.</td>
    <td>integer</td>
    <td>25</td>
    <td>None</td>
  </tr>
  <tr>
    <td>pad</td>
    <td>Specifies the number of screen units that will be added to the largest window contained completely in that column when the grid geometry manager requests a size from the containing window.</td>
    <td>integer</td>
    <td>5</td>
    <td>0</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>The amount specifies how much horizontal external padding to leave on each side of the slave(s), in screen units. This space is added outside the slave(s) border.</td>
    <td>distance</td>
    <td>5</td>
    <td>0</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>The amount specifies how much vertical external padding to leave on the top and bottom of the slave(s), in screen units. This space is added outside the slave(s) border.</td>
    <td>distance</td>
    <td>5</td>
    <td>0</td>
  </tr>
  <tr>
    <td>row</td>
    <td>Insert the slave so that it occupies the nth row in the grid. Row numbers start with 0. If this option is not supplied, then the slave is arranged on the same row as the previous slave specified on this call to grid, or the first unoccupied row if this is the first slave.</td>
    <td>integer</td>
    <td>3</td>
    <td>Same row</td>
  </tr>
</table>