---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.95
tokens: 7994
characters: 483
timestamp: 2025-12-24T00:33:43.229747
finish_reason: stop
---

Figure 4.48 Pmw ScrolledText widget

4.3.27 SelectionDialog

The SelectionDialog widget provides a convenience dialog to allow the user to select an item from a ScrolledList in response to a question. It is similar to a ComboBoxDialog except that there is no provision for the user to type in a value. Figure 4.49 shows an example.

dialog = None
def execute(result):
    sels = dialog.getcurselection()
    if len(sels) == 0:
        print 'You clicked on', result, '(no selection)'