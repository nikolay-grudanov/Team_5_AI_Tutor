---
source_image: page_213.png
page_number: 213
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.17
tokens: 8159
characters: 1152
timestamp: 2025-12-24T00:37:03.848387
finish_reason: stop
---

class TestWizardShell(WizardShell):
    def createButtons(self):
        self.buttonAdd('Cancel', command=self.quit)
        self.nextB = self.buttonAdd('Next', command=self.next)
        self.prevB = self.buttonAdd('Prev', command=self.prev, state=0)

9 The done method is clearly intended to be overridden!
    def done(self):
        print 'All Done'

![Generic Wizard Frame](./images/wizard.png)

Figure 8.12 Wizard

If you run wizardshell.py, you’ll see the basic shell shown in figure 8.12. Now we need to populate the wizard. Here is an example installation sequence:

Example_8_11.py

from Tkinter import *
import Pmw
import sys, string
import WizardShell

class Installer(WizardShell.WizardShell):
    wizname = 'Install Widgets'
    panes= 4

    def createButtons(self):
        self.buttonAdd('Cancel', command=self.quit, state=1)
        self.nextB = self.buttonAdd('Next', command=self.next, state=1)
        self.prevB = self.buttonAdd('Prev', command=self.prev, state=0)

    def createTitle(self, idx, title):
        label = self.createcomponent('l%d' % idx, (), None,
            Label,(self.pInterior(idx),),
            text=title,