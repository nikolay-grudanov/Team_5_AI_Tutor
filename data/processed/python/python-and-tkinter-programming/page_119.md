---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.54
tokens: 8175
characters: 1376
timestamp: 2025-12-24T00:34:29.964321
finish_reason: stop
---

Code comments

1 We add a button to display the image information.
2 To force a refresh of the image info, we toggle the info display.
    self.info();self.info()
3 The info method toggles the information display.
4 If the window is currently displayed, we destroy it.
5 Otherwise, we create a new window, placing it above the image and setting its width to match that of the image. We also add a negative increment to the y position to provide a little whitespace.
    self.fm.place(in_=self.lbl, relx=0.5,
        relwidth=1.0, height=50, anchor=S,
        rely=0.0, y=-4, bordermode='outside')
6 The entries in the information window are placed programmatically.

5.5 Summary

Mastering the geometry managers is an important step in developing the ability to produce attractive and effective GUIs. When starting out with Tkinter, most readers will find grid and pack to be easy to use and capable of producing the best results when a window is resized. For very precise placement of widgets, place is a better choice. However, this does take quite a bit more effort.

You will see many examples of using the three managers throughout the book. Remember that it is often appropriate to combine geometry managers within a single window. If you do, you must be careful to follow some rules; if things are just not working out, then you have probably broken one of those rules!