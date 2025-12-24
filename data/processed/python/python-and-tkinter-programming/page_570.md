---
source_image: page_570.png
page_number: 570
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.67
tokens: 8515
characters: 2251
timestamp: 2025-12-24T00:48:11.213838
finish_reason: stop
---

Balloon

Description
This class implements a balloon help system and provides a mechanism to supply the same (or different) messages to a status area, if present. It is good practice to provide a mechanism for the user to turn off such messages if they are not required.

Inheritance
Balloon inherits from Pmw.MegaToplevel.

Balloon options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activatecommand</td>
    <td>If this is callable, it will be called whenever the megawidget is activated by a call to activate().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>deactivatecommand</td>
    <td>If this is callable, it will be called whenever the megawidget is deactivated by a call to deactivate().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>initwait</td>
    <td>The time to wait, in milliseconds, after the pointer has entered the widget before the balloon is displayed.</td>
    <td>milliseconds</td>
    <td>500</td>
  </tr>
  <tr>
    <td>state</td>
    <td>Determines whether balloon help or status messages are displayed. May be none, balloon, status or both.</td>
    <td>constant</td>
    <td>'both'</td>
  </tr>
  <tr>
    <td>statuscommand</td>
    <td>If this is callable, it will be called whenever the status message is to be updated. This will normally be a call to a Pmw.MessageBar's helpmessage method.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>title</td>
    <td>This is the title that the window manager displays in the title bar of the window.</td>
    <td>string</td>
    <td>None</td>
  </tr>
  <tr>
    <td>xoffset</td>
    <td>Horizontal offset for the balloon help widget. Starts at the bottom left-hand corner of the associated widget's bounding box.</td>
    <td>distance</td>
    <td>20</td>
  </tr>
  <tr>
    <td>yoffset</td>
    <td>Vertical offset for the balloon help widget. Starts at the bottom left-hand corner of the associated widget's bounding box.</td>
    <td>distance</td>
    <td>1</td>
  </tr>
</table>

Components

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.