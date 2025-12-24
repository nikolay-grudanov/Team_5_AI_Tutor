---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.91
tokens: 8331
characters: 2035
timestamp: 2025-12-24T00:36:55.370690
finish_reason: stop
---

8.4 Notebooks

Notebooks (sometimes referred to as style or property sheets) have become a common motif for user interfaces. One large advantage is that they allow the form designer to display a large number of entry fields without overwhelming the user. Additionally, the fields can be arranged in related groupings, or less-important fields can be separated from fields which are frequently changed.

The next example demonstrates the use of notebooks, data dictionaries and AppShell to present the same basic data in Example_8_7.py on three separate notebook panes. datadictionary.py has been rearranged as datadictionary2.py, but it will not be presented here (the previous dictionary has been divided into one section for each pane of the notebook).

Example_8_9.py

from Tkinter import *
import Pmw
import os
import AppShell
from datadictionary2 import *

class DDNotebook(AppShell.AppShell):
    usecommandarea = 1
    appname        = 'Update Crew Information'
    dictionary     = 'crewmembers'
    frameWidth     = 435
    frameHeight    = 520

    def createButtons(self):
        self.buttonAdd('Save',
            helpMessage='Save current data',
            statusMessage='Write current information to database',
            command=self.save)
        self.buttonAdd('Close',
            helpMessage='Close Screen',
            statusMessage='Exit',
            command=self.close)

    def createNotebook(self):
        self.notebook = self.createcomponent('notebook', (), None,
            Pmw.NoteBookR, (self.interior(),),)
        self.notebook.pack(side=TOP, expand=YES, fill=BOTH, padx=5, pady=5)
        self.formwidth = self.root.winfo_width()

    def addPage(self, dictionary):
        table, top, anchor, incr, fields, \
            title, keylist = dataDict[dictionary]
        self.notebook.add(table, label=title)
        self.current = 0
        ypos = top
        idx = 0

        for label, field, width, proc, valid, nonblank in fields:
            pstr = 'Label(self.notebook.page(table).interior(),\'