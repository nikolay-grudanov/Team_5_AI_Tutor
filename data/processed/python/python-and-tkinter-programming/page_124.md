---
source_image: page_124.png
page_number: 124
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 93.07
tokens: 9397
characters: 4059
timestamp: 2025-12-24T00:35:51.758686
finish_reason: stop
---

event mask). Many events may be entered in a shorthand form. For example, <Key-a>, <Key-Press-a>, and a are all acceptable event identifiers for pressing a lower-case a.

Here are some of the more commonly used events. You will find a complete list of events and keysyms in “Events and keysyms” on page 617

<table>
  <tr>
    <th>Event</th>
    <th>Alt. 1</th>
    <th>Alt2</th>
    <th>Mod</th>
    <th>Type</th>
    <th>Qualifier</th>
    <th>Action to generate event</th>
  </tr>
  <tr>
    <td>&lt;Any-Enter&gt;</td>
    <td></td>
    <td></td>
    <td>Any</td>
    <td>Enter</td>
    <td></td>
    <td>Enter event regardless of mode.</td>
  </tr>
  <tr>
    <td>&lt;Button-1&gt;</td>
    <td>ButtonPress-1</td>
    <td>1</td>
    <td></td>
    <td>Button</td>
    <td>1</td>
    <td>Left mouse button click.</td>
  </tr>
  <tr>
    <td>&lt;Button-2&gt;</td>
    <td>ButtonPress-2</td>
    <td>2</td>
    <td></td>
    <td>ButtonPress</td>
    <td>1</td>
    <td>Middle mouse button click.</td>
  </tr>
  <tr>
    <td>&lt;B2-Motion&gt;</td>
    <td></td>
    <td></td>
    <td>B1</td>
    <td>Motion</td>
    <td></td>
    <td>Mouse movement with middle mouse button down.</td>
  </tr>
  <tr>
    <td>&lt;ButtonRelease-3&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>ButtonRelease</td>
    <td>3</td>
    <td>Release third mouse button 3.</td>
  </tr>
  <tr>
    <td>&lt;Configure&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Configure</td>
    <td></td>
    <td>Size stacking or position has changed.</td>
  </tr>
  <tr>
    <td>&lt;Control-Insert&gt;</td>
    <td></td>
    <td></td>
    <td>Control</td>
    <td>Insert</td>
    <td></td>
    <td>Press INSERT key with CONTROL key down.</td>
  </tr>
  <tr>
    <td>&lt;Control-Shift-F3&gt;</td>
    <td></td>
    <td></td>
    <td>Control-Shift</td>
    <td></td>
    <td>F3</td>
    <td>Press CONTROL-SHIFT and F3 keys simultaneously.</td>
  </tr>
  <tr>
    <td>&lt;Destroy&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Destroy</td>
    <td></td>
    <td>Window is being destroyed.</td>
  </tr>
  <tr>
    <td>&lt;Double-Button-1&gt;</td>
    <td></td>
    <td></td>
    <td>Double</td>
    <td>Button</td>
    <td>1</td>
    <td>Double-click first mouse button 1.</td>
  </tr>
  <tr>
    <td>&lt;Enter&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Enter</td>
    <td></td>
    <td>Cursor enters window.</td>
  </tr>
  <tr>
    <td>&lt;Expose&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Expose</td>
    <td></td>
    <td>Window fully or partially exposed.</td>
  </tr>
  <tr>
    <td>&lt;FocusIn&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>FocusIn</td>
    <td></td>
    <td>Widget gains focus.</td>
  </tr>
  <tr>
    <td>&lt;FocusOut&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>FocusOut</td>
    <td></td>
    <td>Widget loses focus.</td>
  </tr>
  <tr>
    <td>&lt;KeyPress&gt;</td>
    <td>Key</td>
    <td></td>
    <td></td>
    <td>KeyPress</td>
    <td></td>
    <td>Any key has been pressed.</td>
  </tr>
  <tr>
    <td>&lt;KeyRelease-backslash&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>KeyRelease</td>
    <td>backslash</td>
    <td>Backslash key has been released.</td>
  </tr>
  <tr>
    <td>&lt;Leave&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Leave</td>
    <td></td>
    <td>Cursor leaves window.</td>
  </tr>
  <tr>
    <td>&lt;Map&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Map</td>
    <td></td>
    <td>Window has been mapped.</td>
  </tr>
  <tr>
    <td>&lt;Print&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Print</td>
    <td></td>
    <td>PRINT key has been pressed.</td>
  </tr>
  <tr>
    <td>Z</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Print</td>
    <td>Z</td>
    <td>Capital Z has been pressed.</td>
  </tr>
</table>

Let’s take a look at some example code that allows us to explore the event mechanism as it’s supported by Tkinter.

Example_6_2.py

from Tkinter import *
import Pmw

eventDict = {