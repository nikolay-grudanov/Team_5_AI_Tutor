---
source_image: page_448.png
page_number: 448
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.34
tokens: 8757
characters: 2605
timestamp: 2025-12-24T00:44:25.353777
finish_reason: stop
---

Table A.85  Font methods

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>font actual fontDesc [-displayof window] [option]</td>
    <td>fontDesc.actual[option])</td>
  </tr>
  <tr>
    <td>font configure fontname [option [value option value ...]]</td>
    <td>fontname.configure([option=value ...])</td>
  </tr>
  <tr>
    <td>font create [fontname [option value ...]]</td>
    <td>font = Font([master] [, option=value ...])</td>
  </tr>
  <tr>
    <td>font delete fontname [fontname ...]</td>
    <td>del(fontname)</td>
  </tr>
  <tr>
    <td>font families [-displayof window]</td>
    <td>families([window])</td>
  </tr>
  <tr>
    <td>font measure fontDesc [-displayof window] text</td>
    <td>fontDesc.measure(text)</td>
  </tr>
  <tr>
    <td>font metrics fontDesc [-displayof window] [metric]</td>
    <td>fontDesc.metrics([metric])</td>
  </tr>
  <tr>
    <td>font names</td>
    <td>names([window])</td>
  </tr>
</table>

Other Tk commands

Table A.86  Other Tk methods

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>bell [-displayof window]</td>
    <td>window.bell([displayof=window])</td>
  </tr>
  <tr>
    <td>clipboard clear [-displayof window]</td>
    <td>window.clipbord_clear([displayof=window])</td>
  </tr>
  <tr>
    <td>clipboard append [-displayof win] [-format fmt] [-type type] data</td>
    <td>window.clipbord_clear(data [, option=value ...])</td>
  </tr>
  <tr>
    <td>destroy [window window ...]</td>
    <td>window.destroy()</td>
  </tr>
  <tr>
    <td>focus [-force] window</td>
    <td>window.focus_force()</td>
  </tr>
  <tr>
    <td>focus [-displayof window]</td>
    <td>window.focus_displayof()</td>
  </tr>
  <tr>
    <td>focus -lastfor window</td>
    <td>window.focus_lastfor()</td>
  </tr>
  <tr>
    <td>grab current [window]</td>
    <td>window.grab_current()</td>
  </tr>
  <tr>
    <td>grab release window</td>
    <td>window.grab_release()</td>
  </tr>
  <tr>
    <td>grab set window</td>
    <td>window.grab_set()</td>
  </tr>
  <tr>
    <td>grab set -global window</td>
    <td>window.grab_set_global()</td>
  </tr>
  <tr>
    <td>grab status window</td>
    <td>window.grab_status()</td>
  </tr>
  <tr>
    <td>lower window [belowThis]</td>
    <td>window.lower([belowThis])</td>
  </tr>
  <tr>
    <td>option add pattern value [priority]</td>
    <td>window.option_add(pattern, value, [, priority])</td>
  </tr>
  <tr>
    <td>option clear</td>
    <td>window.option clear()</td>
  </tr>
  <tr>
    <td>option get window name class</td>
    <td>window.option_get(name, class)</td>
  </tr>
</table>