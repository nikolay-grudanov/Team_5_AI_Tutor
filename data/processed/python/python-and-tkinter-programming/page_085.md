---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.41
tokens: 8209
characters: 1350
timestamp: 2025-12-24T00:33:37.510594
finish_reason: stop
---

messagetype = sels[0]
if messagetype == 'state':
    messagebar.message('state', 'Change of state message')
else:
    text = messages[messagetype]
    messagebar.message(messagetype, text)

messages = { 'help'      : 'Save current file',
             'userevent' : 'Saving file "foo"',
             'busy'      : 'Busy deleting all files from file system ...',
             'systemevent': 'File "foo" saved',
             'usererror' : 'Invalid file name "foo/bar"',
             'systemerror': 'Failed to save file: file system full',
             }

messagebar = Pmw.MessageBar(root, entry_width=40, entry_relief=GROOVE,
                            labelfpos=W, label_text='Status:')
messagebar.pack(side=BOTTOM, fill=X, expand=1, padx=10, pady=10)

box = Pmw.ScrolledListBox(root, listbox_selectmode=SINGLE,
                          items=('state', 'help', 'userevent', 'systemevent',
                                 'usererror', 'systemerror', 'busy',),
                          label_text='Message type', labelfpos=N,
                          selectioncommand=selectionCommand)
box.pack(fill=BOTH, expand=1, padx=10, pady=10)

Documentation for the MessageBar widget starts on page 574.

![Screenshot of the Pmw MessageBar widget showing a list of message types and a status bar](./images/figure_4.35.png)

Figure 4.35  Pmw MessageBar widget