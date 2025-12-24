---
source_image: page_118.png
page_number: 118
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.49
tokens: 8275
characters: 1838
timestamp: 2025-12-24T00:34:37.929161
finish_reason: stop
---

The Placer has another important property: unlike the other Tkinter managers, it does not attempt to set the geometry of the master window. If you want to control the dimensions of container widgets, you must use widgets such as Frames or Canvases that have a configure option to allow you to control their sizes. Let’s take a look at the code needed to implement the information window.

scrapbook2.py

from Tkinter import *
import Image, ImageTk, os, string

class Scrapbook:
    def __init__(self, master=None):
        # --- Code Removed -------------------------------------------------------------
        Button(self.frame, text='Info', command=self.info,
            bg='blue', fg='yellow').place(relx=0.99, rely=0.90, anchor=SE)
        self.infoDisplayed = FALSE

    def getImg(self, img):
        # --- Code Removed -------------------------------------------------------------
        if self.infoDisplayed:
            self.info();self.info()

    def info(self):
        if self.infoDisplayed:
            self.fm.destroy()
            self.infoDisplayed = FALSE
        else:
            self.fm = Frame(self.master, bg='gray10')
            self.fm.place(in_=self.lbl, relx=0.5,
                relwidth=1.0, height=50, anchor=S,
                rely=0.0, y=-4, bordermode='outside')
            ypos = 0.15
            for lattr in ['Format', 'Size', 'Mode']:
                Label(self.fm, text='%s:\t%s' % (lattr,
                    getattr(self.masterImg,
                        '%s' % string.lower(lattr))),
                    bg='gray10', fg='white',
                    font=('verdana', 8)).place(relx=0.3,
                    rely= ypos, anchor=W)
                ypos = ypos + 0.35
            self.infoDisplayed = TRUE

        # --- Code Removed -------------------------------------------------------------