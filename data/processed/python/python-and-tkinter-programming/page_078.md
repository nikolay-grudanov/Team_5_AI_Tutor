---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.14
tokens: 8108
characters: 959
timestamp: 2025-12-24T00:33:21.838071
finish_reason: stop
---

Figure 4.26 Pmw ComboBox widget

4.3.5 ComboBoxDialog

The ComboBoxDialog widget provides a convenience dialog to allow the user to select an item from a ComboBox in response to a question. It is similar to a SelectionDialog widget except that it may allow the user to type in a value in the EntryField widget or select from a permanently displayed list or a dropdown list. An example is shown in figure 4.27.

choice = None
def choseEntry(entry):
    print 'You chose "%s"' % entry
    choice.configure(text=entry)

plays = ("The Taming of the Shrew", "Two Gentlemen of Verona", "Twelfth Night", "The Merchant of Venice", "Hamlet", "King Richard the Third")

dialog = Pmw.ComboBoxDialog(root, title = 'ComboBoxDialog',
    buttons=('OK', 'Cancel'), defaultbutton='OK',
    combobox_labelfpos=N, label_text='Which play?',
    scrolledlist_items=plays, listbox_width=22)
dialog.tkraise()

result = dialog.activate()
print 'You clicked on', result, dialog.get()