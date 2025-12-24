---
source_image: page_488.png
page_number: 488
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.19
tokens: 8697
characters: 3605
timestamp: 2025-12-24T00:45:46.936929
finish_reason: stop
---

for the first item given by tagOrId. If option is specified with no value, then the method returns a dictionary describing the one named option (this list will be identical to the corresponding sublist of the value returned if no option is specified). If one or more option-value pairs are specified, then the method modifies the given widget option(s) to have the given value(s) in each of the items given by tagOrId; in this case the method returns None. The options and values are the same as those permissible in the create widget method when the item(s) were created; see the sections describing individual item types below for details on the legal options.

move(tagOrId, xAmount, yAmount)
Moves each of the items given by tagOrId in the canvas coordinate space by adding xAmount to the x-coordinate of each point associated with the item and yAmount to the y-coordinate of each point associated with the item. This method returns None.

postscript(options)
Generates a Postscript representation for part or all of the canvas. If the file option is specified then the Postscript is written to a file and an empty string is returned; otherwise the Postscript is returned as the result of the method. If the interpreter that owns the canvas is marked as safe, the operation will fail because safe interpreters are not allowed to write files. If the channel option is specified, the argument denotes the name of a channel already opened for writing. The Postscript is written to that channel, and the channel is left open for further writing at the end of the operation. The Postscript is created in Encapsulated Postscript form using version 3.0 of the Document Structuring Conventions.

Note: By default Postscript is only generated for information that appears in the canvas’s window on the screen. If the canvas is freshly created it may still have its initial size of 1×1 pixel so nothing will appear in the Postscript. To get around this problem either invoke the update method to wait for the canvas window to reach its final size, or else use the width and height options to specify the area of the canvas to print. The option-value argument pairs provide additional information to control the generation of Postscript. The following options are supported:

<table>
  <tr>
    <th>Option</th>
    <th>Value (type)</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>colormap</td>
    <td>varName (array)</td>
    <td>VarName must be the name of an array variable that specifies a color mapping to use in the Postscript. Each element of varName must consist of Postscript code to set a particular color value (e.g. 1.0 1.0 0.0 setrgbcolor). When outputting color information in the Postscript, Tk checks to see if there is an element of varName with the same name as the color. If so, Tk uses the value of the element as the Postscript command to set the color. If this option hasn’t been specified, or if there isn’t an entry in varName for a given color, then Tk uses the red, green, and blue intensities from the X color.</td>
  </tr>
  <tr>
    <td>colormode</td>
    <td>mode (string)</td>
    <td>Specifies how to output color information. Mode must be either color (for full color output), gray (convert all colors to their gray-scale equivalents) or mono (convert all colors to black or white).</td>
  </tr>
  <tr>
    <td>file</td>
    <td>fileName (string)</td>
    <td>Specifies the name of the file in which to write the Postscript. If this option isn’t specified then the Postscript is returned as the result of the command instead of being written to a file.</td>
  </tr>
</table>