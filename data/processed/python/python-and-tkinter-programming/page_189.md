---
source_image: page_189.png
page_number: 189
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.21
tokens: 8243
characters: 1671
timestamp: 2025-12-24T00:36:38.433316
finish_reason: stop
---

self.label = self.createcomponent('label', (), None,
    Label,
    (self.interior(),),
    text='Data Area')
self.label.pack()
self.bind(self.label, 'Space taker')

def createInterface(self):
    AppShell.createInterface(self)
    self.createButtons()
    self.createMain()

if __name__ == '__main__':
    test = TestAppShell(balloon_state='both')
    test.run()

Code comments (continued)

19 __createInterface creates each of the standard areas and then calls the createInterface method (which is overridden by the application) to complete the population of the various areas:

def __createInterface(self):
    self.__createBalloon()
    self.__createMenuBar()
    self.__createDataArea()
    self.__createCommandArea()
    self.__createMessageBar()
    self.__createAboutBox()
    self.busyWidgets = (self.root,)
    self.createMenuBar()
    self.createInterface()

20 For this example, we define just one button to exit the application; you would add all of your buttons to this method for your application.

def createButtons(self):
    self.buttonAdd('Ok',
        helpMessage='Exit',
        statusMessage='Exit',
        command=self.quit)

21 Again, for the purpose of illustration, the dataarea has not been populated with any more than a simple label:

def createMain(self):
    self.label = self.createcomponent('label', (), None,
        Label,
        (self.interior(),),
        text='Data Area')
    self.label.pack()
    self.bind(self.label, 'Space taker')
    Notice how we define balloon help for the label.

22 Finally, here is the createInterface method which extends AppShells method:

def createInterface(self):
    AppShell.createInterface(self)