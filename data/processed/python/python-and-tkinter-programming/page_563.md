---
source_image: page_563.png
page_number: 563
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.25
tokens: 8418
characters: 2526
timestamp: 2025-12-24T00:47:47.852749
finish_reason: stop
---

window_create(index, options...)
Creates a new window annotation, which will appear in the text at the position given by index. Any number of option-value pairs may be specified to configure the annotation.

window_names()
Returns a list whose elements are the names of all windows currently embedded in window.

xview_moveto(fraction)
Adjusts the view in the window so that fraction of the horizontal span of the text is off-screen to the left. fraction is a fraction between 0 and 1.

xview_scroll(number, what)
Shifts the view in the window left or right according to number and what. number must be an integer. what must be either UNITS or PAGES or an abbreviation of one of these. If what is UNITS, the view adjusts left or right by number average-width characters on the display; if it is PAGES then the view adjusts by number screenfuls. If number is negative then characters farther to the left become visible; if it is positive then characters farther to the right become visible.

yview_moveto(fraction)
Adjusts the view in the window so that the character given by fraction appears on the top line of the window. fraction is a fraction between 0 and 1; 0 indicates the first character in the text, 0.33 indicates the character one-third of the way through the text, and so on.

yview_scroll(number, what)
Adjusts the view in the window up or down according to number and what. number must be an integer. what must be either UNITS or PAGES. If what is UNITS, the view adjusts up or down by number lines on the display; if it is PAGES then the view adjusts by number screenfuls. If number is negative then earlier positions in the text become visible; if it is positive then later positions in the text become visible.

yview_pickplace(index)
Changes the view in the widget’s window to make index visible. If the pickplace option isn’t specified then index will appear at the top of the window. If pickplace is specified then the widget chooses where index appears in the window. If index is already visible somewhere in the window then the method does nothing.
    If index is only a few lines off-screen above the window then it will be positioned at the top of the window. If index is only a few lines off-screen below the window then it will be positioned at the bottom of the window. Otherwise, index will be centered in the window.
    The pickplace option has been made obsolete by the see widget method (see handles both x- and y-motion to make a location visible, whereas pickplace only handles motion in y).