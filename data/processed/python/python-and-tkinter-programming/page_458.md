---
source_image: page_458.png
page_number: 458
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.28
tokens: 8375
characters: 2294
timestamp: 2025-12-24T00:44:31.955904
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
    <td>yscrollcommand</td>
    <td>Specifies the prefix for a command function used to communicate with vertical scrollbars. When the view in the widget’s window changes (or whenever anything else occurs that could change the display in a scrollbar, such as a change in the total size of the widget’s contents), the widget will generate a command by concatenating the scroll command and two numbers. Each of the numbers is a fraction between 0 and 1, which indicates a position in the document. 0 indicates the beginning of the document, 1 indicates the end, .333 indicates a position one third of the way through the document, and so on. The first fraction indicates the first information in the document that is visible in the window, and the second fraction indicates the information just after the last portion that is visible. The command is then passed to the Tcl interpreter for execution.<br>Typically the yScrollCommand option consists of the identity of a scrollbar widget followed by set; for example, self.y.scrollbar set will cause the scrollbar to be updated whenever the view in the window changes. If this option is not specified, then no command will be executed.</td>
    <td></td>
    <td></td>
    <td>Canvas<br>Entry Listbox Text</td>
  </tr>
</table>

Inherited methods

Many methods are inherited from the bases classes and are available to all widgets. In addition to the methods listed here, grid, pack and place geometry manager methods are inherited by all widgets. These methods are documented separately from the widgets.

The arguments to the methods are presented in the form that Tkinter defines them. You will find a mapping to Tk commands here; typically Tk commands have the window as the first argument. Tkinter methods are applied to the current instance of a widget which may be interpreted as the window or slave or master arguments in Tk commands.

Common widget methods

after(ms, function=None, *args)
Registers a callback that is called after ms milliseconds. Note that this period is not guaranteed to be accurate; you must assume that the wait period is at least the given period and it can be