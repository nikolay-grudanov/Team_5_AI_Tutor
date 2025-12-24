---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.67
tokens: 8348
characters: 1829
timestamp: 2025-12-24T00:36:14.392347
finish_reason: stop
---

8 We create an About... dialog for the application. This is definitely something we could have left out, but now that you have seen it done once, I won’t need to cover it again. First, we define the data to be displayed by the dialog:

Pmw.aboutversion('8.1')
Pmw.aboutcopyright('Copyright My Company 1999'
    '\nAll rights reserved')
Pmw.aboutcontact(
    'For information about this application contact:\n' +
    '    My Help Desk\n' +
    '    Phone: 800 555-1212\n' +
    '    email: help@my.company.com')

9 Then the dialog is created and withdrawn (unmapped) so that it remains invisible until required:

self.about = Pmw.AboutDialog(master, applicationname = 'Example 8-1')
self.about.withdraw()

Example_8_4.py (continued)

def getStatus(self):
    username = self.userName.get()
    cardnumber = self.cardNumber.get()

    self.img = PhotoImage(file='%s.gif' % username)
    self.pictureID['image'] = self.img

    self.userInfo.importfile('%s.txt' % username)
    self.userInfo.configure(label_text = username)

def help(self):
    self.about.show()

def doDataForm(self):
    self.userName=Pmw.EntryField(self.dataFrame, entry_width=8,
        value='',
        modifiedcommand=self.upd_username,
        label_text='User name:',
        labelfpos=W, labelmargin=1)
    self.userName.place(relx=.20, rely=.325, anchor=W)

    self.cardNumber = Pmw.EntryField(self.dataFrame, entry_width=8,
        value='',
        modifiedcommand=self.upd_cardnumber,
        label_text='Card number:  ',
        labelfpos=W, labelmargin=1)
    self.cardNumber.place(relx=.20, rely=.70, anchor=W)

def doInfoForm(self):
    self.pictureID=Label(self.infoFrame, bd=0)
    self.pictureID.pack(side=LEFT, expand=1)

    self.userInfo = Pmw.ScrolledText(self.infoFrame,
        borderframe=1,
        labelfpos=N,
        usehullsize=1,