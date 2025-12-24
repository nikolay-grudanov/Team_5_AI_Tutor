---
source_image: page_467.png
page_number: 467
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.35
tokens: 8379
characters: 2335
timestamp: 2025-12-24T00:44:56.759309
finish_reason: stop
---

(Tk_GetScreenMM), such as 2.0c or 1i. The return value may be fractional; for an integer value, use winfo_pixels.

winfo_geometry()
Returns the geometry for window, in the form widthxheight+x+y. All dimensions are in pixels.

winfo_height()
Returns an integer giving window’s height in pixels. When a window is first created its height will be 1 pixel; the height will eventually be changed by a geometry manager to fulfill the window’s needs. If you need the true height immediately after creating a widget, invoke update to force the geometry manager to arrange it, or use winfo_reqheight to get the window’s requested height instead of its actual height.

winfo_id()
Returns an integer giving a low-level platform-specific identifier for window. On Unix platforms, this is the X window identifier. Under Windows, this is the Windows HWND. On the Macintosh the value has no meaning outside Tk.

winfo_interps(displayof=0)
Returns a list whose members are the names of all Tcl interpreters (e.g. all Tk-based applications) currently registered for a particular display. If the displayof option is given then the return value refers to the display of window; otherwise it refers to the display of the application’s main window. This may be of limited use to Tkinter applications.

winfo_ismapped()
Returns TRUE if self is currently mapped, FALSE otherwise.

winfo_manager()
Returns the name of the geometry manager currently responsible for self’s window, or an empty string if window isn’t managed by any geometry manager. The name is usually the name of the Tcl method for the geometry manager, such as pack or place. If the geometry manager is a widget, such as canvases or text, the name is the widget’s class, such as canvas.

winfo_name()
Returns window’s name (i.e. its name within its parent, as opposed to its full path name).

winfo_parent()
Returns the path name of window’s parent, or an empty string if window is the main window of the application.

winfo_pathname(id, displayof=0)
Returns the path name of the window whose X identifier is id. id must be a decimal, hexadecimal or octal integer and must correspond to a window in the invoking application. If the displayof option is given then the identifier is looked up on the display of window; otherwise it is looked up on the display of the application’s main window.