---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.06
tokens: 8327
characters: 1664
timestamp: 2025-12-24T00:33:07.108288
finish_reason: stop
---

If the indicatoron flag is set to FALSE, the radiobutton group behaves as a button box, as shown in figure 4.10. The selected button is normally indicated with a SUNKEN relief.

var = IntVar()
for text, value in [('Red Leicester', 1), ('Tilsit', 2), ('Caerphilly', 3),
                    ('Stilton', 4), ('Emental', 5),
                    ('Roquefort', 6), ('Brie', 7)]:
    Radiobutton(root, text=text, value=value, variable=var,
                indicatoron=0).pack(anchor=W, fill=X, ipadx=18)
var.set(3)

![Radiobuttons: indicatoron=0](https://i.imgur.com/3Q5z5QG.png)

Figure 4.10  Radiobuttons: indicatoron=0

Documentation for the Radiobutton widget starts on page 519.

4.1.7 Checkbutton

Checkbutton widgets are used to provide on/off selections for one or more items. Unlike radiobuttons (see “Radiobutton” on page 37) there is no interaction between checkbuttons. You may load checkbuttons with either text or images. Checkbuttons should normally have a variable (IntVar) assigned to the variable option which allows you to determine the state of the checkbutton. In addition (or alternately) you may bind a callback to the button which will be called whenever the button is pressed.

Note that the appearance of checkbuttons is quite different on UNIX and Windows; UNIX normally indicates selection by using a fill color, whereas Windows uses a checkmark. The Windows form is shown in figure 4.11.

![Checkbutton widget](https://i.imgur.com/3Q5z5QG.png)

Figure 4.11  Checkbutton widget

for castmember, row, col, status in [
    ('John Cleese', 0,0,NORMAL), ('Eric Idle', 0,1,NORMAL),
    ('Graham Chapman', 1,0,DISABLED), ('Terry Jones', 1,1,NORMAL),