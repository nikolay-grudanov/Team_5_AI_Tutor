---
source_image: page_595.png
page_number: 595
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.39
tokens: 8457
characters: 2456
timestamp: 2025-12-24T00:48:51.490010
finish_reason: stop
---

The currently active windows form a stack with the most recently activated window at the top of the stack. All mouse and keyboard events are sent to this top window. When it deactivates, the next window in the stack will start to receive events.

Inheritance

MegaToplevel inherits from Pmw.MegaArchetype.

MegaToplevel options

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
    <td>title</td>
    <td>This is the title that the window manager displays in the title bar of the window.</td>
    <td>string</td>
    <td>None</td>
  </tr>
</table>

Components

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

Methods

activate(globalMode = 0, master = None, geometry = 'centerscreenfirst')
Displays the window as a modal dialog. This means that all mouse and keyboard events go to this window and no other windows can receive any events. If you do not want to restrict mouse and keyboard events to this window, use the show() method instead. The activate() method does not return until the deactivate() method is called, when the window is withdrawn, the grab is released and the result is returned.

If globalMode is false, the window will grab control of the pointer and keyboard, preventing any events from being delivered to any other toplevel windows within the application. If globalMode is true, the grab will prevent events from being delivered to any other toplevel windows regardless of application. Global grabs should be used sparingly.

When the window is displayed, it is positioned on the screen according to geometry which may be one of the following:

• centerscreenfirst   The window will be centered the first time it is activated. On subsequent activations it will be positioned in the same position as the last time it was displayed, even if it has been moved by the user.
• centerscreenalway   The window will be centered on the screen (halfway across and one-third down).