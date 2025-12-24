---
source_image: page_469.png
page_number: 469
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.63
tokens: 8247
characters: 1776
timestamp: 2025-12-24T00:44:49.723180
finish_reason: stop
---

winfo_screen()
Returns the name of the screen associated with window, in the form displayName.screenIndex.

winfo_screencells()
Returns an integer giving the number of cells in the default color map for window’s screen.

winfo_screendepth()
Returns an integer giving the depth of the root window of window’s screen (number of bits per pixel).

winfo_screenheight()
Returns an integer giving the height of window’s screen, in pixels.

winfo_screenmmheight()
Returns an integer giving the height of window’s screen, in millimeters.

winfo_screenmmwidth()
Returns an integer giving the width of window’s screen, in millimeters.

winfo_screenvisual()
Returns one of the following strings to indicate the default visual class for window’s screen: directcolor, grayscale, pseudocolor, staticcolor, staticgray or truecolor.

winfo_screenwidth()
Returns an integer giving the width of window’s screen, in pixels.

winfo_server()
Returns a string containing information about the server for window’s display. The exact format of this string may vary from platform to platform. For X servers the string has the form XmajorRminor vendor vendorVersion where major and minor are the version and revision numbers provided by the server (e.g. X11R5), vendor is the name of the vendor for the server and vendorRelease is an integer release number provided by the server.

winfo_toplevel()
Returns the identity of the top-level window containing window.

winfo_viewable()
Returns TRUE if window and all of its ancestors up through the nearest toplevel window are mapped. Returns FALSE if any of these windows are not mapped.

winfo_visual()
Returns one of the following strings to indicate the visual class for window: directcolor, grayscale, pseudocolor, staticcolor, staticgray or truecolor.