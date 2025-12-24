---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.63
tokens: 8230
characters: 1226
timestamp: 2025-12-24T00:33:49.715918
finish_reason: stop
---

items= ('Stockbroker', 'Quantity Surveyor', 'Church Warden', 'BRM'),
    menubutton_width=16)
opt_menu.pack(anchor=W, padx=20, pady=30)

Documentation for the OptionMenu widget starts on page 584.

4.3.19 PanedWidget

The PanedWidget widget creates a manager containing multiple frames. Each frame is a container for other widgets and may be resized by dragging on its handle or separator line. The area within each pane is managed independently, so a single pane may be grown or shrunk to modify the layout of its children. Figure 4.41 shows an example.

![PanedWidget example](./images/panedwidget.png)

Figure 4.41 Pmw PanedWidget widget

pane = Pmw.PanedWidget(root, hull_width=400, hull_height=300)
pane.add('top', min=100)
pane.add('bottom', min=100)

topPane = Pmw.PanedWidget(pane.pane('top'), orient=HORIZONTAL)
for num in range(4):
    if num == 1:
        name = 'Fixed\nSize'
        topPane.add(name, min=.2, max=.2)
    else:
        name = 'Pane\n' + str(num)
        topPane.add(name, min=.1, size=.25)
    button = Button(topPane.pane(name), text=name)
    button.pack(expand=1)
    topPane.pack(expand=1, fill=BOTH)
pane.pack(expand=1, fill=BOTH)

Documentation for the PanedWidget widget starts on page 586.