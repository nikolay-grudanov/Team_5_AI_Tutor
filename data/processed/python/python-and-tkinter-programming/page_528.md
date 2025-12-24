---
source_image: page_528.png
page_number: 528
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.73
tokens: 8402
characters: 2017
timestamp: 2025-12-24T00:46:44.567277
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
    <td>tearoffcommand</td>
    <td>If this option has a non-empty value, then it specifies a Tkinter command to invoke whenever the menu is torn off. The actual command will consist of the value of this option, followed by a space, followed by the name of the menu window, followed by a space, followed by the name of the torn-off menu window.</td>
    <td>command</td>
    <td>myTearoff</td>
    <td></td>
  </tr>
  <tr>
    <td>title</td>
    <td>The string will be used to title the window created when a shell is created or a menu is torn off. For menus, if the title is NULL, then the window will have the title of the menubutton or the text of the cascade item from which this menu was invoked.</td>
    <td>string</td>
    <td>"Widget Table"</td>
    <td></td>
  </tr>
  <tr>
    <td>type</td>
    <td>This option can be one of MENUBAR, TEAROFF, or NORMAL, and it is set when a menu is created. While the string returned by the configuration database will change if this option is changed, this does not affect the menu widget’s behavior. This is used by the cloning mechanism and is not normally set outside of the Tk library.</td>
    <td>constant</td>
    <td>NORMAL</td>
    <td>normal</td>
  </tr>
</table>

Methods

add_cascade(options...)
Adds a new cascade to the bottom of the menu.

add_checkbutton(options...)
Adds a new checkbutton to the bottom of the menu.

add_command(options...)
Adds a new command to the bottom of the menu.

add_radiobutton(options...)
Adds a new radiobutton to the bottom of the menu.

add_separator(options...)
Adds a new separator to the bottom of the menu.

delete(index1, index2=None)
Deletes all of the menu entries between index1 and index2 inclusive. If index2 is omitted then it defaults to index1. Attempts to delete a tear-off menu entry are ignored (instead, you should change the tearOff option to remove the tear-off entry).