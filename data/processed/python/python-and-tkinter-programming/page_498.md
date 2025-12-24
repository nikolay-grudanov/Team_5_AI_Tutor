---
source_image: page_498.png
page_number: 498
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.10
tokens: 8623
characters: 2620
timestamp: 2025-12-24T00:45:55.024858
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
    <td>arrow</td>
    <td>Indicates whether or not arrowheads are to be drawn at one or both ends of the line. where must have one of the values None (for no arrowheads), FIRST (for an arrowhead at the first point of the line), last (for an arrowhead at the last point of the line), or both (for arrowheads at both ends).</td>
    <td>constant</td>
    <td>FIRST<br>'last'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>arrowshape</td>
    <td>This option indicates how to draw arrowheads. The shape argument must be a tuple with three elements, each specifying a distance in any of the forms acceptable to Tkinter. The first element of the list gives the distance along the line from the neck of the arrowhead to its tip. The second element gives the distance along the line from the trailing points of the arrowhead to the tip, and the third element gives the distance from the outside edge of the line to the trailing points. If this option isn’t specified then Tk picks a “reasonable” shape.</td>
    <td>tuple</td>
    <td>(6,8,3)</td>
    <td>(8,10,3)</td>
  </tr>
  <tr>
    <td>capstyle</td>
    <td>Specifies the ways in which caps are to be drawn at the endpoints of the line. The style may have any of the forms (BUTT, PROJECTING, or ROUND). Where arrowheads are drawn the cap style is ignored.</td>
    <td>constant</td>
    <td>BUTT<br>'round'</td>
    <td>BUTT</td>
  </tr>
  <tr>
    <td>joinstyle</td>
    <td>Specifies the ways in which joints are to be drawn at the vertices of the line. The style may have any of the forms (BEVEL, MITER, or ROUND). If the line only contains two points then this option is irrelevant.</td>
    <td>constant</td>
    <td>BEVEL<br>'miter'</td>
    <td>ROUND</td>
  </tr>
  <tr>
    <td>smooth</td>
    <td>The value must be a boolean. It indicates whether or not the line should be drawn as a curve. If so, the line is rendered as a set of parabolic splines: one spline is drawn for the first and second line segments, one for the second and third, and so on. Straight-line segments can be generated within a curve by duplicating the end-points of the desired line segment.</td>
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
</table>