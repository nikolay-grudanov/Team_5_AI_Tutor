---
source_image: page_489.png
page_number: 489
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.92
tokens: 8941
characters: 4207
timestamp: 2025-12-24T00:45:57.090807
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Value (type)</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>fontmap</td>
    <td>varName (array)</td>
    <td>VarName must be the name of an array variable that specifies a font mapping to use in the Postscript. Each element of varName must consist of a Tcl list with two elements, which are the name and point size of a Postscript font. When outputting Postscript commands for a particular font, Tk checks to see if varName contains an element with the same name as the font. If there is such an element, then the font information contained in that element is used in the Postscript. Otherwise Tk attempts to guess what Postscript font to use. Tk’s guesses generally only work for well-known fonts such as Times and Helvetica and Courier, and only if the X font name does not omit any dashes up through the point size. For example, –Courier-Bold-R-Normal-*–120-* will work but *CourierBoldRNor-mal*120* will not; Tk needs the dashes to parse the font name.</td>
  </tr>
  <tr>
    <td>height</td>
    <td>height (distance)</td>
    <td>Specifies the height of the area of the canvas to print. Defaults to the height of the canvas window.</td>
  </tr>
  <tr>
    <td>pageanchor</td>
    <td>constant</td>
    <td>Specifies which point of the printed area of the canvas should appear over the positioning point on the page (which is given by the pagex and pagey options). For example, pageanchor n means that the top center of the area of the canvas being printed (as it appears in the canvas window) should be over the positioning point. Defaults to center.</td>
  </tr>
  <tr>
    <td>pageheight</td>
    <td>height (distance)</td>
    <td>Specifies that the Postscript should be scaled in both x and y so that the printed area is size high on the Postscript page. size consists of a floating-point number followed by c for centimeters, i for inches, m for millimeters, or p or nothing for printer’s points (1/72 inch). Defaults to the height of the printed area on the screen. If both pageheight and pagewidth are specified then the scale factor from pagewidth is used (non-uniform scaling is not implemented).</td>
  </tr>
  <tr>
    <td>pagewidth</td>
    <td>width (distance)</td>
    <td>Specifies that the Postscript should be scaled in both x and y so that the printed area is size wide on the Postscript page. size has the same form as for pageheight. Defaults to the width of the printed area on the screen. If both pageheight and pagewidth are specified then the scale factor from pagewidth is used (non-uniform scaling is not implemented).</td>
  </tr>
  <tr>
    <td>pagex</td>
    <td>position (integer)</td>
    <td>position gives the x-coordinate of the positioning point on the Postscript page, using any of the forms allowed for pageheight. Used in conjunction with the pagey and pageanchor options to determine where the printed area appears on the Postscript page. Defaults to the center of the page.</td>
  </tr>
  <tr>
    <td>pagey</td>
    <td>position (integer)</td>
    <td>position gives the y-coordinate of the positioning point on the Postscript page, using any of the forms allowed for pageheight. Used in conjunction with the pagex and pageanchor options to determine where the printed area appears on the Postscript page. Defaults to the center of the page.</td>
  </tr>
  <tr>
    <td>rotate</td>
    <td>boolean (boolean)</td>
    <td>boolean specifies whether the printed area is to be rotated 90 degrees. In non-rotated output the x-axis of the printed area runs along the short dimension of the page ("portrait" orientation); in rotated output the x-axis runs along the long dimension of the page ("landscape" orientation). Defaults to non-rotated.</td>
  </tr>
  <tr>
    <td>width</td>
    <td>width (distance)</td>
    <td>Specifies the width of the area of the canvas to print. Defaults to the width of the canvas window.</td>
  </tr>
  <tr>
    <td>x</td>
    <td>position (integer)</td>
    <td>Specifies the x-coordinate of the left edge of the area of the canvas that is to be printed, in canvas coordinates, not window coordinates. Defaults to the coordinate of the left edge of the window.</td>
  </tr>
</table>