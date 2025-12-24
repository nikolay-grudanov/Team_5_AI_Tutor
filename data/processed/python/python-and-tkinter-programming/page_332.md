---
source_image: page_332.png
page_number: 332
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.31
tokens: 8301
characters: 2176
timestamp: 2025-12-24T00:40:45.366546
finish_reason: stop
---

1 Management of windows (obviously!): placement, sizing, iconizing and maximizing, for example.
2 Appearance and behavior of windows and the relationship of windows in an application.
3 Management of one or more screens.
4 Keyboard focus control.
5 Window decoration: titles, controls, menus, size and position controls.
6 Icons and icon management (such as iconboxes and system tray).
7 Overall keybindings (before application bindings).
8 Overall mouse bindings.
9 Root-window menus.
10 Window stacking and navigation.
11 Default behavior and client resources (.XDefaults).
12 Size and position negotiation with windowing primitives (geometry managers).
13 Device configuration: mouse double-click time, keyboard repeat and movement thresholds, for example.

Not all window managers support the same features or behave in the same way. However, Tkinter supports a number of window-manager-related facilities which may support your application. Naturally, the names of the facilities are oriented to Tk, so you may not recognize other manager’s names immediately.

13.2 Geometry methods

Geometry methods are used to position and size windows and to set resize behavior. It is important to note that these are requests to the window manager to allocate a given amount of space or to position the window at a particular screen position. There is no guarantee that the window manager will observe the request, since overriding factors may prevent it from happening. In general, if you get no apparent effect from geometry methods, you are probably requesting something that the window manager cannot grant or you are requesting it at the wrong time (either before window realization or too late).

You normally apply window manager methods to the TopLevel widget.

To control the size and position of a window use geometry, giving a single string as the argument in the format:

widthxheight+xoffset+yoffset
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

Note that it is valid to supply either widthxheight or +xoffset+yoffset as separate arguments if you just want to set those parameters.

Without arguments, self.geometry() returns a string in the format shown above.