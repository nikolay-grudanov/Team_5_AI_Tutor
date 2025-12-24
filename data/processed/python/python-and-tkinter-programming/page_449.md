---
source_image: page_449.png
page_number: 449
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.01
tokens: 8876
characters: 3071
timestamp: 2025-12-24T00:44:35.497811
finish_reason: stop
---

Table A.86  Other Tk methods (continued)

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>option readfile fileName [priority]</td>
    <td>window.option_readfile(fileName [, priority])</td>
  </tr>
  <tr>
    <td>raise window [aboveThis]</td>
    <td>window.raise([aboveThis])</td>
  </tr>
  <tr>
    <td>selection clear [-displayof window] [-selection selection]</td>
    <td>window.selection_clear([displayof=window] [, selection=sel])</td>
  </tr>
  <tr>
    <td>selection get [-displayof window] [-selection selection] [-type type]</td>
    <td>window.selection_get([displayof=window] [, -selection=sel][, type=type])</td>
  </tr>
  <tr>
    <td>selection handle [-selection sel] [-type type] [-format fmt] win cmd</td>
    <td>window.selection_handle(cmd [, selection=sel] [, type=type] [, format= fmt])</td>
  </tr>
  <tr>
    <td>selection own [-displayof window] [-selection selection]</td>
    <td>window.selection_own([displayof=window] [, selection=sel])</td>
  </tr>
  <tr>
    <td>selection own [-selection selection] [-command command] window</td>
    <td>window.selection_own_get([selection=sel] [command= command])</td>
  </tr>
  <tr>
    <td>send [-displayof window] [-async] interp cmd [arg arg ...]</td>
    <td>window.send(interp, cmd [, arg ...])</td>
  </tr>
  <tr>
    <td>tk appname [newName]</td>
    <td>No mapping</td>
  </tr>
  <tr>
    <td>tk scaling [-displayof window] [floatNumber]</td>
    <td>No mapping</td>
  </tr>
  <tr>
    <td>tkwait variable varName</td>
    <td>window.wait_variable([window])</td>
  </tr>
  <tr>
    <td>tkwait visibility window</td>
    <td>window.wait_variablevisibility([window])</td>
  </tr>
  <tr>
    <td>tkwait window window</td>
    <td>window.wait_window([window])</td>
  </tr>
  <tr>
    <td>tk_bisque</td>
    <td>window.tk_bisque()</td>
  </tr>
  <tr>
    <td>tk_chooseColor [option value ...]</td>
    <td>Use tkColorChooser</td>
  </tr>
  <tr>
    <td>tk_dialog topw title text bitmap default string [string ...]</td>
    <td>Use Dialog</td>
  </tr>
  <tr>
    <td>tk_focusNext window</td>
    <td>window.tk_focusNext()</td>
  </tr>
  <tr>
    <td>tk_focusPrev window</td>
    <td>window.tk_focusPrev()</td>
  </tr>
  <tr>
    <td>tk_focusFollowsMouse</td>
    <td>window.tk_focusFollowsMouse()</td>
  </tr>
  <tr>
    <td>tk_getOpenFile [option value ...]</td>
    <td>No mapping</td>
  </tr>
  <tr>
    <td>tk_getSaveFile [option value ...]</td>
    <td>No mapping</td>
  </tr>
  <tr>
    <td>tk_messageBox [option value ...]</td>
    <td>box=MessageBox(master, text=text [, option ...])</td>
  </tr>
  <tr>
    <td>tk_optionMenu w varName value [value ...]</td>
    <td>menu = OptionMenu(master, varName, value [, value ...])</td>
  </tr>
  <tr>
    <td>tk_popup menu x y [entry]</td>
    <td>menu.tk_popup(x, y [, entry] )</td>
  </tr>
  <tr>
    <td>tk_setPalette color</td>
    <td>window.tk_setPalette(color)</td>
  </tr>
  <tr>
    <td>tk_setPalette name color [name color ...]</td>
    <td>window.tk_setPalette(name=color [, name=color ...])</td>
  </tr>
</table>