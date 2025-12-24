---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.96
tokens: 8343
characters: 1749
timestamp: 2025-12-24T00:33:43.138174
finish_reason: stop
---

4.3.8 Dialog

The Dialog widget provides a simple way to create a toplevel containing a ButtonBox and a child site area. You may populate the child site with whatever your application requires. Figure 4.30 shows an example of a Dialog.

![Screenshot of a Pmw Dialog window showing "Pmw Dialog Bring out your dead!" with OK, Apply, Cancel, and Help buttons](../images/fig4_30.png)

Figure 4.30 Pmw Dialog widget

dialog = Pmw.Dialog(root, buttons=('OK', 'Apply', 'Cancel', 'Help'),
    defaultbutton='OK', title='Simple dialog')
w = Label(dialog.interior(), text='Pmw Dialog\nBring out your dead!',
    background='black', foreground='white', pady=20)
w.pack(expand=1, fill=BOTH, padx=4, pady=4)
dialog.activate()

Documentation for the Dialog widget starts on page 558.

4.3.9 EntryField

The EntryField widget is an Entry widget with associated validation methods. The built-in validation provides validators for integer, hexadecimal, alphabetic, alphanumeric, real, time and date data formats. Some of the controls that may be placed on the validation include checking conformity with the selected data format and checking that entered data is between minimum and maximum limits. You may also define your own validators. A few examples are shown in figure 4.31.

![Screenshot of a Pmw EntryField window showing validation examples for No validation, Real (96.0 to 107.0), Integer (5 to 42), and Date (in 2000)](../images/fig4_31.png)

Figure 4.31 Pmw EntryField widget

noval = Pmw.EntryField(root, labelpos=W, label_text='No validation',
    validate = None)

real = Pmw.EntryField(root, labelpos=W, value = '98.4',
    label_text = 'Real (96.0 to 107.0):',
    validate = {'validator' : 'real',
        'min' : 96, 'max' : 107, 'minstrict' : 0})