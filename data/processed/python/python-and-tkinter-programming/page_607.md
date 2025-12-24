---
source_image: page_607.png
page_number: 607
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.15
tokens: 8788
characters: 2732
timestamp: 2025-12-24T00:49:39.026908
finish_reason: stop
---

NoteBookS

Description
NoteBookS implements an alternative to the familiar notebook motif. The window is arranged as a series of overlaid panes with a tab which raises the corresponding pane to the top of the stack. NoteBookS has more precise control of options than NoteBookR.

Inheritance
NoteBookS inherits from Pmw.MegaWidget.

NoteBookS options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activeColor</td>
    <td>Specifies the color of the tab and its associated pane when it is the active tab.</td>
    <td>color</td>
    <td>'red'</td>
  </tr>
  <tr>
    <td>canvasColor</td>
    <td>Specifies the background color of the canvas behind the notebook panes (normally not seen if there is at least one pane).</td>
    <td>color</td>
    <td>'white'</td>
  </tr>
  <tr>
    <td>canvasHeight</td>
    <td>Specifies the overall height of the base canvas.</td>
    <td>height</td>
    <td>250</td>
  </tr>
  <tr>
    <td>canvasWidth</td>
    <td>Specifies the overall width of the base canvas.</td>
    <td>width</td>
    <td>400</td>
  </tr>
  <tr>
    <td>deactiveColor</td>
    <td>Specifies the color of any tab that is not currently the active tab.</td>
    <td>color</td>
    <td>'grey'</td>
  </tr>
  <tr>
    <td>longX</td>
    <td>Specifies the long X dimension (see diagram below).</td>
    <td>coord</td>
    <td>30</td>
  </tr>
  <tr>
    <td>longY</td>
    <td>Specifies the long Y dimension (see diagram below).</td>
    <td>coord</td>
    <td>35</td>
  </tr>
  <tr>
    <td>offsetY</td>
    <td>Specifies the offset of the top of the tab from the top of the canvas.</td>
    <td>distance</td>
    <td>5</td>
  </tr>
  <tr>
    <td>shadeColor</td>
    <td>Specifies the color of the "shadow" effect behind each tab.</td>
    <td>color</td>
    <td>'#666666'</td>
  </tr>
  <tr>
    <td>shortX</td>
    <td>Specifies the short X dimension (see diagram below).</td>
    <td>coord</td>
    <td>7</td>
  </tr>
  <tr>
    <td>shortY</td>
    <td>Specifies the short short Y dimension (see diagram below).</td>
    <td>coord</td>
    <td>7</td>
  </tr>
  <tr>
    <td>tabColor</td>
    <td>Specifies the color of the canvas behind the tabs.</td>
    <td>color</td>
    <td>'blue'</td>
  </tr>
  <tr>
    <td>tabHeight</td>
    <td>Specifies the height of the area in which the tabs will be drawn.</td>
    <td>height</td>
    <td>40</td>
  </tr>
  <tr>
    <td>textColor</td>
    <td>The color (fill) of the text used for the tab labels</td>
    <td>color</td>
    <td>'black'</td>
  </tr>
  <tr>
    <td>textFont</td>
    <td>The font used to draw the tab labels.</td>
    <td>font</td>
    <td>('Helvetica, 10, normal')</td>
  </tr>
</table>