---
source_image: page_095.png
page_number: 95
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.50
tokens: 8293
characters: 1470
timestamp: 2025-12-24T00:34:04.326135
finish_reason: stop
---

4.3.25 ScrolledListbox

The ScrolledListbox widget is a convenience widget providing a ListBox widget with associated horizontal and vertical scrollbars. Figure 4.47 shows a typical ScrolledListbox.

![ScrolledListbox widget screenshot](./images/fig_4.47.png)

Figure 4.47 Pmw ScrolledListbox widget

box = None
def selectionCommand():
    sels = box.getcurselection()
    if len(sels) == 0:
        print 'No selection'
    else:
        print 'Selection:', sels[0]
box = Pmw.ScrolledListBox(root, listbox_selectmode=SINGLE,
    items=('John Cleese', 'Eric Idle', 'Graham Chapman',
        'Terry Jones', 'Michael Palin', 'Terry Gilliam'),
    labelpos=NW, label_text='Cast Members',
    listbox_height=5, vscrollmode='static',
    selectioncommand=selectionCommand,
    dblclickcommand=selectionCommand,
    usehullsize=1, hull_width=200, hull_height=200,)
box.pack(fill=BOTH, expand=1, padx=5, pady=5)

Documentation for the ScrolledListbox widget starts on page 598.

4.3.26 ScrolledText

The ScrolledText widget is a convenience widget providing a Text widget with associated horizontal and vertical scrollbars, as shown in figure 4.48.

st = Pmw.ScrolledText(root, borderframe=1, labelpos=N,
    label_text='Blackmail', usehullsize=1,
    hull_width=400, hull_height=300,
    text_padx=10, text_pady=10,
    text_wrap='none')
st.importfile('blackmail.txt')
st.pack(fill=BOTH, expand=1, padx=5, pady=5)

Documentation for the ScrolledText widget starts on page 600.