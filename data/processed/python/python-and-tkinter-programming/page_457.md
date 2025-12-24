---
source_image: page_457.png
page_number: 457
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.41
tokens: 8360
characters: 2004
timestamp: 2025-12-24T00:44:25.587495
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
    <td>wraplength</td>
    <td>For widgets that can perform word-wrapping, this option specifies the maximum line length. Lines that would exceed this length are wrapped onto the next line, so that no line is longer than the specified length. The value may be specified in any of the standard forms for screen distances. If this value is less than or equal to 0 then no wrapping is done: lines will break only at newline characters in the text.</td>
    <td>pixel</td>
    <td>4i, 65</td>
    <td>Button<br>Checkbutton Label<br>Menubutton<br>Radiobutton</td>
  </tr>
  <tr>
    <td>xscrollcommand</td>
    <td>Specifies the prefix for a command used to communicate with horizontal scrollbars. When the view in the widget’s window changes (or whenever anything else occurs that could change the display in a scrollbar, such as a change in the total size of the widget’s contents), the widget will generate a command by concatenating the scroll command and two numbers. Each of the numbers is a fraction between 0 and 1, which indicates a position in the document. 0 indicates the beginning of the document, 1 indicates the end, .333 indicates a position one third of the way through the document, and so on. The first fraction indicates the first information in the document that is visible in the window, and the second fraction indicates the information just after the last portion that is visible. The command is then passed to the Tcl interpreter for execution.<br>Typically the xScrollCommand option consists of the identity of a scrollbar widget followed by set; for example, self.x.scrollbar set will cause the scrollbar to be updated whenever the view in the window changes. If this option is not specified, then no command will be executed.</td>
    <td>function</td>
    <td></td>
    <td>Canvas<br>Entry Listbox Text</td>
  </tr>
</table>