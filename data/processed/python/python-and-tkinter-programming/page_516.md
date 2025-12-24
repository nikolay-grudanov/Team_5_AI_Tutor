---
source_image: page_516.png
page_number: 516
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.58
tokens: 8380
characters: 1773
timestamp: 2025-12-24T00:46:24.719237
finish_reason: stop
---

metrics(*options)
Returns information about the metrics (the font-specific data), for font when it is used on window’s display. If option is specified, returns the value of that metric; if it is omitted, the return value is a dictionary of all the metrics and their values.

Functions

families(root=None)
The return value is a list of all the available font families.

names(root=None)
The return value is a list of all the named fonts that are currently defined.

Frame

Description
The Frame class defines a new window and creates an instance of a frame widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the frame such as its background color and relief. The frame command returns the path name of the new window.
A frame is a simple widget. Its primary purpose is to act as a spacer or container for complex window layouts. The only features of a frame are its background color and an optional 3-D border to make the frame appear raised or sunken.

Inheritance
Frame inherits from Widget.

Shared options

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>background (bg)</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>borderwidth (bd)</td>
    <td>0</td>
  </tr>
  <tr>
    <td>cursor</td>
    <td></td>
  </tr>
  <tr>
    <td>height</td>
    <td>0</td>
  </tr>
  <tr>
    <td>highlightbackground</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>highlightcolor</td>
    <td>SystemWindowFrame</td>
  </tr>
  <tr>
    <td>highlightthickness</td>
    <td>0</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>flat</td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td>0</td>
  </tr>
  <tr>
    <td>width</td>
    <td>0</td>
  </tr>
</table>