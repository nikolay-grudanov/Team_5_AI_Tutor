---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.69
tokens: 8440
characters: 2862
timestamp: 2025-12-24T00:40:42.049350
finish_reason: stop
---

There are advantages and disadvantages for both models. Many users like the pointer model, since a simple movement of the mouse positions the pointer and requires no clicking. However, if the mouse is accidentally moved, the keyboard events may be directed to an unintended widget. The explicit model requires the user to click on every window and widget that focus is to be directed to. However, even if the pointer moves out of the widget, keyboard events are directed to it. On Win32 and MacOS, explicit focus is the default, whereas on UNIX, pointer focus is the default.

Tk (and therefore Tkinter) implements an explicit model within a given top-level shell, regardless of how the window manager is configured. However, within the application, the window manager is capable of overriding focus to handle system-level operations, so focus can be lost.

12.2 Mouse navigation

Most computer users are familiar with using the mouse to select actions and objects on the screen. However, there are times when stopping keyboard input to move the mouse is inconvenient; a touch typist will lose station and have to reestablish it before continuing. Therefore, it is usually a good idea to provide a sensible series of tab groups which allow the user to move from widget to widget and area to area in the GUI. This is discussed in more detail in the next section.

When the mouse is used to select objects, you need to consider some important human factors:

1 Widget alignment is important. If widgets are arranged aimlessly on the screen, additional dexterity is needed to position the mouse. Widgets arranged in rows and columns typically allow movement in one or two axes to reposition the pointer.
2 The clickable components of a widget need to be big enough to ensure that the user does not have to reposition the pointer to hit a target. However, this may interfere with the GUI’s visual effectiveness.
3 Ensure that there is space between widgets so that the user cannot accidentally choose an adjacent widget.
4 Remember that not all pointing devices are equal. While a mouse can be easy to use to direct the pointer to a clickable area, some of the mouse buttons (the little buttons embedded in the keyboard on certain laptop computers) can be difficult to control.

Unless Tkinter (Tk) is directed to obey strict Motif rules, it has a useful property that allows it to change the visual attributes of many widgets as the pointer enters the widgets. This can provide valuable feedback to the user that a widget has been located.

12.3 Keyboard navigation: “mouseless navigation”

It is easy to forget to provide alternate navigation methods. If you, as the programmer, are used to using the mouse to direct focus, you may overlook mouseless navigation. However, there are times when the ability to use Tab or Arrow keys to get around a GUI are important.