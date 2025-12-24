---
source_image: page_621.png
page_number: 621
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.15
tokens: 8792
characters: 3552
timestamp: 2025-12-24T00:49:57.292456
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>horizflex</td>
    <td>Specifies how the width of the scrollable interior frame should be resized relative to the clipping frame. If fixed, the interior frame is set to the natural width, as requested by the child widgets of the frame. If expand and the requested width of the interior frame is less than the width of the clipping frame, the interior frame expands to fill the clipping frame. If shrink and the requested width of the interior frame is more than the width of the clipping frame, the interior frame shrinks to the width of the clipping frame. If elastic, the width of the interior frame is always set to the width of the clipping frame.</td>
    <td>constant</td>
    <td>'fixed'</td>
  </tr>
  <tr>
    <td>horizfraction</td>
    <td>The fraction of the width of the clipper frame to scroll the interior frame when the user clicks on the horizontal scrollbar arrows.</td>
    <td>distance</td>
    <td>0.05</td>
  </tr>
  <tr>
    <td>hscrollmode</td>
    <td>The horizontal scroll mode. If none, the horizontal scrollbar will never be displayed. If static, the scrollbar will always be displayed. If dynamic, the scrollbar will be displayed only if necessary.</td>
    <td>constant</td>
    <td>'dynamic'</td>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labelpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>labelpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
  <tr>
    <td>scrollmargin</td>
    <td>The distance between the scrollbars and the clipping frame.</td>
    <td>distance</td>
    <td>2</td>
  </tr>
  <tr>
    <td>usehullsize</td>
    <td>If true, the size of the megawidget is determined solely by the width and height options of the hull component. Otherwise, the size of the megawidget is determined by the width and height of the clipper component, along with the size and/or existence of the other components, such as the label, the scrollbars and the scrollmargin option. All these affect the overall size of the megawidget.</td>
    <td>boolean</td>
    <td>0</td>
  </tr>
  <tr>
    <td>vertflex</td>
    <td>Specifies how the height of the scrollable interior frame should be resized relative to the clipping frame. If fixed, the interior frame is set to the natural height, as requested by the child widgets of the frame. If expand and the requested height of the interior frame is less than the height of the clipping frame, the interior frame expands to fill the clipping frame. If shrink and the requested height of the interior frame is more than the height of the clipping frame, the interior frame shrinks to the height of the clipping frame. If elastic, the height of the interior frame is always set to the height of the clipping frame.</td>
    <td>constant</td>
    <td>'fixed'</td>
  </tr>
</table>