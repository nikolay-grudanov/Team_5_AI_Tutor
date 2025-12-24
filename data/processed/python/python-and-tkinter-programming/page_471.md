---
source_image: page_471.png
page_number: 471
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.62
tokens: 8507
characters: 3023
timestamp: 2025-12-24T00:45:02.628137
finish_reason: stop
---

Wm methods

Description

The wm methods are used to interact with window managers in order to control such things as the title for a window, its geometry, or the increments in terms of which it may be resized. Tkinter makes these methods accessible at the root window (Tk) and with all TopLevel widgets. The wm methods can take any of a number of different forms, depending on the option argument. All of the forms expect at least one additional argument, window, which must be the path name of a top-level window.

Tkinter defines synonyms for wm methods, although you are free to use the wm_ prefix if you wish. The legal forms for the wm methods follow.

aspect(minNumer=None, minDemon=None, maxNumer=None, maxDenom=None)
If minNumer, minDenom, maxNumer, and maxDenom are all specified, then they will be passed to the window manager and the window manager should use them to enforce a range of acceptable aspect ratios for window. The aspect ratio of window (width/length) will be constrained to lie between minNumer/minDenom and maxNumer/maxDenom.

If minNumer, etc., are all unspecified, then any existing aspect ratio restrictions are removed. If minNumer, etc., are specified, then the method returns None. Otherwise, it returns a tuple containing four elements, which are the current values of minNumer, minDenom, maxNumer and maxDenom (if no aspect restrictions are in effect, then None is returned).

client(name=None)
If name is specified, this method stores name (which should be the name of the host on which the application is executing) in window’s WM_CLIENT_MACHINE property for use by the window manager or session manager. If name isn’t specified, the method returns the last name set in a wm_client method for window. If name is specified as an empty string, the method deletes the WM_CLIENT_MACHINE property from window. This method is only useful for X systems.

colormapwindows(*windowList)
Used to manipulate the WM_COLORMAP_WINDOWS property, which provides information to the window managers about windows that have private colormaps. If windowList isn’t specified, the method returns a list whose elements are the names of the windows in the WM_COLORMAP_WINDOWS property. If windowList is specified, it consists of a list of window path names; the method overwrites the WM_COLORMAP_WINDOWS property with the given windows and returns None. This method is only useful for X systems.

The WM_COLORMAP_WINDOWS property should normally contain a list of the internal windows within window whose colormaps differ from their parents. The order of the windows in the property indicates a priority order: the window manager will attempt to install as many colormaps as possible from the head of this list when window gets the colormap focus. If window is not included among the windows in windowList, Tk implicitly adds it at the end of the WM_COLORMAP_WINDOWS property, so that its colormap is lowest in priority. If wm_colormapwindows is not invoked, Tk will automatically set the property for each top-