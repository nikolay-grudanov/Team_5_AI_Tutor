---
source_image: page_173.png
page_number: 173
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.50
tokens: 8362
characters: 2063
timestamp: 2025-12-24T00:36:14.800314
finish_reason: stop
---

Code comments

1 The constructor initializes both Tk and Pmw:
    self.root = Tk()
    Pmw.initialise(self.root)
    Note that Pmw.initialise is not a typo; Pmw comes from Australia!

2 We create an instance of the Pmw.Balloon to implement Balloon Help. Naturally, this bit could have been left out, but it is easy to implement, so we might as well include it.
    self.balloon = Pmw.Balloon(master)
    Actions are bound later.

3 The next few points illustrate how to construct a simple menu using Pmw components. First we create the MenuBar, associating the balloon and defining hotkey as true (this creates mnemonics for menu selections).
    self.menuBar = Pmw.MenuBar(master, hull_borderwidth=1,
        hull_relief = RAISED,
        hotkeys=1, balloon = self.balloon)
    self.menuBar.pack(fill=X)

Note It is important to pack each form component in the order that they are to be displayed—having a menu at the bottom of a form might be considered a little strange!

4 The File menu button is created with an addmenu call:
    self.menuBar.addmenu('File', 'Exit')
    The second argument to addmenu is the balloon help to be displayed for the menu button. We then add an item to the button using addmenuitem:
    self.menuBar.addmenuitem('File', 'command',
        'Exit the application',
        label='Exit', command=self.exit)
    addmenuitem creates an entry within the specified menu. The third argument is the help to be displayed.

5 We create a Frame to contain the data-entry widgets and a second frame to contain some display widgets:
    self.dataFrame = Frame(master)
    self.dataFrame.pack(fill=BOTH, expand=1)

6 At the bottom of the form, we create a statusBar to display help messages and other information:
    self.statusBar = Pmw.MessageBar(master, entry_width = 40,
        entry_relief=GROOVE,
        labelfpos = W,
        label_text = '')
    self.statusBar.pack(fill = X, padx = 10, pady = 10)

7 We bind the balloon’s statuscommand to the MessageBar widget:
    self.balloon.configure(statuscommand = self.statusBar.helpmessage)