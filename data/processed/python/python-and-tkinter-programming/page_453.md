---
source_image: page_453.png
page_number: 453
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.70
tokens: 8461
characters: 2249
timestamp: 2025-12-24T00:44:20.396076
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>These widgets only</th>
  </tr>
  <tr>
    <td>activebackground</td>
    <td>Specifies the background color to use when drawing active elements. An element (a widget or portion of a widget) is active if the mouse cursor is positioned over the element and pressing a mouse button will cause some action to occur. If strict Motif compliance has been requested by setting the tk_strictMotif variable, this option will normally be ignored; the normal background color will be used instead. For some elements on Windows and Macintosh systems, the active color will only be used while mouse button 1 is pressed over the element.</td>
    <td>color</td>
    <td>'red' '<#fa07a3'</td>
    <td>Button Checkbutton Menu Menubutton Radiobutton Scale Scrollbar</td>
  </tr>
  <tr>
    <td>activeforeground</td>
    <td>Specifies the foreground color to use when drawing active elements. See above for definition of active elements.</td>
    <td>color</td>
    <td>'cadet-blue'</td>
    <td>Button Checkbutton Menu Menubutton Radiobutton</td>
  </tr>
  <tr>
    <td>anchor</td>
    <td>Specifies how the information in a widget (e.g. text or a bitmap) is to be displayed in the widget. Must be one of the values N, NE, E, SE, S, SW, W, NW, or CENTER. For example, NW means to display the information so that its top-left corner is at the top-left corner of the widget.</td>
    <td>constant</td>
    <td></td>
    <td>Button Checkbutton Label Menubutton Message Radiobutton</td>
  </tr>
  <tr>
    <td>bitmap</td>
    <td>Specifies a bitmap to display in the widget, in any of the forms acceptable to Tkinter (Tk_GetBitmap). The exact way in which the bitmap is displayed may be affected by other options such as anchor or justify.<br>Typically, if this option is specified then it overrides other options that specify a textual value to display in the widget; the bitmap option may be reset to an empty string to re-enable a text display. In widgets that support both bitmap and image options, image will usually override bitmap.</td>
    <td>bitmap</td>
    <td></td>
    <td>Button Checkbutton Label Menubutton Radiobutton</td>
  </tr>
</table>