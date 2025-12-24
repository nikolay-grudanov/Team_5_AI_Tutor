---
source_image: page_564.png
page_number: 564
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.11
tokens: 8332
characters: 1520
timestamp: 2025-12-24T00:47:48.000913
finish_reason: stop
---

Toplevel

Description
The Toplevel class defines a new toplevel widget (given by the pathName argument). Additional options, described below, may be specified in the method call or in the option database to configure aspects of the toplevel such as its background color and relief. The toplevel method returns the pathname of the new window.

A toplevel is similar to a frame except that it is created as a top-level window: its X parent is the root window of a screen rather than the logical parent from its pathname. The primary purpose of a toplevel is to serve as a container for dialog boxes and other collections of widgets. The only visible features of a toplevel are its background color and an optional 3-D border to make the toplevel appear raised or sunken.

Inheritance
Toplevel inherits from BaseWidget, Wm.

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