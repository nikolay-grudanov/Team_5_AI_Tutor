---
source_image: page_470.png
page_number: 470
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.77
tokens: 8294
characters: 1989
timestamp: 2025-12-24T00:44:54.429184
finish_reason: stop
---

winfo_visualid()
Returns the X identifier for the visual for window.

winfo_visualsavailable(includeids=0)
Returns a list whose elements describe the visuals available for window’s screen. Each element consists of a visual class followed by an integer depth. The class has the same form as returned by winfo_visual. The depth gives the number of bits per pixel in the visual. In addition, if the includeids argument is provided, then the depth is followed by the X identifier for the visual.

winfo_vrootheight()
Returns the height of the virtual root window associated with window if there is one; otherwise returns the height of window’s screen.

winfo_vrootwidth()
Returns the width of the virtual root window associated with window if there is one; otherwise returns the width of window’s screen.

winfo_vrootx()
Returns the x-offset of the virtual root window associated with window, relative to the root window of its screen. This is normally either zero or negative. Returns 0 if there is no virtual root window for window.

winfo_vrooty()
Returns the y-offset of the virtual root window associated with window, relative to the root window of its screen. This is normally either zero or negative. Returns 0 if there is no virtual root window for window.

winfo_width()
Returns an integer giving window’s width in pixels. When a window is first created its width will be 1 pixel; the width will eventually be changed by a geometry manager to fulfill the window’s needs. If you need the true width immediately after creating a widget, invoke update to force the geometry manager to arrange it, or use winfo_reqwidth to get the window’s requested width instead of its actual width.

winfo_x()
Returns an integer giving the x-coordinate, in window’s parent, of the upper left corner of window’s border (or window if it has no border).

winfo_y()
Returns an integer giving the y-coordinate, in window’s parent, of the upper left corner of window’s border (or window if it has no border).