---
source_image: page_611.png
page_number: 611
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.00
tokens: 8433
characters: 1835
timestamp: 2025-12-24T00:49:20.481323
finish_reason: stop
---

PanedWidget

Description
This class creates a manager widget for containing resizable frames, known as panes. Each pane may act as the container for other widgets. The user may resize the panes by dragging a small rectangle (the handle) or the line between the panes (the separator).

Inheritance
PanedWidget inherits from Pmw.MegaWidget.

PanedWidget options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>command</td>
    <td>Specifies a function to be called whenever the size of any of the panes changes. The function is called with a single argument, being a list of the sizes of the panes, in order. For vertical orientation, the size is the height of the panes. For horizontal orientation, the size is the width of the panes.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>orient</td>
    <td>Specifies the orientation of the paned widget. This may be HORIZONTAL or VERTICAL. If VERTICAL, the panes are stacked above and below each other; otherwise the panes are laid out side by side.</td>
    <td>constant</td>
    <td>VERTICAL</td>
  </tr>
  <tr>
    <td>separatorrelief</td>
    <td>Specifies the relief of the line separating the panes.</td>
    <td>constant</td>
    <td>SUNKEN</td>
  </tr>
</table>

Pane options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>size</td>
    <td>Specifies the initial size of the pane.</td>
    <td>integer or real</td>
    <td>0</td>
  </tr>
  <tr>
    <td>min</td>
    <td>Specifies the minimum size of the pane.</td>
    <td>integer or real</td>
    <td>0</td>
  </tr>
  <tr>
    <td>max</td>
    <td>Specifies the maximum size of the pane.</td>
    <td>integer or real</td>
    <td>100000</td>
  </tr>
</table>