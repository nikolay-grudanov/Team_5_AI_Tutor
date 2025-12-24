---
source_image: page_454.png
page_number: 454
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.28
tokens: 8551
characters: 2458
timestamp: 2025-12-24T00:44:27.040806
finish_reason: stop
---

Вот таблица с описанием общих опций для многих виджетов:

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>These widgets only</th>
  </tr>
  <tr>
    <td>command</td>
    <td>Specifies a Python command to associate with the widget. This command is typically invoked when mouse button 1 is released over the widget. For check buttons and radio buttons the button’s tkinter variable (set with the variable option) will be updated before the command is invoked.</td>
    <td>command</td>
    <td>setupData</td>
    <td>Button<br>Checkbutton<br>Radiobutton<br>Scrollbar</td>
  </tr>
  <tr>
    <td>disabledforeground</td>
    <td>Specifies the foreground color to use when drawing a disabled element. If the option is specified as an empty string (which is typically the case on monochrome displays), disabled elements are drawn with the normal foreground color but they are dimmed by drawing them with a stippled fill pattern.</td>
    <td>color</td>
    <td>'gray50'</td>
    <td>Button<br>Checkbutton Menu<br>Menubutton<br>Radiobutton</td>
  </tr>
  <tr>
    <td>height</td>
    <td>Specifies the desired height for the window, in units of characters in the font given by the font option. Must be at least one.</td>
    <td>integer</td>
    <td>1 4</td>
    <td>Button Canvas Checkbutton<br>Frame Label<br>Listbox<br>Menubutton<br>Radiobutton Text<br>Toplevel</td>
  </tr>
  <tr>
    <td>image</td>
    <td>Specifies an image to display in the widget, which must have been created with the image create method.<br>Typically, if the image option is specified then it overrides other options that specify a bitmap or textual value to display in the widget; the image option may be reset to an empty string to re-enable a bitmap or text display.</td>
    <td>image</td>
    <td></td>
    <td>Button<br>Checkbutton Label<br>Menubutton<br>Radiobutton</td>
  </tr>
  <tr>
    <td>justify</td>
    <td>When multiple lines of text are displayed in a widget, this option determines how the lines line up with each other. Must be one of LEFT, CENTER, or RIGHT. LEFT means that the lines’ left edges all line up, CENTER means that the lines’ centers are aligned, and RIGHT means that the lines’ right edges line up.</td>
    <td>constant</td>
    <td>RIGHT</td>
    <td>Button<br>Checkbutton Entry<br>Label<br>Menubutton<br>Message<br>Radiobutton</td>
  </tr>
</table>

Опции, общие для многих виджетов.