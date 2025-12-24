---
source_image: page_209.png
page_number: 209
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.52
tokens: 8345
characters: 1985
timestamp: 2025-12-24T00:37:09.481596
finish_reason: stop
---

8.6 Wizards

Windows 95/98/NT users have become familiar with wizard interfaces since they have become prevalent with installation and configuration tools. Wizards guide the user through a sequence of steps, and they allow forward and backward navigation. In many respects they are similar to Notebooks, except for their ordered access as opposed to the random access of the Notebook.

This example illustrates a wizard that supports software installation. WizardShell.py is derived from AppShell.py, but it has sufficient differences to preclude inheriting AppShell’s properties. However, much of the code is similar to AppShell and is not presented here; the complete source is available online.

WizardShell.py

from Tkinter import *
import Pmw
import sys, string

class WizardShell(Pmw.MegaWidget):
    wizversion= '1.0'
    wizname    = 'Generic Wizard Frame'
    wizimage= 'wizard.gif'

    panes      = 4

    def __init__(self, **kw):
        optiondefs = (
            ('framewidth',   1,           Pmw.INITOPT),
            ('frameheight',   1,           Pmw.INITOPT))
        self.defineoptions(kw, optiondefs)

        # setup panes
        self.pCurrent = 0
        self.pFrame = [None] * self.panes

    def wizardInit(self):
        # Called before interface is created (should be overridden).
        pass

    def __createWizardArea(self):
        self.__wizardArea = self.createcomponent('wizard',(), None,
            Frame, (self._hull,),
            relief=FLAT, bd=1)
        self.__illustration = self.createcomponent('illust',(), None,
            Label,(self.__wizardArea,))
        self.__illustration.pack(side=LEFT, expand=NO, padx=20)
        self.__wizimage = PhotoImage(file=self.wizimage)
        self.__illustration['image'] = self.__wizimage

        self.__dataArea = self.createcomponent('dataarea',(), None,
            Frame,(self.__wizardArea,),
            relief=FLAT, bd=1)

        self.__dataArea.pack(side=LEFT, fill = 'both', expand = YES)