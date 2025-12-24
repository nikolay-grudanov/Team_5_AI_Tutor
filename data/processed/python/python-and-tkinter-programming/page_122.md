---
source_image: page_122.png
page_number: 122
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.29
tokens: 8613
characters: 2884
timestamp: 2025-12-24T00:34:59.358218
finish_reason: stop
---

6.1.2 Event propagation

Events occur relative to a window, which is usually described as the source window of the event. If no client has registered for a particular event for the source window, the event is propagated up the window hierarchy until it either finds a window that a client has registered with, it finds a window that prohibits event propagation or it reaches the root window. If it does reach the root window, the event is ignored.

Only device events that occur as a result of a key, pointer motion or mouse click are propagated. Other events, such as exposure and configuration events, have to be registered for explicitly.

6.1.3 Event types

Events are grouped into several categories depending on X event masks. Tk maps Windows events to the same masks when running on a Windows architecture. The event masks recognized by Tk (and therefore Tkinter) are shown in table 6.1.

Table 6.1 Event masks used to group X events

<table>
  <tr>
    <th>NoEventMask</th>
    <th>StructureNotifyMask</th>
    <th>Button3MotionMask</th>
  </tr>
  <tr>
    <td>KeyReleaseMask</td>
    <td>SubstructureNotifyMask</td>
    <td>Button5MotionMask</td>
  </tr>
  <tr>
    <td>ButtonReleaseMask</td>
    <td>FocusChangeMask</td>
    <td>KeymapStateMask</td>
  </tr>
  <tr>
    <td>LeaveWindowMask</td>
    <td>ColormapChangeMask</td>
    <td>VisibilityChangeMask</td>
  </tr>
  <tr>
    <td>PointerMotionHintMask</td>
    <td>KeyPressMask</td>
    <td>ResizeRedirectMask</td>
  </tr>
  <tr>
    <td>Button2MotionMask</td>
    <td>ButtonPressMask</td>
    <td>SubstructureRedirectMask</td>
  </tr>
  <tr>
    <td>Button4MotionMask</td>
    <td>EnterWindowMask</td>
    <td>PropertyChangeMask</td>
  </tr>
  <tr>
    <td>ButtonMotionMask</td>
    <td>PointerMotionMask</td>
    <td>OwnerGrabButtonMask</td>
  </tr>
  <tr>
    <td>ExposureMask</td>
    <td>Button1MotionMask</td>
    <td></td>
  </tr>
</table>

Keyboard events
Whenever a key is pressed, a KeyPress event is generated, and whenever a key is released, a KeyRelease event is generated. Modifier keys, such as SHIFT and CONTROL, generate keyboard events.

Pointer events
If buttons on the mouse are pressed or if the mouse is moved, ButtonPress, ButtonRelease and MotionNotify events are generated. The window associated with the event is the lowest window in the hierarchy unless a pointer grab exists, in that case, the window that initiated the grab will be identified. Like keyboard events, modifier keys may be combined with pointer events.

Crossing events
Whenever the pointer enters or leaves a window boundary, an EnterNotify or LeaveNotify event is generated. It does not matter whether the crossing was a result of moving the pointer or because of a change in the stacking order of the windows. For example, if a window containing the pointer is lowered behind another window, and the pointer now is in the top