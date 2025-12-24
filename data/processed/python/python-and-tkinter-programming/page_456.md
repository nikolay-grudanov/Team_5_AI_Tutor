---
source_image: page_456.png
page_number: 456
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.50
tokens: 8508
characters: 2447
timestamp: 2025-12-24T00:44:35.513193
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
    <td>state</td>
    <td>Specifies one of two or three states for the widget (typically checkbutton): NORMAL and DISABLED or NORMAL, ACTIVE and DISABLED. In NORMAL state the widget is displayed using the foreground and background options. The ACTIVE state is typically used when the pointer is over the widget. In ACTIVE state the widget is displayed using the activeforeground and activebackground options. DISABLED state means that the widget should be insensitive: the default bindings will refuse to activate the widget and will ignore mouse button presses. In this state the disabledforeground and background options determine how the widget is displayed.</td>
    <td>constant</td>
    <td>ACTIVE</td>
    <td>Button<br>Checkbutton Entry<br>Menubutton<br>Radiobutton Scale<br>Text</td>
  </tr>
  <tr>
    <td>text</td>
    <td>Specifies a string to be displayed inside the widget. The way in which the string is displayed depends on the particular widget and may be determined by other options, such as anchor or justify.</td>
    <td>string</td>
    <td>'Display This'</td>
    <td>Button<br>Checkbutton Label<br>Menubutton<br>Message<br>Radiobutton</td>
  </tr>
  <tr>
    <td>textvariable</td>
    <td>Specifies the name of a variable. The value of the variable is converted to a text string to be displayed inside the widget; if the variable value changes then the widget will automatically update itself to reflect the new value. The way in which the string is displayed in the widget depends on the particular widget and may be determined by other options, such as anchor or justify.</td>
    <td>variable</td>
    <td>widgetContent</td>
    <td>Button<br>Checkbutton Entry<br>Label<br>Menubutton<br>Message<br>Radiobutton</td>
  </tr>
  <tr>
    <td>underline</td>
    <td>Specifies the integer index of a character to underline in the widget. This option is used by the default bindings to implement keyboard traversal for menu buttons and menu entries. 0 corresponds to the first character of the text displayed in the widget, 1 to the next character, and so on.</td>
    <td>integer</td>
    <td>2</td>
    <td>Button<br>Checkbutton Label<br>Menubutton<br>Radiobutton</td>
  </tr>
</table>

ОПЦИИ ДЛЯ МНОГИХ ВИДЖЕТОВ