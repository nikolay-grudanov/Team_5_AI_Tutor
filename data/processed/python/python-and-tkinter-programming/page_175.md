---
source_image: page_175.png
page_number: 175
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.96
tokens: 8125
characters: 1081
timestamp: 2025-12-24T00:36:06.909063
finish_reason: stop
---

Code comments (continued)

10 getStatus is a placeholder for a more realistic function that can be applied to the collected data. First, we use the get methods of the Pmw widgets to obtain the content of the widgets:

username = self.userName.get()
cardnumber = self.cardNumber.get()

11 Using username, we retrieve an image and load it into the label widget we created earlier:

self.img = PhotoImage(file='%s.gif' % username)
self.pictureID['image'] = self.img

12 Then we load the contents of a file into the ScrolledText widget and update its title:

self.userInfo.importfile('%s.txt' % username)
self.userInfo.configure(label_text = username)

13 Using the About dialog is simply a matter of binding the widget’s show method to the menu item:

def help(self):
    self.about.show()

14 The form itself uses two Pmw EntryField widgets to collect data:

self.userName=Pmw.EntryField(self.dataFrame, entry_width=8,
    value='',
    modifiedcommand=self.upd_username,
    label_text='User name:',
    labelfpos=W, labelmargin=1)
self.userName.place(relx=.20, rely=.325, anchor=W)