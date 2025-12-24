---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.32
tokens: 7998
characters: 467
timestamp: 2025-12-24T00:33:29.676943
finish_reason: stop
---

Figure 4.37 Pmw NoteBookR widget

Documentation for the NotebookR widget starts on page 580.

4.3.16 NoteBookS

The NoteBookS widget implements an alternative style of NoteBook. NoteBookS provides additional options to control the color, dimensions and appearance of the tabs. Otherwise it is quite similar to NoteBookR. Figure 4.38 illustrates a similar layout using NotebookS.

nb = Pmw.NoteBookS(root)
nb.addPage('Page 1')
nb.addPage('Page 2')
nb.addPage('Page 3')