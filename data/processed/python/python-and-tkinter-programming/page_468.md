---
source_image: page_468.png
page_number: 468
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.01
tokens: 8368
characters: 2262
timestamp: 2025-12-24T00:44:56.654580
finish_reason: stop
---

winfo_pixels(number)
Returns the number of pixels in window corresponding to the distance given by number. number may be specified in any of the forms acceptable to Tkinter (Tk_GetPixels), such as 2.0c or 1i. The result is rounded to the nearest integer value; for a fractional result, use winfo_fpixels.

winfo_pointerx()
If the mouse pointer is on the same screen as window, returns the pointer’s x coordinate, measured in pixels in the screen’s root window. If a virtual root window is in use on the screen, the position is measured in the virtual root. If the mouse pointer isn’t on the same screen as window then -1 is returned.

winfo_pointerxy()
If the mouse pointer is on the same screen as window, returns a tuple with two elements, which are the pointer’s x and y coordinates measured in pixels in the screen’s root window. If a virtual root window is in use on the screen, the position is computed in the virtual root. If the mouse pointer isn’t on the same screen as window then both of the returned coordinates are -1.

winfo_pointery()
If the mouse pointer is on the same screen as window, returns the pointer’s y coordinate, measured in pixels in the screen’s root window. If a virtual root window is in use on the screen, the position is computed in the virtual root. If the mouse pointer isn’t on the same screen as window then -1 is returned.

winfo_reqheight()
Returns an integer giving window’s requested height, in pixels. This is the value used by window’s geometry manager to compute its geometry.

winfo_reqwidth()
Returns an integer giving window’s requested width, in pixels. This is the value used by window’s geometry manager to compute its geometry.

winfo_rgb(color)
Returns a tuple containing three decimal values, which are the red, green, and blue intensities that correspond to color in the window given by window. Color may be specified in any of the forms acceptable for a color option.

winfo_rootx()
Returns an integer giving the x-coordinate, in the root window of the screen, of the upper-left corner of window’s border (or window if it has no border).

winfo_rooty()
Returns an integer giving the y-coordinate, in the root window of the screen, of the upper-left corner of window’s border (or window if it has no border).