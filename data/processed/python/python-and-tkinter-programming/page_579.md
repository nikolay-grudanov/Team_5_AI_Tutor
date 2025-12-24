---
source_image: page_579.png
page_number: 579
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.50
tokens: 8677
characters: 2925
timestamp: 2025-12-24T00:48:35.415928
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
    <td>increment</td>
    <td>If datatype is not a dictionary, then it is equivalent to specifying it as a dictionary with a single counter field. For example, datatype = 'real' is equivalent to datatype = {'counter': 'real'}.<br><br>Specifies how many units should be added or subtracted when the counter is incremented or decremented. If the currently displayed value is not a multiple of increment, the value is changed to the next multiple greater or less than the current value.<br><br>For the number datatypes, the value of increment is a number. For the time datatype, the value is in seconds. For the date datatype, the value is in days.</td>
    <td>units</td>
    <td>1</td>
  </tr>
  <tr>
    <td>initwait</td>
    <td>Specifies the initial delay (in milliseconds) before a depressed arrow button automatically starts to repeat counting.</td>
    <td>milliseconds</td>
    <td>300</td>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labellpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>labelpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelpos is W, the label is placed in the centre of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td></td>
  </tr>
  <tr>
    <td>orient</td>
    <td>Specifies whether the arrow buttons should appear to the left and right of the entry field (HORIZONTAL) or above and below (VERTICAL).</td>
    <td>constant</td>
    <td>HORIZONTAL</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>Specifies a padding distance to leave around the arrow buttons in the x direction.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>Specifies a padding distance to leave around the arrow buttons in the y direction.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>repeatrate</td>
    <td>Specifies the delay (in milliseconds) between automatic counts while an arrow button is held down.</td>
    <td>milliseconds</td>
    <td>50</td>
  </tr>
</table>

* The standard counters are:
  • numeric   An integer number, as accepted by string.atol()
  • integer   Same as numeric.
  • real      A real number, as accepted by string.atof(). This counter accepts a separator argument, which specifies the character used to represent the decimal point. The default separator is ‘.’.