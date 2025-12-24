---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.26
tokens: 8278
characters: 1745
timestamp: 2025-12-24T00:33:25.434866
finish_reason: stop
---

4.3.1 AboutDialog

The AboutDialog widget provides a convenience dialog to present version, copyright and developer information. By providing a small number of data items the dialog can be displayed with minimal code. Figure 4.23 shows a typical AboutDialog.

![Screenshot of an About Dialog window showing version, copyright, contact info, and a close button](./images/aboutdialog.png)

Figure 4.23 Pmw AboutDialog widget

from Tkinter import *
import Pmw
root = Tk()
root.option_readfile('optionDB')
Pmw.initialise()

Pmw.aboutversion('1.5')
Pmw.aboutcopyright('Copyright Company Name 1999\nAll rights reserved')
Pmw.aboutcontact(
    'For information about this application contact:\n' +
    'Sales at Company Name\n' +
    'Phone: (401) 555-1212\n' +
    'email: info@company_name.com'
)
about = Pmw.AboutDialog(root, applicationname='About Dialog')

root.mainloop()

This widget is used in the AppShell class which will be presented in “A standard application framework” on page 155 and it is used in several examples later in the book.
Documentation for the AboutDialog widget starts on page 542.

4.3.2 Balloon

The Balloon widget implements the now somewhat familiar balloon help motif (this is sometimes called Tool Tips). The purpose of the widget is to display help information when the cursor is placed over a widget on the screen, normally after a short delay. Additionally (or alternatively) information may be displayed in a status area on the screen. The information in this area is removed after a short delay. This is illustrated in figure 4.24.

Although balloon help can be very helpful to novice users, it may be annoying to experts. If you provide balloon help make sure that you provide an option to turn off output to the