---
source_image: page_473.png
page_number: 473
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.70
tokens: 8477
characters: 2952
timestamp: 2025-12-24T00:45:05.250640
finish_reason: stop
---

border and the bottom of the screen. If newGeometry is specified as an empty string then any existing user-specified geometry for window is cancelled, and the window will revert to the size requested internally by its widgets.

group(pathName=None)
If pathname is specified, it gives the path name for the leader of a group of related windows. The window manager may use this information, for example, to unmap all of the windows in a group when the group’s leader is iconified. pathName may be specified as an empty string to remove window from any group association. If pathname is specified then the method returns an empty string; otherwise it returns the path name of window’s current group leader, or an empty string if window isn’t part of any group.

iconbitmap(bitmap=None)
If bitmap is specified, then it names a bitmap in the standard forms accepted by Tkinter (Tk_GetBitmap). This bitmap is passed to the window manager to be displayed in window’s icon, and the method returns an empty string. If bitmap is not specified, then any current icon bitmap is cancelled for window. If bitmap is specified then the method returns an empty string. Otherwise it returns the name of the current icon bitmap associated with window, or an empty string if window has no icon bitmap.

wm_iconify()
Arrange for window to be iconified. It window hasn’t yet been mapped for the first time, this method will arrange for it to appear in the iconified state when it is eventually mapped.

iconmask(bitmap=None)
If bitmap is specified, then it names a bitmap in the standard forms accepted by Tkinter (Tk_GetBitmap). This bitmap is passed to the window manager to be used as a mask in conjunction with the iconbitmap option: where the mask has zeroes no icon will be displayed; where it has ones, the bits from the icon bitmap will be displayed. If bitmap is not specified, then any current icon mask is cancelled for window (this is equivalent to specifying a bitmap of all ones). If bitmap is specified then the method returns an empty string. Otherwise it returns the name of the current icon mask associated with window, or an empty string if no mask is in effect.

iconname(newName=None)
If newName is specified, then it is passed to the window manager; the window manager should display newName inside the icon associated with window. In this case an empty string is returned as result. If newName isn’t specified then the method returns the current icon name for window, or an empty string if no icon name has been specified (in this case the window manager will normally display the window’s title, as specified with the wm_title call).

iconposition(x=None, y=None)
If x and y are specified, they are passed to the window manager as a hint about where to position the icon for window. In this case an empty string is returned. If x and y are specified as empty strings then any existing icon position hint is cancelled. If neither x nor y is specified,