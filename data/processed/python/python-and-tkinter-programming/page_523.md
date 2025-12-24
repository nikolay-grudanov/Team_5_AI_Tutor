---
source_image: page_523.png
page_number: 523
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.19
tokens: 8577
characters: 2649
timestamp: 2025-12-24T00:46:48.262739
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>width</td>
    <td>20</td>
  </tr>
  <tr>
    <td>xscrollcommand</td>
    <td></td>
  </tr>
</table>

<h2>Options specific to Listbox</h2>

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>exportselection</td>
    <td>Specifies whether or not a selection in the widget should also be the X selection. The value may have any of the forms accepted by Tcl_GetBoolean, such as true, false, 0, 1, yes, or no. If the selection is exported, then selecting in the widget deselects the current X selection, selecting outside the widget deselects any widget selection, and the widget will respond to selection retrieval requests when it has a selection. The default is usually for widgets to export selections.</td>
    <td>boolean</td>
    <td>0 YES</td>
    <td>1</td>
  </tr>
  <tr>
    <td>selectmode</td>
    <td>Specifies one of several styles for manipulating the selection. The value of the option may be arbitrary, but the default bindings expect it to be either SINGLE, BROWSE, MULTIPLE, or EXTENDED; the default value is BROWSE.</td>
    <td>constant</td>
    <td>SINGLE "browse"</td>
    <td>browse</td>
  </tr>
  <tr>
    <td>setgrid</td>
    <td>Specifies a boolean value that determines whether this widget controls the resizing grid for its top-level window. This option is typically used in text widgets, where the information in the widget has a natural size (the size of a character) and it makes sense for the window’s dimensions to be integral numbers of these units. These natural window sizes form a grid. If the setGrid option is set to true then the widget will communicate with the window manager so that when the user interactively resizes the top-level window that contains the widget, the dimensions of the window will be displayed to the user in grid units and the window size will be constrained to integral numbers of grid units. See the section “Gridded geometry management” in the wm entry in the Tkman pages for more details.</td>
    <td>boolean</td>
    <td>NO 1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>yscrollcommand</td>
    <td>Specifies the prefix for a command used to communicate with vertical scrollbars. This option is treated in the same way as the xScrollCommand option, except that it is used for vertical scrollbars and is provided by widgets that support vertical scrolling. See the description of xScrollCommand for details on how this option is used.</td>
    <td>function</td>
    <td></td>
    <td></td>
  </tr>
</table>