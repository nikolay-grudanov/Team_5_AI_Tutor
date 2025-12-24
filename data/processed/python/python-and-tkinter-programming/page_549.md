---
source_image: page_549.png
page_number: 549
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.75
tokens: 8707
characters: 2721
timestamp: 2025-12-24T00:47:33.645648
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>repeatinterval</td>
    <td>Used in conjunction with repeatDelay: once auto-repeat begins, this option determines the number of milliseconds between auto repeats.</td>
    <td>integer</td>
    <td>100</td>
    <td>100</td>
  </tr>
  <tr>
    <td>resolution</td>
    <td>A real value specifying the resolution for a scale widget. If this value is greater than zero then the scale’s value will always be rounded to an even multiple of this value, as will tick marks and the endpoints of the scale. If the value is less than zero then no rounding occurs. Defaults to 1 (i.e., the value will be integral).</td>
    <td>float</td>
    <td>2.0 10.0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>showvalue</td>
    <td>Specifies a boolean value indicating whether or not the current value of a scale widget is to be displayed.</td>
    <td>boolean</td>
    <td>TRUE 0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>sliderlength</td>
    <td>Specfies the size of a slider, measured in screen units along the slider’s long dimension. The value may be specified in any of the forms acceptable to winfo.pixels.</td>
    <td>distance</td>
    <td>140 2i</td>
    <td>30</td>
  </tr>
  <tr>
    <td>sliderrelief</td>
    <td>Specifies the relief to use when drawing the slider, such as raised or sunken.</td>
    <td></td>
    <td></td>
    <td>raised</td>
  </tr>
  <tr>
    <td>tickinterval</td>
    <td>Must be a real value. Determines the spacing between numerical tick marks displayed below or to the left of the slider. If it is 0, no tick marks will be displayed.</td>
    <td>float</td>
    <td>0 5.0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>to</td>
    <td>Specifies a real value corresponding to the right or bottom end of the scale. This value may be either less than or greater than the from option.</td>
    <td>float</td>
    <td>25.0 -30.0</td>
    <td>100</td>
  </tr>
  <tr>
    <td>troughcolor</td>
    <td>Specifies the color to use for the rectangular trough areas in widgets such as scrollbars and scales.</td>
    <td>color</td>
    <td>'gray40'</td>
    <td>System-Scroll-bar</td>
  </tr>
  <tr>
    <td>variable</td>
    <td>Specifies name of a Tkinter variable to contain the content and set the content of the widget.</td>
    <td>variable</td>
    <td>myVariable</td>
    <td></td>
  </tr>
</table>

Methods

coords(value=None)
Returns a tuple whose elements are the x and y coordinates of the point along the centerline of the trough that corresponds to value. If value is omitted then the scale’s current value is used.

get()
Returns the current value of the scale.