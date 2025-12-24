---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.76
tokens: 8317
characters: 2204
timestamp: 2025-12-24T00:34:43.277396
finish_reason: stop
---

window, the lowered window receives a LeaveNotify event and the top window receives an EnterNotify event.

*Focus events*
The window which receives keyboard events is known as the *focus window*. FocusIn and FocusOut events are generated whenever the focus window changes. Handling focus events is a little more tricky than handling pointer events because the pointer does not necessarily have to be in the window that is receiving focus events. You do not usually have to handle focus events yourself, because setting takefocus to true in the widgets allows you to move focus between the widgets by pressing the TAB key.

*Exposure events*
Whenever a window or a part of a window becomes visible, an Exposure event is generated. You will not typically be managing exposure events in Tkinter GUIs, but you do have the ability to receive these events if you have some very specialized drawing to support.

*Configuration events*
When a window’s size, position or border changes, ConfigureNotify events are generated. A ConfigureNotify event will be created whenever the stacking order of the windows changes. Other types of configuration events include Gravity, Map/Unmap, Reparent and Visibility.

*Colormap events*
If a new colormap is installed, a ColormapNotify event is generated. This may be used by your application to prevent the annoying colormap flashing which can occur when another application installs a colormap. However, most applications do not control their colormaps directly.

6.2 *Tkinter events*

In general, handling events in Tkinter applications is considerably easier than doing the same in X/Motif, Win32 or QuickDraw. Tkinter provides convenient methods to bind callbacks to specific events.

6.2.1 *Events*

We express events as strings, using the following format:

<modifier-type-qualifier>

• modifier is optional and may be repeated, separated by spaces or a dash.
• type is optional if there is a qualifier.
• qualifier is either a *button-option* or a keysym and is optional if type is present.

Many events can be described using just type, so the modifier and qualifier may be left out. The type defines the class of event that is to be bound (in X terms it defines the