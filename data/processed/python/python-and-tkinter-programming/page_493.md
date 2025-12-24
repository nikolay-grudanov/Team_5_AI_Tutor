---
source_image: page_493.png
page_number: 493
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.68
tokens: 8494
characters: 2123
timestamp: 2025-12-24T00:45:40.773115
finish_reason: stop
---

Canvas Arc

Description
Items of type arc appear on the display as arc-shaped regions. An arc is a section of an oval delimited by two angles (specified by the start and extent options) and is displayed in one of several ways (specified by the style option).

Inheritance
Inherits from Widget, Canvas.

Shared options

<table>
  <tr>
    <th>Option</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>fill</td>
    <td>Transparent</td>
  </tr>
  <tr>
    <td>width</td>
    <td>1</td>
  </tr>
</table>

Options specific to Arc

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>extent</td>
    <td>Specifies the size of the angular range occupied by the arc. The arc’s range extends for degrees degrees counter-clockwise from the starting angle given by the start option. degrees may be negative. If it is greater than 360 or less than -360, then degrees modulo 360 is used as the extent.</td>
    <td>degrees</td>
    <td>10.0</td>
    <td></td>
  </tr>
  <tr>
    <td>outline</td>
    <td>color specifies a color to use for drawing the arc’s outline; it may have any of the forms accepted by Tkinter (Tk_GetColor). This option defaults to black. If color is specified as an empty string then no outline is drawn for the arc.</td>
    <td>color</td>
    <td>RED 'black' 'black'</td>
    <td></td>
  </tr>
  <tr>
    <td>outlinestipple</td>
    <td>Indicates that the outline for the arc should be drawn with a stipple pattern; bitmap specifies the stipple pattern to use. If the outline option hasn’t been specified then this option has no effect. If bitmap is an empty string (the default), then the outline is drawn in a solid fashion.</td>
    <td>bitmap</td>
    <td>'gray12'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>start</td>
    <td>Specifies the beginning of the angular range occupied by the arc. degrees is given in units of degrees measured counter-clockwise from the three-o’clock position; it may be either positive or negative.</td>
    <td>degrees</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
</table>