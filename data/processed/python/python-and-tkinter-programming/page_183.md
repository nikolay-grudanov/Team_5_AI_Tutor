---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.03
tokens: 8357
characters: 2049
timestamp: 2025-12-24T00:36:30.155136
finish_reason: stop
---

We then define several class variables which provide default data for the version, title and about... information. We assume that these values will be overridden.

3 Default dimensions and padding are supplied. Again we expect that the application will override these values.

    frameWidth= 450
    frameHeight= 320
    padx      = 5
    pady      = 5
    usecommandarea= 0
    balloonhelp= 1

usecommandarea is used to inhibit or display the command (button) area.

4 In the __init__ for AppShell, we build the options supplied by the megawidget.

    def __init__(self, **kw):
        optiondefs = (
            ('padx',   1,           Pmw.INITOPT),
            ('pady',   1,           Pmw.INITOPT),
            ('framewidth',   1, Pmw.INITOPT),
            ('frameheight',   1,Pmw.INITOPT),
            ('usecommandarea', self.usecommandarea, Pmw.INITOPT))
        self.defineoptions(kw, optiondefs)

Pmw.INITOPT defines an option that is available only at initialization—it cannot be set with a configure call. (See “Pmw reference: Python megawidgets” on page 542 for more information on defining options.)

5 Now we can initialize Tk and Pmw and set the window’s title and geometry:

    self.root = Tk()
    self.initializeTk(self.root)
    Pmw.initialise(self.root)
    self.root.title(self.appname)
    self.root.geometry('%dx%d' % (self.frameWidth,
                                 self.frameHeight))

6 After defining the options and initializing Tk, we call the constructor for the base class:

    Pmw.MegaWidget.__init__(self, parent=self.root)

7 AppShell is intended to support the major Tkinter architectures; the next few methods define the colors and fonts appropriate for the particular platform.

AppShell.py (continued)

    def busyStart(self, newcursor=None):
        if not newcursor:
            newcursor = self.busyCursor LLLLLLLLLL
        newPreBusyCursors = {}

        for component in self.busyWidgets:
            newPreBusyCursors[component] = component['cursor']
            component.configure(cursor=newcursor)