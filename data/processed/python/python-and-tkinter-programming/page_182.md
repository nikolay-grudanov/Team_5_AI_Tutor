---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.98
tokens: 8338
characters: 1868
timestamp: 2025-12-24T00:36:29.704693
finish_reason: stop
---

self.preBusyCursors = None

# Pack the container and set focus
# to ourselves
self._hull.pack(side=TOP, fill=BOTH, expand=YES)
self.focus_set()
# Initialize our options
self.initialiseoptions(AppShell)

def appInit(self):
    # Called before interface is created (should be overridden).
    pass

def initializeTk(self, root):  ⑦
    # Initialize platform-specific options
    if sys.platform == 'mac':
        self.__initializeTk_mac(root)
    elif sys.platform == 'win32':
        self.__initializeTk_win32(root)
    else:
        self.__initializeTk_unix(root)

def __initializeTk_colors_common(self, root):
    root.option_add('*background', 'grey')
    root.option_add('*foreground', 'black')
    root.option_add('*EntryField.Entry.background', 'white')
    root.option_add('*MessageBar.Entry.background', 'gray85')
    root.option_add('*Listbox*background', 'white')
    root.option_add('*Listbox*selectBackground', 'dark slate blue')
    root.option_add('*Listbox*selectForeground', 'white')

def __initializeTk_win32(self, root):
    self.__initializeTk_colors_common(root)
    root.option_add('*Font', 'Verdana 10 bold')
    root.option_add('*EntryField.Entry.Font', 'Courier 10')
    root.option_add('*Listbox*Font', 'Courier 10')

def __initializeTk_mac(self, root):
    self.__initializeTk_colors_common(root)

def __initializeTk_unix(self, root):
    self.__initializeTk_colors_common(root)


Code comments

① AppShell imports ProgressBar. Its code is not shown here, but is available online.
import ProgressBar

② AppShell inherits Pmw.MegaWidget since we are constructing a megawidget.
class AppShell(Pmw.MegaWidget):
    appversion= '1.0'
    appname    = 'Generic Application Frame'
    copyright= 'Copyright YYYY Your Company. All Rights Reserved'
    contactname= 'Your Name'
    contactphone= '(999) 555-1212'
    contactemail= 'youremail@host.com'