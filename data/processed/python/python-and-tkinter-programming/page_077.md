---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.24
tokens: 8389
characters: 1934
timestamp: 2025-12-24T00:33:37.510906
finish_reason: stop
---

def buttonPress(btn):
    print 'The "%s" button was pressed' % btn
def defaultKey(event):
    buttonBox.invoke()

buttonBox = Pmw.ButtonBox(root, labelpos='nw', label_text='ButtonBox:')
buttonBox.pack(fill=BOTH, expand=1, padx=10, pady=10)

buttonBox.add('OK', command = lambda b='ok': buttonPress(b))
buttonBox.add('Apply', command = lambda b='apply': buttonPress(b))
buttonBox.add('Cancel', command = lambda b='cancel': buttonPress(b))

buttonBox.setdefault('OK')
root.bind('<Return>', defaultKey)
root.focus_set()
buttonBox.alignbuttons()

Documentation for the Buttonbox widget starts on page 546.

4.3.4 ComboBox

The ComboBox widget is an important widget, originally found on Macintosh and Windows interfaces and later on Motif. It allows the user to select from a list of options, which, unlike an OptionMenu, may be scrolled to accommodate large numbers of selections. The list may be displayed permanently, such as the example at the left of figure 4.26 or as a dropdown list, shown at the right of figure 4.26. Using the dropdown form results in GUIs which require much less space to implement complex interfaces.

choice = None
def choseEntry(entry):
    print 'You chose "%s"' % entry
    choice.configure(text=entry)

asply = ("The Mating of the Wersh", "Two Netlemeng of Verona", "Twelfth Thing", "The Chamrent of Venice", "Thamle", "Ring Kichard the Thrid")

choice = Label(root, text='Choose play', relief='sunken', padx=20, pady=20)
choice.pack(expand=1, fill='both', padx=8, pady=8)

combobox = Pmw.ComboBox(root, label_text='Play:', labelpos='wn',
    listbox_width=24, dropdown=0,
    selectioncommand=choseEntry,
    scrolledlist_items=asply)
combobox.pack(fill=BOTH, expand=1, padx=8, pady=8)
combobox.selectitem(asply[0])

# ==========
combobox = Pmw.ComboBox(root, label_text='Play:', labelpos='wn',
    listbox_width=24, dropdown=1,
    ...
    ...

Documentation for the ComboBox widget starts on page 549.