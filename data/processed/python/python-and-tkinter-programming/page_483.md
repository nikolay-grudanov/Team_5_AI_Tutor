---
source_image: page_483.png
page_number: 483
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.92
tokens: 8499
characters: 2471
timestamp: 2025-12-24T00:45:20.873503
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
    <td>xscrollincrement</td>
    <td>Specifies an increment for horizontal scrolling, in any of the usual forms permitted for screen distances. If the value of this option is greater than zero, the horizontal view in the window will be constrained so that the canvas x coordinate at the left edge of the window is always an even multiple of xscrollincrement; furthermore, the units for scrolling (e.g., the change in view when the left and right arrows of a scrollbar are selected) will also be xscrollincrement. If the value of this option is less than or equal to zero, then horizontal scrolling is unconstrained.</td>
    <td>distance</td>
    <td>10m 200</td>
    <td>0</td>
  </tr>
  <tr>
    <td>yscrollcommand</td>
    <td>Specifies the prefix for a command used to communicate with vertical scrollbars. This option is treated in the same way as the xScrollCommand option, except that it is used for vertical scrollbars and is provided by widgets that support vertical scrolling. See the description of xScrollCommand for details on how this option is used.</td>
    <td>function</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>yscrollincrement</td>
    <td>Specifies an increment for horizontal scrolling, in any of the usual forms permitted for screen distances. If the value of this option is greater than zero, the horizontal view in the window will be constrained so that the canvas y coordinate at the top edge of the window is always an even multiple of yscrollincrement; furthermore, the units for scrolling (e.g., the change in view when the top and bottom arrows of a scrollbar are selected) will also be yscrollincrement. If the value of this option is less than or equal to zero, then horizontal scrolling is unconstrained.</td>
    <td>distance</td>
    <td>10m 200</td>
    <td>0</td>
  </tr>
</table>

Methods

addtag_above(newtag, tagOrId)
Adds newtag to the item just above the one given by tagOrId in the display list. If tagOrId denotes more than one item, then the topmost of these items in the display list is used.

addtag_all(newtag)
Adds newtag to all the items in the canvas.

addtag_below(newtag, tagOrId)
Adds newtag to the item just below the one given by tagOrId in the display list. If tagOrId denotes more than one item, then the lowest of these items in the display list is used.