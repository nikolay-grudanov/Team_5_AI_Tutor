---
source_image: page_632.png
page_number: 632
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.42
tokens: 8764
characters: 2980
timestamp: 2025-12-24T00:50:13.080031
finish_reason: stop
---

**TimeCounter**

**Description**
A TimeCounter presents three up/down counters which act together to allow the user to input a time. Incrementing a second or minute counter past 59 will increment the minute or hour counter respectively.

**Inheritance**
TimeCounter inherits from Pmw.MegaWidget.

**TimeCounter options**

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>autorepeat</td>
    <td>If autorepeat is true the up and down buttons will activate every repeatrate milliseconds after the initwait delay.</td>
    <td>boolean</td>
    <td>1</td>
  </tr>
  <tr>
    <td>buttonaspect</td>
    <td>Specifies the width of the arrow buttons as a proportion of their height. Values less than 1.0 will produce thin arrow buttons. Values greater than 1.0 will produce fat arrow buttons.</td>
    <td>float</td>
    <td>1.0</td>
  </tr>
  <tr>
    <td>initwait</td>
    <td>If autorepeat is true the widget will wait initwait milliseconds before repeatedly activating an up or down button.</td>
    <td>milliseconds</td>
    <td>300</td>
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
    <td>max</td>
    <td>The maximum value to be displayed by the widget. A value of 23:59:59 will result in a 24-hour time counter.</td>
    <td>string</td>
    <td>"</td>
  </tr>
  <tr>
    <td>min</td>
    <td>The minimum time to be displayed in the widget. This will normally be 00:00:00 or be left as the default.</td>
    <td></td>
    <td>"</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>Specifies a padding distance to leave between each spin button in the x dimension.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>Specifies a padding distance to leave between each spin button in the y dimension.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>repeatrate</td>
    <td>If autorepeat is true, specifies the rate at which a button will repeatedly activate if the button is held down.</td>
    <td>milliseconds</td>
    <td>50</td>
  </tr>
  <tr>
    <td>value</td>
    <td>The initial value to be displayed in the widget.</td>
    <td></td>
    <td>"</td>
  </tr>
</table>