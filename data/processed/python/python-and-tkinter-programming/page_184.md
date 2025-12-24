---
source_image: page_184.png
page_number: 184
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.85
tokens: 8277
characters: 1783
timestamp: 2025-12-24T00:36:23.917073
finish_reason: stop
---

```python
component.update_idletasks()
self.preBusyCursors = (newPreBusyCursors, self.preBusyCursors)

def busyEnd(self):
    if not self.preBusyCursors:
        return
    oldPreBusyCursors = self.preBusyCursors[0]
    self.preBusyCursors = self.preBusyCursors[1]

    for component in self.busyWidgets:
        try:
            component.configure(cursor=oldPreBusyCursors[component])
        except KeyError:
            pass
    component.update_idletasks()

def __createAboutBox(self):  #9
    Pmw.aboutversion(self.appversion)
    Pmw.aboutcopyright(self.copyright)
    Pmw.aboutcontact(
        'For more information, contact:\n %s\n Phone: %s\n Email: %s' %
        (self.contactname, self.contactphone,
         self.contactemail))
    self.about = Pmw.AboutDialog(self._hull,
                                 applicationname=self.appname)
    self.about.withdraw()
    return None

def showAbout(self):
    # Create the dialog to display about and contact information.
    self.about.show()
    self.about.focus_set()

def toggleBalloon(self):  #10
    if self.toggleBalloonVar.get():
        self.__balloon.configure(state = 'both')
    else:
        self.__balloon.configure(state = 'status')

def __createMenuBar(self):  #11
    self.menuBar = self.createcomponent('menubar', (), None,
                                        Pmw.MenuBar,
                                        (self._hull,),
                                        hull_relief=RAISED,
                                        hull_borderwidth=1,
                                        balloon=self.balloon())
    self.menuBar.pack(fill=X)
    self.menuBar.addmenu('Help', 'About %s' % self.appname, side='right')
    self.menuBar.addmenu('File', 'File commands and Quit')

def createMenuBar(self):
```