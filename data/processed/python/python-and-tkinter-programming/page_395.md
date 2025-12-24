---
source_image: page_395.png
page_number: 395
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.10
tokens: 8355
characters: 2253
timestamp: 2025-12-24T00:42:35.948987
finish_reason: stop
---

def __init__(self, master=None):
    self.master = master
    self.frame = Frame(master, relief=RAISED, borderwidth=2)
    Label(self.frame, text='Press the button\nnto start operation').pack()
    self.frame.pack(padx=4, pady=4)
    Button(master, text='Start', command=self.startOP).pack(side=TOP)

def startOP(self):
    self.displayBusyCursor()
    time.sleep(10.0)  # simulate a long operation

def displayBusyCursor(self):
    self.master.configure(cursor='watch')
    self.master.update()
    self.master.after_idle(self.removeBusyCursor)

def removeBusyCursor(self):
    self.master.configure(cursor='arrow')

root = Tk()
root.option_readfile('optionDB2')
root.title('Busy Cursor')
AfterIdleExample(root)
root.mainloop()

Code comments
① displayBusyCursor changes the cursor to an appropriate cursor and then calls update to make sure that the cursor is displayed before the long operation starts.
② The after_idle method registers the removeBusyCursor which will be called when the event queue is empty. There is no opportunity for the mainloop to spin until after the sleep has ended.
③ All that removeBusyCursor has to do is restore the cursor.

Note In a full implementation, the busy cursor implementation would be more general so you should probably get the current cursor and store it so that you can restore the same cursor.

Another method can be used to process asynchronous operations. Unfortunately, in the current release of Tcl/Tk, this currently works only for UNIX. In Tk version 8.0, support for Win32 was suddenly withdrawn for createfilehandler which is equivalent to XtAppAddInput in the X Window world. It allows you to bind a callback which is run when a file-class operation occurs. This currently works for sockets. I would normally exclude a method which is exclusive to a particular operating system, but this one is useful enough to warrant inclusion.

Many applications have requirements to respond to an external event, such as receiving data on a socket. You have several choices in implementing a system, but normally you would choose either to block, waiting for input; or poll, on a periodic basis, until data is received. Now, when a GUI is involved, you clearly cannot block unless that occurs within a thread.