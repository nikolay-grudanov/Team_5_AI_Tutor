---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.26
tokens: 8303
characters: 1714
timestamp: 2025-12-24T00:37:24.590776
finish_reason: stop
---

print 'This is where the work starts!'

if __name__ == '__main__':
    install = Installer()
    install.run()

Code comments

1 We begin by defining some routines to perform common tasks. Each of the wizard panes has a title:

def createTitle(self, idx, title):
    label = self.createcomponent('l%d' % idx, (), None,
        Label,(self.pInterior(idx),),
        text=title,
        font=(_('verdana', 18, 'bold', 'italic')))
    label.pack()
    return label

2 Wizards need to supply concise and clear directions to the user; this routine formats the information appropriately using a regular Tkinter Text widget—the text is read from a file:

def createExplanation(self, idx):
    text = self.createcomponent('t%d' % idx, (), None,
        Text,(self.pInterior(idx),),
        bd=0, wrap=WORD, height=6)
    fd = open('install%d.txt' % (idx+1))
    text.insert(END, fd.read())
    fd.close()
    text.pack(pady=15)

3 Each pane in the wizard is constructed separately—here is an example:

def createPanelTwo(self):
    self.createTitle(1, 'Select Destination\nDirectory')
    self.createExplanation(1)
    frame = Frame(self.pInterior(1), bd=2, relief=GROOVE)
    self.entry = Label(frame, text='C:\\\\Widgets\\\\WidgetStorage',
        font=('Verdana', 10))
    self.entry.pack(side=LEFT, padx=10)
    self.btn = Button(frame, text='Browse...')
    self.btn.pack(side=LEFT, ipadx=5, padx=5, pady=5)
    frame.pack()

4 This example is still a bit of a cheat because the done function still does not do very much! (However, I’m sure that you’ve got the idea by now!)

Figure 8.13 shows the sequence supported by the wizard. Screens such as these will clearly give a polished image for an installation program.