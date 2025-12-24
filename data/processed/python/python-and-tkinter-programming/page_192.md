---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.77
tokens: 8264
characters: 1783
timestamp: 2025-12-24T00:36:45.222663
finish_reason: stop
---

4 The final entry in each table defines the title and a list of indices for the primary and secondary keys (in this case, we are only using a single key):
    'Crew Members', [0]),
Now let’s use datadictionary.py to create an interface. We will also use AppShell to provide the framework.

Example_8_7.py

from Tkinter import *
import Pmw
import os
import AppShell
from datadictionary import *

class DDForm(AppShell.AppShell): ①
    usecommandarea = 1
    appname        = 'Update Crew Information'
    dictionary     = 'crewmembers'
    frameWidth     = 600
    frameHeight    = 590

def createButtons(self): ②
    self.buttonAdd('Save',
        helpMessage='Save current data',
        statusMessage='Write current information to database',
        command=self.unimplemented)
    self.buttonAdd('Undo',
        helpMessage='Ignore changes',
        statusMessage='Do not save changes to database',
        command=self.unimplemented)
    self.buttonAdd('New',
        helpMessage='Create a New record',
        statusMessage='Create New record',
        command=self.unimplemented)
    self.buttonAdd('Delete',
        helpMessage='Delete current record',
        statusMessage='Delete this record',
        command=self.unimplemented)
    self.buttonAdd('Print',
        helpMessage='Print this screen',
        statusMessage='Print data in this screen',
        command=self.unimplemented)
    self.buttonAdd('Prev',
        helpMessage='Previous record',
        statusMessage='Display previous record',
        command=self.unimplemented)
    self.buttonAdd('Next',
        helpMessage='Next record',
        statusMessage='Display next record',
        command=self.unimplemented)
    self.buttonAdd('Close',
        helpMessage='Close Screen',
        statusMessage='Exit',