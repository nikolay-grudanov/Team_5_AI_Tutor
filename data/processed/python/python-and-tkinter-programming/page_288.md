---
source_image: page_288.png
page_number: 288
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.05
tokens: 8088
characters: 1004
timestamp: 2025-12-24T00:39:10.130165
finish_reason: stop
---

Figure 10.10 Adding movement and stretching to the drawing program

transDict = { 'bx': 'boundX', 'by': 'boundY',
              'x': 'adjX',   'y': 'adjY',
              'S': 'uniqueIDINT' }

class Draw(AppShell.AppShell):
    # --- Code Removed -------------------------------------------------------------
    def createMenus(self):
        self.menuBar.deletemenuitems('File')
        self.menuBar.addmenuitem('File', 'command', 'New drawing',
                                 label='New', command=self.newDrawing)
        self.menuBar.addmenuitem('File', 'command', 'Open drawing',
                                 label='Open...', command=self.openDrawing)
        self.menuBar.addmenuitem('File', 'command', 'Save drawing',
                                 label='Save', command=self.saveDrawing)
        self.menuBar.addmenuitem('File', 'command', 'Save drawing',
                                 label='SaveAs...', command=self.saveAsDrawing)
        self.menuBar.addmenuitem('File', 'separator')