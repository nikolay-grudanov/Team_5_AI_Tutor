---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.93
tokens: 8314
characters: 1946
timestamp: 2025-12-24T00:36:30.155260
finish_reason: stop
---

self.menuBar.addmenuitem('Help', 'command',
    'Get information on application',
    label='About...', command=self.showAbout)
self.toggleBalloonVar = IntVar()
self.toggleBalloonVar.set(1)
self.menuBar.addmenuitem('Help', 'checkbutton',
    'Toggle balloon help',
    label='Balloon help',
    variable = self.toggleBalloonVar,
    command=self.toggleBalloon)

self.menuBar.addmenuitem('File', 'command', 'Quit this application',
    label='Quit',
    command=self.quit)

Code comments (continued)

8 The next few methods support setting and unsetting the busy cursor:
    def busyStart(self, newcursor=None):
        ...

9 Next we define methods to support the About... functionality. The message box is created before it is used, so that it can be popped up when required.
    def __createAboutBox(self):
        ...

10 Balloon help can be useful for users unfamiliar with an interface, but annoying to expert users. AppShell provides a menu option to turn off balloon help, leaving the regular status messages displayed, since they do not tend to cause a distraction.
    def toggleBalloon(self):
        if self.toggleBalloonVar.get():
            self.__balloon.configure(state = 'both')
        else:
            self.__balloon.configure(state = 'status')

11 Menu bar creation is split into two member functions. __createMenuBar creates a Pmw MenuBar component and createMenuBar populates the menu with standard options, which you may extend as necessary to support your application.

AppShell.py (continued)

def __createBalloon(self):    12
    # Create the balloon help manager for the frame.
    # Create the manager for the balloon help
    self.__balloon = self.createcomponent('balloon', (), None,
        Pmw.Balloon, (self._hull,))

def balloon(self):
    return self.__balloon

def __createDataArea(self):    13
    # Create a data area where data entry widgets are placed.
    self.dataArea = self.createcomponent('dataarea',