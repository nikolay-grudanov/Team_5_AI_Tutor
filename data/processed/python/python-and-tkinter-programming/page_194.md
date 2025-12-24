---
source_image: page_194.png
page_number: 194
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.73
tokens: 8287
characters: 1648
timestamp: 2025-12-24T00:36:48.618401
finish_reason: stop
---

def update_display(self):
    idx = 0
    for label, field, width, proc, valid, nonblank in self.fields:
        v=self.records[self.current][idx]
        if not v:v=""
        exec 'self.%sV.set(v)' % field
        idx = idx + 1
    if self.current in self.deleted:
        self.rmarker['text'] = 'Deleted'
    elif self.current in self.newrecs:
        self.rmarker['text'] = 'New'
    else:
        self.rmarker['text'] = ''
    if self.dirty:
        self.lmarker['text'] = "Modified"
        self.lmarker['foreground'] = "#FF3333"
    else:
        self.lmarker['text'] = ""
        self.lmarker['foreground'] = "#00FF44"
    # We'll set focus on the first widget
    label, field, width, proc, valid, nonblank = self.fields[0]
    exec 'self.%s.focus_set()' % field

def unimplemented(self):
    pass

def createInterface(self):
    AppShell.AppShell.createInterface(self)
    self.createButtons()
    self.createForm()
    self.createFields()

if __name__ == '__main__':
    ddform = DDForm()
    ddform.run()

Code comments

1 First we define the Application class, inheriting from AppShell and overriding its class variables to set the title, width, height and other values:

class DDForm(AppShell.AppShell):
    usecommandarea = 1
    appname        = 'Update Crew Information'
    dictionary     = 'crewmembers'
    frameWidth     = 600
    frameHeight    = 590

2 In this example, we are defining a more realistic complement of control buttons:

def createButtons(self):
    self.buttonAdd('Save',
        helpMessage='Save current data',
        statusMessage='Write current information to database',
        command=self.save)
    ...