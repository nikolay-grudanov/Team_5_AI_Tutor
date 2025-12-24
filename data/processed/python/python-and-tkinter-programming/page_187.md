---
source_image: page_187.png
page_number: 187
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.10
tokens: 8288
characters: 1789
timestamp: 2025-12-24T00:36:29.791867
finish_reason: stop
---

def bind(self, child, balloonHelpMsg, statusHelpMsg=None):
    # Bind a help message and/or status message to a widget.
    self.__balloon.bind(child, balloonHelpMsg, statusHelpMsg)

def interior(self):
    # Retrieve the interior site where widgets should go.
    return self.dataArea

def buttonBox(self):
    # Retrieve the button box.
    return self.__buttonBox

def buttonAdd(self, buttonName, helpMessage=None, statusMessage=None, **kw):
    # Add a button to the button box.
    newBtn = self.__buttonBox.add(buttonName)
    newBtn.configure(kw)
    if helpMessage:
        self.bind(newBtn, helpMessage, statusMessage)
    return newBtn

Code comments (continued)

12 The balloon component is created:
    def __createBalloon(self):
        self.__balloon = self.createcomponent('balloon', (), None,
            Pmw.Balloon, (self._hull,))

13 The dataarea component is simply a frame to contain whatever widget arrangement is needed for the application:
    def __createDataArea(self):
        self.dataArea = self.createcomponent('dataarea',
            (), None,
            Frame, (self._hull,),
            relief=GROOVE,
            bd=1)

14 The commandarea is a frame containing a Pmw ButtonBox:
    def __createCommandArea(self):
        self.__commandFrame = self.createcomponent('commandframe', (), None,
            Frame,
            (self._hull,),
            relief=SUNKEN,
            bd=1)
        self.__buttonBox = self.createcomponent('buttonbox', (), None,
            Pmw.ButtonBox,
            (self.__commandFrame,),
            padx=0, pady=0)

15 Similarly, the messagebar is a frame containing a Pmw MessageBox:
    def __createMessageBar(self):
        ...

16 To complete our major components, we create a progressbar component next to the messagebar: