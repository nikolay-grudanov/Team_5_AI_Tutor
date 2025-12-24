---
source_image: page_615.png
page_number: 615
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.24
tokens: 8691
characters: 3019
timestamp: 2025-12-24T00:49:42.753108
finish_reason: stop
---

RadioSelect options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>buttontype</td>
    <td>Specifies the default type of buttons created by the add() method. If button, the default type is Button. If radiobutton, the default type is Radiobutton. If checkbutton, the default type is Checkbutton.</td>
    <td>constant</td>
    <td>None</td>
  </tr>
  <tr>
    <td>command</td>
    <td>Specifies a function to call when one of the buttons is clicked on or when invoke() is called.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labellpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
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
    <td>Specifies the direction in which the buttons are laid out. This may be HORIZONTAL or VERTICAL.</td>
    <td>constant</td>
    <td>HORIZONTAL</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>Specifies a padding distance to leave between each button in the x direction and also between the buttons and the outer edge of the radio select widget.</td>
    <td>distance</td>
    <td>5</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>Specifies a padding distance to leave between each button in the y direction and also between the buttons and the outer edge of the radio select widget.</td>
    <td>distance</td>
    <td>5</td>
  </tr>
  <tr>
    <td>selectmode</td>
    <td>Specifies the selection mode: whether a single button or multiple buttons can be selected at one time. If single, clicking on an unselected button selects it and deselects all other buttons. If multiple, clicking on an unselected button selects it and clicking on a selected button deselects it. This option is ignored if buttontype is radiobutton or checkbutton.</td>
    <td>constant</td>
    <td>'single'</td>
  </tr>
</table>

Components

frame
If the label component has been created (that is, the labelpos option is not None), the frame component is created to act as the container of the buttons created by the add() method. If there is no label component, then no frame component is created and the hull component acts as the container.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.