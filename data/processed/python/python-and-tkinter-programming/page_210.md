---
source_image: page_210.png
page_number: 210
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.95
tokens: 8361
characters: 1762
timestamp: 2025-12-24T00:37:14.159122
finish_reason: stop
---

```python
self.__wizardArea.pack(side=TOP, fill=BOTH, expand=YES)

def __createSeparator(self):
    self.__separator = self.createcomponent('separator',(), None,
        Frame,(self._hull,),
        relief=SUNKEN,
        bd=2, height=2)
    self.__separator.pack(fill=X, expand=YES)

def __createCommandArea(self):
    self.__commandFrame = self.createcomponent('commandframe',(), None,
        Frame,(self._hull,),
        relief=FLAT, bd=1)
    self.__commandFrame.pack(side=TOP, expand=NO, fill=X)

def interior(self):
    return self.__dataArea

def changePicture(self, gif):
    self.__wizimage = PhotoImage(file=gif)
    self.__illustration['image'] = self.__wizimage

def buttonAdd(self, buttonName, command=None, state=1): ④
    frame = Frame(self.__commandFrame)
    newBtn = Button(frame, text=buttonName, command=command)
    newBtn.pack()
    newBtn['state'] = [DISABLED,NORMAL][state]
    frame.pack(side=RIGHT, ipadx=5, ipady=5)
    return newBtn

def __createPanes(self):
    for i in range(self.panes):
        self.pFrame[i] = self.createcomponent('pframe',(), None,
            Frame,(self.interior(),),
            relief=FLAT, bd=1)
        if not i == self.pCurrent:
            self.pFrame[i].forget()
        else:
            self.pFrame[i].pack(fill=BOTH, expand=YES)

def pInterior(self, idx): ⑥
    return self.pFrame[idx]

def next(self): ⑦
    cpane = self.pCurrent
    self.pCurrent = self.pCurrent + 1
    self.prevB['state'] = NORMAL
    if self.pCurrent == self.panes - 1:
        self.nextB['text'] = 'Finish'
        self.nextB['command'] = self.done
    self.pFrame[cpane].forget()
    self.pFrame[self.pCurrent].pack(fill=BOTH, expand=YES)

def prev(self):
    cpane = self.pCurrent
    self.pCurrent = self.pCurrent - 1
```