---
source_image: page_086.png
page_number: 86
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.42
tokens: 8365
characters: 1698
timestamp: 2025-12-24T00:33:53.910921
finish_reason: stop
---

4.3.14 MessageDialog

The MessageDialog widget is a convenience dialog which displays a single message, which may be broken into multiple lines, and a number of buttons in a ButtonBox. It is useful for creating simple dialogs “on-the-fly.” Figure 4.36 shows an example.

![Screenshot of a simple dialog box with OK, Apply, Cancel, and Help buttons](./images/figure_4.36.png)

Figure 4.36 Pmw MessageDialog widget

dialog = Pmw.MessageDialog(root, title = 'Simple Dialog',
    defaultbutton = 0,
    buttons = ('OK', 'Apply', 'Cancel', 'Help'),
    message_text = 'This dialog box was constructed on demand')
dialog.iconname('Simple message dialog')

result = dialog.activate()
print 'You selected', result

Documentation for the MessageDialog widget starts on page 576.

4.3.15 NoteBookR

The NoteBookR widget implements the popular property sheet motif. Methods allow a number of pages or panes to be created. Any content may then be added to the panels. The user selects a panel by clicking on the tab at its top. Alternatively panels may be raised or lowered through instance methods. An example is shown in figure 4.37.

nb = Pmw.NoteBookR(root)
nb.add('p1', label='Page 1')
nb.add('p2', label='Page 2')
nb.add('p3', label='Page 3')

p1 = nb.page('p1').interior()
p2 = nb.page('p2').interior()
p3 = nb.page('p3').interior()

nb.pack(padx=5, pady=5, fill=BOTH, expand=1)
Button(p1, text='This is text on page 1', fg='blue').pack(pady=40)

c = Canvas(p2, bg='gray30')
w = c.winfo_reqwidth()
h = c.winfo_reqheight()
c.create_oval(10,10,w-10,h-10,fill='DeepSkyBlue1')
c.create_text(w/2,h/2,text='This is text on a canvas', fill='white',
    font=('Verdana', 14, 'bold'))
c.pack(fill=BOTH, expand=1)