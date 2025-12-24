---
source_image: page_212.png
page_number: 212
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.66
tokens: 8374
characters: 2161
timestamp: 2025-12-24T00:37:20.915486
finish_reason: stop
---

2 We initialize an empty pane for each step and initialize for the first step:
    self.pCurrent = 0
    self.pFrame = [None] * self.panes

3 The main WizardArea is created:
    def __createWizardArea(self):
        ...
    def __createSeparator(self):
        ...
    def __createCommandArea(self):
        ...

Then, a Separator and a CommandArea are added.

4 buttonAdd is slightly more comprehensive than AppShell’s since we have to enable and disable the next and prev buttons as we move through the sequence:
    def buttonAdd(self, buttonName, command=None, state=1):
        frame = Frame(self.__commandFrame)
        newBtn = Button(frame, text=buttonName, command=command)
        newBtn.pack()
        newBtn['state'] = [DISABLED, NORMAL][state]
        frame.pack(side=RIGHT, ipadx=5, ipady=5)
        return newBtn

5 Now we create a pane for each step, packing the current frame and forgetting all others so that they are not displayed:
    def __createPanes(self):
        for i in range(self.panes):
            self.pFrame[i] = self.createcomponent('pframe', (), None,
                Frame,(self.interior(),),
                relief=FLAT, bd=1)
            if not i == self.pCurrent:
                self.pFrame[i].forget()
            else:
                self.pFrame[i].pack(fill=BOTH, expand=YES)

6 Similar to the convention to define an interior method, we define the pInterior method to give access to individual panes in the wizard:
    def pInterior(self, idx):
        return self.pFrame[idx]

7 The next and prev methods forget the current pane and pack the next pane, changing the state of buttons as appropriate and changing the labels as necessary:
    def next(self):
        cpane = self.pCurrent
        self.pCurrent = self.pCurrent + 1
        self.prevB['state'] = NORMAL
        if self.pCurrent == self.panes - 1:
            self.nextB['text'] = 'Finish'
            self.nextB['command'] = self.done
        self.pFrame[cpane].forget()
        self.pFrame[self.pCurrent].pack(fill=BOTH, expand=YES)

8 Unlike AppShell, we have to store references to the control buttons so that we can manipulate their state and labels: