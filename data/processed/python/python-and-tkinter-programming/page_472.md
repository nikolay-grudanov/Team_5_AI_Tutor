---
source_image: page_472.png
page_number: 472
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.22
tokens: 8507
characters: 3157
timestamp: 2025-12-24T00:45:02.688587
finish_reason: stop
---

level window to all the internal windows whose colormaps differ from their parents, followed by the top-level itself; the order of the internal windows is undefined. See the ICCCM documentation for more information on the WM_COLORMAP_WINDOWS property.

command(callback=None)
Specifies a callback to associate with the button. This callback is typically invoked when mouse button 1 is released over the button window. This method is only useful for X systems.

deiconify()
Arranges for window to be displayed in normal (non-iconified) form. This is done by mapping the window. If the window has never been mapped then this method will not map the window, but it will ensure that when the window is first mapped it will be displayed in de-iconified form. Returns None.

focusmodel(model=None)
If active or passive is supplied as an optional model argument to the method, then it specifies the focus model for window. In this case the method returns an empty string. If no additional argument is supplied, then the method returns the current focus model for window. An active focus model means that window will claim the input focus for itself or its descendants, even at times when the focus is currently in some other application. Passive means that window will never claim the focus for itself: the window manager should give the focus to window at appropriate times. However, once the focus has been given to window or one of its descendants, the application may re-assign the focus among window’s descendants. The focus model defaults to passive, and Tk’s focus method assumes a passive model of focusing.

frame()
If window has been reparented by the window manager into a decorative frame, the method returns the platform-specific window identifier for the outermost frame that contains window (the window whose parent is the root or virtual root). If window hasn’t been reparented by the window manager then the method returns the platform specific window identifier for window. This method is only useful for X systems.

geometry(newGeometry=None)
If newGeometry is specified, then the geometry of window is changed and an empty string is returned. Otherwise the current geometry for window is returned (this is the most recent geometry specified either by manual resizing or in a wm_geometry call). newGeometry has the form =widthxheight+-x+-y, where any of =, widthxheight, or +-x+-y may be omitted. Width and height are positive integers specifying the desired dimensions of window. If window is gridded then the dimensions are specified in grid units; otherwise they are specified in pixel units. x and y specify the desired location of window on the screen, in pixels. If x is preceded by +, it specifies the number of pixels between the left edge of the screen and the left edge of window’s border; if preceded by – then x specifies the number of pixels between the right edge of the screen and the right edge of window’s border. If y is preceded by + then it specifies the number of pixels between the top of the screen and the top of window’s border; if y is preceded by – then it specifies the number of pixels between the bottom of window’s