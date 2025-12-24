---
source_image: page_198.png
page_number: 198
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.93
tokens: 8003
characters: 504
timestamp: 2025-12-24T00:36:38.903284
finish_reason: stop
---

Code comments

1 Creating a notebook within the AppShell is simply a case of creating a Pmw NoteBookR component.

def createNotebook(self):
    self.notebook = self.createcomponent('notebook', (), None,
        Pmw.NoteBookR, (self.interior(),),)
    self.notebook.pack(side=TOP, expand=YES, fill=BOTH, padx=5, pady=5)

Pmw provides an alternate notebook widget, NoteBookS (see figure 8.10 on page 174 for an example). I do not recommend that you use this widget since it has a generally inferior layout.