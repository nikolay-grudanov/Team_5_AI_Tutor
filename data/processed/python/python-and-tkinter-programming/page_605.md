---
source_image: page_605.png
page_number: 605
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.91
tokens: 8329
characters: 1801
timestamp: 2025-12-24T00:49:07.408625
finish_reason: stop
---

recolorborders()
Changes the color of the page and tab borders. This method is required because the borders are created as canvas polygons and hence do not respond to normal color changing techniques, such as Pmw.Color.changecolor().

selectpage(page)
Selects page to be the currently selected page. The page will be raised and the previous selected page will be lowered.

setnaturalpagesize(pageNames = None)
Sets the width and height of the notebook to be the maximum requested width and height of all the pages. This should be called after all pages and their contents have been created. It calls update_idletasks() so that the width and height of the pages can be determined. This may cause the notebook to flash onto the screen at the default size before resizing to the natural size.

tab(pageIndex)
Returns the tab component widget of the page pageIndex, where pageIndex may have any of the forms accepted by the index() method. If tabpos is None, returns None.

NoteBookR

Description
NoteBookR implements the familiar notebook motif. The window is arranged as a series of overlaid panes with a tab which raises the corresponding pane to the top of the stack.

Inheritance
NoteBookR inherits from Pmw.MegaWidget.

NoteBookR options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>balloon</td>
    <td>Specifies balloon help for the widget.</td>
    <td>string</td>
    <td>None</td>
  </tr>
  <tr>
    <td>ipadx</td>
    <td>Specifies a padding distance to leave within each pane in the x direction.</td>
    <td>distance</td>
    <td>4</td>
  </tr>
  <tr>
    <td>ipady</td>
    <td>Specifies a padding distance to leave within each pane in the y direction.</td>
    <td>distance</td>
    <td>4</td>
  </tr>
</table>