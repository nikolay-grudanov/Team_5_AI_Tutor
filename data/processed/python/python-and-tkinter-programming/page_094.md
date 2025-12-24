---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.95
tokens: 8162
characters: 964
timestamp: 2025-12-24T00:33:53.675923
finish_reason: stop
---

4.3.24 ScrolledFrame

The ScrolledFrame widget is a convenience widget providing a Frame widget with associated horizontal and vertical scrollbars. An example is shown in figure 4.46.

![ScrolledFrame widget screenshot](./images/fig_4_46.png)

Figure 4.46 Pmw ScrolledFrame widget

global row, col
row = col = 0
sf = frame = None
def addButton():
    global row, col
    button = Button(frame, text = '(%d,%d)' % (col, row))
    button.grid(row=row, col=col, sticky='nsew')
    frame.grid_rowconfigure(row, weight=1)
    frame.grid_columnconfigure(col, weight=1)
    sf.reposition()
    if col == row:
        col = 0
        row = row + 1
    else:
        col = col + 1

sf = Pmw.ScrolledFrame(root, labelpos=N, label_text='ScrolledFrame',
    usehullsize=1, hull_width=400, hull_height=220)
sf.pack(padx=5, pady=3, fill='both', expand=1)
frame = sf.interior()

for i in range(250):
    addButton()

Documentation for the ScrolledFrame widget starts on page 595.