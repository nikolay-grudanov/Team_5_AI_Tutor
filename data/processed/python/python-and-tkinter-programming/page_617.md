---
source_image: page_617.png
page_number: 617
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.07
tokens: 8564
characters: 2469
timestamp: 2025-12-24T00:49:39.415852
finish_reason: stop
---

ScrolledCanvas

Description
This megawidget consists of a standard canvas widget with optional scrollbars which can be used to scroll the canvas. The scrollbars can be dynamic, which means that a scrollbar will only be displayed if it is necessary (if the scrollregion of the canvas is larger than the canvas).

Inheritance
ScrolledCanvas inherits from Pmw.MegaWidget.

ScrolledCanvas options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>borderframe</td>
    <td>A frame widget which snugly fits around the canvas, to give the appearance of a canvas border. It is created with a border so that the canvas, which is created without a border, looks like it has a border.</td>
    <td>widget</td>
    <td>Frame</td>
  </tr>
  <tr>
    <td>canvasmargin</td>
    <td>The margin around the items in the canvas. Used by the resizescrollregion() method.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>hscrollmode</td>
    <td>The horizontal scroll mode. If none, the horizontal scrollbar will never be displayed. If static, the scrollbar will always be displayed. If dynamic, the scrollbar will be displayed only if necessary.</td>
    <td>constant</td>
    <td>'dynamic'</td>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labelfpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>labelfpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelfpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
  <tr>
    <td>scrollmargin</td>
    <td>The distance between the scrollbars and the enclosing canvas widget.</td>
    <td>distance</td>
    <td>2</td>
  </tr>
  <tr>
    <td>usehullsize</td>
    <td>If true, the size of the megawidget is determined solely by the width and height options of the hull component.</td>
    <td>boolean</td>
    <td>0</td>
  </tr>
</table>