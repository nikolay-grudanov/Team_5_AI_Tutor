---
source_image: page_565.png
page_number: 565
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.89
tokens: 8557
characters: 2546
timestamp: 2025-12-24T00:48:04.171721
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>class</td>
    <td>Specifies a class for the window. This class will be used when querying the option database for the window’s other options, and it will also be used later for other purposes such as bindings. The class option may not be changed with the configure method. Note that because class is a reserved word, _class must be used with Tkinter.</td>
    <td>class</td>
    <td></td>
    <td>Toplevel</td>
  </tr>
  <tr>
    <td>colormap</td>
    <td>Specifies a colormap to use for the window. The value may be either NEW, in which case a new colormap is created for the window and its children, or the name of another window (which must be on the same screen and have the same visual as pathName), in which case the new window will use the colormap from the specified window. If the colormap option is not specified, the new window uses the same colormap as its parent. This option may not be changed with the configure method.</td>
    <td>colormap</td>
    <td>NEW myWindow</td>
    <td></td>
  </tr>
  <tr>
    <td>container</td>
    <td>The value must be a boolean. If TRUE, it means that this window will be used as a container in which some other application will be embedded (for example, a Tkinter toplevel can be embedded using the use option). The window will support the appropriate window manager protocols for things like geometry requests. The window should not have any children of its own in this application. This option may not be changed with the configure method.</td>
    <td>boolean</td>
    <td>TRUE 0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>menu</td>
    <td>Specifies the pathname of the menu associated with a menubutton. The menu must be a child of the menubutton.</td>
    <td>string</td>
    <td>subMenuAction</td>
    <td></td>
  </tr>
  <tr>
    <td>screen</td>
    <td>Specifies the screen on which to place the new window. Any valid screen name may be used, even one associated with a different display. Defaults to the same screen as its parent. This option is special in that it may not be specified via the option database, and it may not be modified with the configure method.</td>
    <td>screen</td>
    <td>"Default"</td>
    <td></td>
  </tr>
  <tr>
    <td>use</td>
    <td>Specifies the value to store in the widget’s associated Tkinter variable whenever the widget is selected.</td>
    <td>string</td>
    <td></td>
    <td></td>
  </tr>
</table>