---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.83
tokens: 8186
characters: 1250
timestamp: 2025-12-24T00:38:56.153548
finish_reason: stop
---

if ids:
    id = ids[0]
    if not 'text' in self.canvas.gettags(CURRENT):
        id = id+1
    print 'You clicked on %s' % \
        self.canvas.itemcget(id, 'text')

First we find all the ids with the CURRENT tag (this will be either the rectangle or the text field at its center). We only care about the first tag.
Then, we check to see if it is the text object. If it is not, the next id will be the text object, since we defined the rectangle first.
Last, we get the text object’s contents which give the row-column coordinates.

10.4 Ruler-class tools

Another common drawing tool is a ruler. This can be used to provide tab stops or other constraint graphics. It also illustrates some of the aspects of drag-and-drop from within an application. This example was also recoded from a Tk example.

![A simple ruler tool](ruler.png)

Figure 10.8 A simple ruler tool

ruler.py

from Tkinter import *

class Ruler:
    def __init__(self, master, width='14.8c', height='2.5c'):
        Label(master, text="This canvas widget shows a mock-up of a "
            "ruler. You can create tab stops by dragging them out "
            "of the well to the right of the ruler. You can also "
            "drag existing tab stops. If you drag a tab stop far "