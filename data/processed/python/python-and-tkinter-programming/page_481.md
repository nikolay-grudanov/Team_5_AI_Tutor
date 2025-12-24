---
source_image: page_481.png
page_number: 481
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.09
tokens: 8474
characters: 2014
timestamp: 2025-12-24T00:45:19.658665
finish_reason: stop
---

Canvas

Description
The Canvas class defines a new window and creates an instance of a canvas widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the canvas such as its colors and 3-D relief. The canvas method returns the identity of the new widget. At the time this method is invoked, the canvas’s parent must exist.

Canvas widgets implement structured graphics. A canvas displays any number of items, which may be things like rectangles, circles, lines, and text. Items may be manipulated (e.g. moved or re-colored) and callbacks may be associated with items in much the same way that the bind method allows callbacks to be bound to widgets. For example, a particular callback may be associated with the <Button-1> event so that the callback is invoked whenever Button-1 is pressed with the mouse cursor over an item. This means that items in a canvas can have behaviors defined by the Tkinter functions bound to them.

Inheritance
Canvas inherits from Widget.

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
    <td>7c</td>
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
    <td>2</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>flat</td>
  </tr>
  <tr>
    <td>selectbackground</td>
    <td>SystemHighlight</td>
  </tr>
  <tr>
    <td>selectborderwidth</td>
    <td>1</td>
  </tr>
  <tr>
    <td>selectforeground</td>
    <td>SystemHighlightText</td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td></td>
  </tr>
  <tr>
    <td>width</td>
    <td>10c</td>
  </tr>
  <tr>
    <td>xscrollcommand</td>
    <td></td>
  </tr>
</table>