---
source_image: page_572.png
page_number: 572
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.82
tokens: 8492
characters: 2310
timestamp: 2025-12-24T00:48:10.785141
finish_reason: stop
---

ButtonBox options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
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
    <td>orient</td>
    <td>Specifies the orientation of the button box. This may be HORIZONTAL or VERTICAL.</td>
    <td>constant</td>
    <td>HORIZONTAL</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>Specifies a padding distance to leave between each button in the x direction and also between the buttons and the outer edge of the button box.</td>
    <td>distance</td>
    <td>3</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>Specifies a padding distance to leave between each button in the y direction and also between the buttons and the outer edge of the button box.</td>
    <td>distance</td>
    <td>3</td>
  </tr>
</table>

Components

frame
If the label component has been created (that is, the labelpos option is not None), the frame component is created to act as the container of the buttons created by the add() and insert() methods. If there is no label component, then no frame component is created and the hull component acts as the container.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelpos option is not None, this component is created as a text label for the megawidget. See the labelpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.