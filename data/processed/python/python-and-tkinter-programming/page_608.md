---
source_image: page_608.png
page_number: 608
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.00
tokens: 8072
characters: 925
timestamp: 2025-12-24T00:48:57.296853
finish_reason: stop
---

Components

containerCanvas
By default, this component is a Canvas.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

mainCanvas
By default, this component is a Canvas.

tabCanvas
By default, this component is a Canvas.

Methods

addPage(name)
Creates a Frame within the notebook associated with name name.

delPage(name)
Deletes the pane (Frame) associated with name name.

getPage(name)
Returns the panel (Frame) associated with name name. Does not raise the specified panel to the top of the stack.

pageNames()
Returns a list of all the page names currently defined for the notebook.

pages()
Returns a list of all the panes (Frames) currently defined for the notebook.

raisePage(name, select = 1)
Raises the pane associated with name name to the top of the stack. If select is false, do not deselect the currently active pane.