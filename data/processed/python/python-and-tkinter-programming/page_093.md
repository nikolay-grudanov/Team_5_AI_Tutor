---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.54
tokens: 8278
characters: 1603
timestamp: 2025-12-24T00:34:00.032175
finish_reason: stop
---

4.3.23 ScrolledField

The ScrolledField widget provides a labeled EntryField widget with bindings to allow the user to scroll through data which is too great to be displayed within the available space. This widget should be reserved for very special uses, since it contravenes many of the commonly considered human factors for GUI elements. Figure 4.45 shows the effect of scrolling the field using the keyboard arrow keys.

![Figure 4.45 Pmw ScrolledField widget](https://i.imgur.com/3Q5z5QG.png)

Figure 4.45 Pmw ScrolledField widget

lines = (
    "Mount Everest. Forbidding, aloof, terrifying. This year, this",
    "remote Himalayan mountain, this mystical temple, surrounded by the",
    "most difficult terrain in the world, repulsed yet another attempt to",
    "conquer it. (Picture changes to wind-swept, snowy tents and people)",
    "This time, by the International Hairdresser's Expedition. In such",
    "freezing, adverse conditions, man comes very close to breaking",
    "point. What was the real cause of the disharmony which destroyed",
    "their chances at success?")

global index
field = index = None
def execute():
    global index
    field.configure(text=lines[index % len(lines)])
    index = index + 1
field = Pmw.ScrolledField(root, entry_width=30,
    entry_relief=GROOVE, labelpos=N,
    label_text='Scroll the field using the\nmiddle mouse button')
field.pack(fill=X, expand=1, padx=10, pady=10)

button = Button(root, text='Change field', command=execute)
button.pack(padx=10, pady=10)

index = 0
execute()

Documentation for the ScrolledField widget starts on page 594.