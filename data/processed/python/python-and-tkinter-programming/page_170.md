---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.91
tokens: 8391
characters: 2059
timestamp: 2025-12-24T00:36:12.734502
finish_reason: stop
---

import Pmw

class GetPassword(Dialog):
    def body(self, master):
        self.title("Enter New Password")

        Label(master, text='Old Password:').grid(row=0, sticky=W)
        Label(master, text='New Password:').grid(row=1, sticky=W)
        Label(master, text='Enter New Password Again:').grid(row=2, sticky=W)

        self.oldpw = Entry(master, width = 16, show='*')
        self.newpw1 = Entry(master, width = 16, show='*')
        self.newpw2 = Entry(master, width = 16, show='*')

        self.oldpw.grid(row=0, column=1, sticky=W)
        self.newpw1.grid(row=1, column=1, sticky=W)
        self.newpw2.grid(row=2, column=1, sticky=W)
        return self.oldpw

    def apply(self):
        opw = self.oldpw.get()
        npw1 = self.newpw1.get()
        npw2 = self.newpw2.get()

        if not npw1 == npw2:
            tkMessageBox.showerror('Bad Password',
                'New Passwords do not match')
        else:
            # This is where we would set the new password...
            pass

root = Tk()
dialog = GetPassword(root)

Code comments

① This example uses the grid geometry manager. The sticky attribute is used to make sure that the labels line up at the left of their grid cells (the default is to center the text in the cell). See “Grid” on page 86 for more details.

    Label(master, text='Old Password:').grid(row=0, sticky=W)

② Since we are collecting passwords from the user, we do not echo the characters that are typed. Instead, we use the show attribute to display an asterisk for each character.

    self.oldpw = Entry(master, width = 16, show='*')

③ When the user clicks the OK button, the apply callback gets the current data from the widgets. In a full implementation, the original password would be checked first. In our case we’re just checking that the user typed the same new password twice and if the passwords do not match we pop up an error dialog, using showerror.

    tkMessageBox.showerror('Bad Password',
        'New Passwords do not match')

Figure 8.3 illustrates the output of Example_8_3.py.