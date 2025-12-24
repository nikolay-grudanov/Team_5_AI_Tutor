---
source_image: page_211.png
page_number: 211
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.87
tokens: 8310
characters: 1749
timestamp: 2025-12-24T00:37:14.142176
finish_reason: stop
---

```python
if self.pCurrent <= 0:
    self.pCurrent = 0
    self.prevB['state'] = DISABLED
if cpane == self.panes - 1:
    self.nextB['text'] = 'Next'
    self.nextB['command'] = self.next
self.pFrame[cpane].forget()
self.pFrame[self.pCurrent].pack(fill=BOTH, expand=YES)

def done(self):
    #to be overridden
    pass

def __createInterface(self):
    self.__createWizardArea()
    self.__createSeparator()
    self.__createCommandArea()
    self.__createPanes()
    self.busyWidgets = (self.root,)
    self.createInterface()

class TestWizardShell(WizardShell):
    def createButtons(self):
        self.buttonAdd('Cancel', command=self.quit)
        self.nextB = self.buttonAdd('Next', command=self.next)
        self.prevB = self.buttonAdd('Prev', command=self.prev, state=0)

    def createMain(self):
        self.w1 = self.createcomponent('w1', (), None,
            Label,(self.pInterior(0),),
            text='Wizard Area 1')
        self.w1.pack()
        self.w2 = self.createcomponent('w2', (), None,
            Label,(self.pInterior(1),),
            text='Wizard Area 2')
        self.w2.pack()

    def createInterface(self):
        WizardShell.createInterface(self)
        self.createButtons()
        self.createMain()

    def done(self):
        print 'All Done'

if __name__ == '__main__':
    test = TestWizardShell()
    test.run()

Code comments
WizardShell uses AppShell’s class variables, adding panes to define the number of discrete steps to be presented in the wizard.

class WizardShell(Pmw.MegaWidget):
    panes = 4
```

1 WizardShell uses AppShell’s class variables, adding panes to define the number of discrete steps to be presented in the wizard.

```python
class WizardShell(Pmw.MegaWidget):
    panes = 4
```