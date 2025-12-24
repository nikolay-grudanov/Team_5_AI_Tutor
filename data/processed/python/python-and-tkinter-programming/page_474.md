---
source_image: page_474.png
page_number: 474
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.44
tokens: 8528
characters: 3188
timestamp: 2025-12-24T00:45:11.041268
finish_reason: stop
---

then the method returns a tuple containing two values, which are the current icon position hints (if no hints are in effect then None is returned).

iconwindow(pathName=None)
If pathname is specified, it is the path name for a window to use as icon for window; when window is iconified then pathname will be mapped to serve as icon, and when window is de-iconified then pathname will be unmapped again. If pathname is specified as an empty string then any existing icon window association for window will be cancelled. If the pathname argument is specified then an empty string is returned. Otherwise the method returns the path name of the current icon window for window, or an empty string if there is no icon window currently specified for window. Button press events are disabled for window as long as it is an icon window; this is needed in order to allow window managers to “own” those events.

Note: Not all window managers support the notion of an icon window.

maxsize(width=None, height=None)
If width and height are specified, they give the maximum permissible dimensions for window. For gridded windows the dimensions are specified in grid units; otherwise they are specified in pixel units. The window manager will restrict the window’s dimensions to be less than or equal to width and height. If width and height are specified, then the method returns None. Otherwise it returns a tuple with two elements, which are the maximum width and height currently in effect. The maximum size defaults to the size of the screen. If resizing has been disabled with the wm_resizable method, then this method has no effect. See the sections on geometry management: “Grid” section on page 492, “Pack” section on page 511 and “Place” section on page 516 for more information.

minsize(width=None, height=None)
If width and height are specified, they give the minimum permissible dimensions for window. For gridded windows the dimensions are specified in grid units; otherwise they are specified in pixel units. The window manager will restrict the window’s dimensions to be greater than or equal to width and height. If width and height are specified, then the method returns None. Otherwise it returns a tuple with two elements, which are the minimum width and height currently in effect. The minimum size defaults to one pixel in each dimension. If resizing has been disabled with the wm_resizable method, then this method has no effect. See the sections on geometry management: “Grid” section on page 492, “Pack” section on page 511 and “Place” section on page 516 for more information.

overrideredirect(boolean=None)
If boolean is specified, it must have a proper boolean form and the override-redirect flag for window is set to that value. If boolean is not specified then TRUE or FALSE is returned to indicate whether the override-redirect flag is currently set for window. Setting the override-redirect flag for a window causes it to be ignored by the window manager; among other things, this means that the window will not be reparented from the root window into a decorative frame and the user will not be able to manipulate the window using the normal window manager mechanisms.