---
source_image: page_626.png
page_number: 626
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.74
tokens: 8647
characters: 2864
timestamp: 2025-12-24T00:49:57.277610
finish_reason: stop
---

Inheritance
ScrolledText inherits from Pmw.MegaWidget.

ScrolledText options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>borderframe</td>
    <td>A frame widget which snugly fits around the text widget, to give the appearance of a text border. It is created with a border so that the text widget, which is created without a border, looks like it has a border.</td>
    <td>widget</td>
    <td>Frame</td>
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
    <td>The distance between the scrollbars and the text widget.</td>
    <td>distance</td>
    <td>2</td>
  </tr>
  <tr>
    <td>usehullsize</td>
    <td>If true, the size of the megawidget is determined solely by the width and height options of the hull component. Otherwise, the size of the megawidget is determined by the width and height of the text component, along with the size and/or existence of the other components, such as the label, the scrollbars and the scrollmargin option. All of these affect the overall size of the megawidget.</td>
    <td>boolean</td>
    <td>0</td>
  </tr>
  <tr>
    <td>vscrollmode</td>
    <td>The vertical scroll mode. If none, the vertical scrollbar will never be displayed. If static, the scrollbar will always be displayed. If dynamic, the scrollbar will be displayed only if necessary.</td>
    <td>constant</td>
    <td>'dynamic'</td>
  </tr>
</table>

Components

borderframe
A frame widget which snugly fits around the text widget, to give the appearance of a text border. It is created with a border so that the text widget, which is created without a border, looks like it has a border.

horizscrollbar
The horizontal scrollbar. Its component group is Scrollbar.