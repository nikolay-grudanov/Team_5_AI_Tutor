---
source_image: page_466.png
page_number: 466
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.43
tokens: 8338
characters: 2265
timestamp: 2025-12-24T00:44:49.898544
finish_reason: stop
---

the atom is looked up on the display of window; otherwise it is looked up on the display of the application’s main window.

winfo_atomname(id, displayof=0)
Returns the textual name for the atom whose integer identifier is id. If the displayof option is given then the identifier is looked up on the display of window; otherwise it is looked up on the display of the application’s main window. This method is the inverse of the winfo_atom method. It generates an error if no such atom exists.

winfo_cells()
Returns an integer giving the number of cells in the color map for the window.

winfo_children()
Returns a list containing the path names of all the children of window. The list is in stacking order, with the lowest window first. Top-level windows are returned as children of their logical parents.

winfo_class()
Returns the class name for window.

winfo_colormapfull()
Returns TRUE if the colormap for the window is known to be full, FALSE otherwise. The colormap for a window is “known” to be full if the last attempt to allocate a new color on that window failed and this application hasn’t freed any colors in the colormap since the failed allocation.

winfo_containing(rootX, rootY, displayof=0)
Returns the identity of the window containing the point given by rootX and rootY. rootX and rootY are specified in screen units in the coordinate system of the root window (if a virtual-root window manager is in use then the coordinate system of the virtual root window is used). If the displayof option is given then the coordinates refer to the screen containing the window; otherwise they refer to the screen of the application’s main window. If no window in this application contains the point then None is returned. In selecting the containing window, children are given higher priority than parents and among siblings the highest one in the stacking order is chosen.

winfo_depth()
Returns an integer giving the depth of window (number of bits per pixel).

winfo_exists()
Returns TRUE if a window exists for self, FALSE if no such window exists.

winfo_fpixels(number)
Returns a floating-point value giving the number of pixels in window corresponding to the distance given by number. number may be specified in any of the forms acceptable to Tkinter