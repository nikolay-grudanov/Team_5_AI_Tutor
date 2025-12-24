---
source_image: page_329.png
page_number: 329
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.58
tokens: 8075
characters: 874
timestamp: 2025-12-24T00:40:21.653647
finish_reason: stop
---

Figure 12.1 Using the Tab key to select a frame

Once you have focus, you can activate the widget using the SPACE bar (this is the default SELECT key, certainly for Win32 and Motif) or you can click on any widget using the pointer. Notice in figure 12.2 that the Enable button shows that it has been traversed to using TAB key, but that we select Disable with the pointer. Keyboard focus remains with the Enable button, so pressing the SPACE key will re-enable the buttons.

Figure 12.2 Demonstrating the difference between keyboard and pointer focus

Text widgets use TAB keys as separators, so the default binding does not cause traversal out of the widget. In figure 12.3 you can see that tabs are inserted into the text. To move out of the widget we must use CTRL-TAB which is not bound to the Text widget.

Figure 12.3 Using CONTROL-TAB to navigate out of a Text widget