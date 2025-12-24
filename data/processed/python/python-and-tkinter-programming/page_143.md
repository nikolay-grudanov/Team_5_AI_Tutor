---
source_image: page_143.png
page_number: 143
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.24
tokens: 8290
characters: 1571
timestamp: 2025-12-24T00:35:21.943711
finish_reason: stop
---

def createField(self, master, label='', text='', width=1,
    format=None, enter=None, row=0, col=0):
    Label(master, text=label).grid(row=row, column=col-1,
        padx=15, sticky=W)
    id = Entry(master, text=text, width=width, takefocus=1)
    id.bind('<KeyRelease>', format)   ②
    id.bind('<Return>', enter)
    id.grid(row=row, column=col, pady=10, sticky=W)
    return id

def activate(self, event):
    print '<Return>: value is', event.widget.get()

def fmtPhone(self, event):
    current = event.widget.get()
    if len(current) == 1:
        current = '1-(%s' % current
    elif len(current) == 6:
        current = '%s)-' % current
    elif len(current) == 11:
        current = '%s-' % current
    event.widget.delete(0, END)
    event.widget.insert(0, current)

def fmtSSN(self, event):
    current = event.widget.get()
    if len(current) in [3, 6]:
        current = '%s-' % current
    event.widget.delete(0, END)
    event.widget.insert(0, current)

root = Tk()
root.title('Entry Formatting')

top = EntryFormatting(root)
quit = Button(root, text='Quit', command=root.destroy)
quit.pack(side = 'bottom')

root.mainloop()

Code comments
① The createField method provides a wrapper to bind a formatting function that runs whenever the user presses a key.
② This is the binding that initiates the formatting.
③ The fmtPhone method has to count the digits entered into the field to supply the additional separators.
④ Similarly, fmtSSN inserts hyphens at the appropriate positions.

If you run Example_6_9.py, you will see output similar to figure 6.4.