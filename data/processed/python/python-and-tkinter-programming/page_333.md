---
source_image: page_333.png
page_number: 333
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.34
tokens: 8328
characters: 2160
timestamp: 2025-12-24T00:40:51.619964
finish_reason: stop
---

Note In general, you should issue geometry requests at most only once when a window is first drawn. It is not good practice to change the position of windows under program control; such positioning should be left for the user to decide using the window manager controls.

Setting the minimum and maximum dimensions of a window is often a good idea. If you have designed an application which has a complex layout, it may be inappropriate to provide the user with the ability to resize the window. In fact, it may be impossible to maintain the integrity of a GUI if you do not limit this ability. However, Tkinter GUIs using the Pack or Grid geometry managers are much easier to configure than equivalent X window GUIs.

window.maxsize(width, height)
window.minsize(width, height)

window.minsize() and window.maxsize() with no arguments return a tuple (width, height).

You may control the resize capability using the resizable method. The method takes two boolean flags; setting either the width or height flags to false inhibits the resizing of the corresponding dimension:

resizable(1, 0)      # allow width changes only
resizable(0, 0)      # do not allow resizing in either dimension

13.3 Visibility methods

Window managers usually provide the ability to iconify windows so that the user can declutter the workspace. It is often appropriate to change the state of the window under program control. For example, if the user requests a window which is currently iconified, we can deiconify the window on his behalf. For reasons which will be explained in “Programming for performance” on page 348, it is usually better to draw complex GUIs with the window hidden; this results in faster window-creation speeds.

To iconify a window, use the iconify method:

root.iconify()

To hide a window, use the withdraw method:

self.toplevel.withdraw()

You can find out the current state of a window using the state method. This returns a string which is one of the following values: normal (the window is currently realized), iconic (the window has been iconified), withdrawn (the window is hidden), or icon (the window is an icon).

state = self.toplevel.state()