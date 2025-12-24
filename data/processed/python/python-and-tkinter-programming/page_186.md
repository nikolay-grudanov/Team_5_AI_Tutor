---
source_image: page_186.png
page_number: 186
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.50
tokens: 8376
characters: 1956
timestamp: 2025-12-24T00:36:38.903174
finish_reason: stop
---

```python
Frame, (self._hull,),
    relief=GROOVE,
    bd=1)
self.dataArea.pack(side=TOP, fill=BOTH, expand=YES,
    padx=self['padx'], pady=self['pady'])

def __createCommandArea(self):
    # Create a command area for application-wide buttons.
    self.__commandFrame = self.createcomponent('commandframe', (), None,
        Frame,
        (self._hull,),
        relief=SUNKEN,
        bd=1)
    self.__buttonBox = self.createcomponent('buttonbox', (), None,
        Pmw.ButtonBox,
        (self.__commandFrame,),
        padx=0, pady=0)
    self.__buttonBox.pack(side=TOP, expand=NO, fill=X)
    if self['usecommandarea']:
        self.__commandFrame.pack(side=TOP,
            expand=NO,
            fill=X,
            padx=self['padx'],
            pady=self['pady'])

def __createMessageBar(self):
    # Create the message bar area for help and status messages.
    frame = self.createcomponent('bottomtray', (), None,
        Frame,(self._hull,), relief=SUNKEN)
    self.__messageBar = self.createcomponent('messagebar',
        (), None,
        Pmw.MessageBar,
        (frame,),
        #entry_width = 40,
        entry_relief=SUNKEN,
        entry_bd=1,
        labelpos=None)
    self.__messageBar.pack(side=LEFT, expand=YES, fill=X)

    self.__progressBar = ProgressBar.ProgressBar(frame,
        fillColor='slateblue',
        doLabel=1,
        width=150)
    self.__progressBar.frame.pack(side=LEFT, expand=NO, fill=NONE)

    self.updateProgress(0)
    frame.pack(side=BOTTOM, expand=NO, fill=X)

    self.__balloon.configure(statuscommand = \
        self.__messageBar.helpmessage)

def messageBar(self):
    return self.__messageBar

def updateProgress(self, newValue=0, newLimit=0):
    self.__progressBar.updateProgress(newValue, newLimit)
```

14. Создает командную область для кнопок, доступных во всем приложении.

15. Создает область сообщений для помощи и статусных сообщений.

16. Создает прогресс-бар и настраивает его свойства.