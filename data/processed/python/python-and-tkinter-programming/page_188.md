---
source_image: page_188.png
page_number: 188
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.98
tokens: 8199
characters: 1485
timestamp: 2025-12-24T00:36:23.943626
finish_reason: stop
---

self.__progressBar = ProgressBar.ProgressBar(frame,
    ...
17 It is a Pmw convention to provide a method to return a reference to the container where widgets should be created; this method is called interior:
    def interior(self):
        return self.dataArea
18 It also provides a method to create buttons within the commandarea and to bind balloon and status help to the button:
    def buttonAdd(self, buttonName, helpMessage=None,
        statusMessage=None, **kw):
        newBtn = self.__buttonBox.add(buttonName)
        newBtn.configure(kw)
        if helpMessage:
            self.bind(newBtn, helpMessage, statusMessage)
        return newBtn

AppShell.py (continued)

def __createInterface(self):
    self.__createBalloon()
    self.__createMenuBar()
    self.__createDataArea()
    self.__createCommandArea()
    self.__createMessageBar()
    self.__createAboutBox()
    #
    # Create the parts of the interface
    # which can be modified by subclasses.
    #
    self.busyWidgets = (self.root,)
    self.createMenuBar()
    self.createInterface()

def createInterface(self):
    # Override this method to create the interface for the app.
    pass

def main(self):
    self.pack()
    self.mainloop()

def run(self):
    self.main()

class TestAppShell(AppShell):
    usecommandarea=1

    def createButtons(self):
        self.buttonAdd('Ok',
            helpMessage='Exit',
            statusMessage='Exit',
            command=self.quit)

    def createMain(self):