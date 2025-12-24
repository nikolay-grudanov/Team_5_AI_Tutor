---
source_image: page_181.png
page_number: 181
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.47
tokens: 8299
characters: 1674
timestamp: 2025-12-24T00:36:23.406236
finish_reason: stop
---

Since AppShell is an important feature of several of our examples, we are going to examine the source code in detail; additionally, if you are going to use AppShell directly, or adapt it for your own needs, you need to understand its facilities and operations.

AppShell.py

from Tkinter import *
import Pmw
import sys, string
import ProgressBar

class AppShell(Pmw.MegaWidget):
    appversion= '1.0'
    appname    = 'Generic Application Frame'
    copyright= 'Copyright YYYY Your Company. All Rights Reserved'
    contactname= 'Your Name'
    contactphone= '(999) 555-1212'
    contactemail= 'youremail@host.com'

    frameWidth= 450
    frameHeight= 320
    padx      = 5
    pady      = 5
    usecommandarea= 0
    balloonhelp= 1

    busyCursor = 'watch'

    def __init__(self, **kw):
        optiondefs = (
            ('padx',    1,      Pmw.INITOPT),
            ('pady',    1,      Pmw.INITOPT),
            ('framewidth',   1, Pmw.INITOPT),
            ('frameheight',   1,Pmw.INITOPT),
            ('usecommandarea', self.usecommandarea, Pmw.INITOPT))
        self.defineoptions(kw, optiondefs)

        self.root = Tk()
        self.initializeTk(self.root)
        Pmw.initialise(self.root)
        self.root.title(self.appname)
        self.root.geometry('%dx%d' % (self.frameWidth,
                                      self.frameHeight))

        # Initialize the base class
        Pmw.MegaWidget.__init__(self, parent=self.root)

        # Initialize the application
        self.appInit()

        # Create the interface
        self.__createInterface()

        # Create a table to hold the cursors for
        # widgets which get changed when we go busy