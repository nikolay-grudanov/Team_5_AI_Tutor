---
source_image: page_501.png
page_number: 501
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.23
tokens: 8529
characters: 2231
timestamp: 2025-12-24T00:45:57.491511
finish_reason: stop
---

Canvas polygon

Description
Items of type polygon appear as polygonal or curved-filled regions on the display.

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
    <td>transparent</td>
  </tr>
  <tr>
    <td>width</td>
    <td>1</td>
  </tr>
</table>

Options specific to Polygon

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>outline</td>
    <td>color specifies a color to use for drawing the polygon’s outline. If color is an empty string then no outline will be drawn for the polygon.</td>
    <td>color</td>
    <td>BLUE<br>'black'</td>
    <td>'black'</td>
  </tr>
  <tr>
    <td>smooth</td>
    <td>boolean must have one of the forms accepted by Tkinter. It indicates whether or not the polygon should be drawn with a curved perimeter. If so, the outline of the polygon becomes a set of parabolic splines, one spline for the first and second line segments, one for the second and third, and so on. Straight-line segments can be generated in a smoothed polygon by duplicating the end-points of the desired line segment.</td>
    <td>boolean</td>
    <td>1 FALSE</td>
    <td>FALSE</td>
  </tr>
  <tr>
    <td>splinesteps</td>
    <td>Specifies the degree of smoothness desired for curves: each spline will be approximated with number line segments. This option is ignored unless the smooth option is true.</td>
    <td>integer</td>
    <td>20</td>
    <td>12</td>
  </tr>
  <tr>
    <td>stipple</td>
    <td>Indicates that the polygon should be filled in a stipple pattern; bitmap specifies the stipple pattern to use. If the fill option hasn’t been specified then this option has no effect. If bitmap is an empty string (the default), then filling is done in a solid fashion.</td>
    <td>bitmap</td>
    <td>'gray25'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', 'poly')</td>
    <td>None</td>
  </tr>
</table>