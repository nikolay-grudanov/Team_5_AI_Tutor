---
source_image: page_160.png
page_number: 160
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.57
tokens: 8454
characters: 2013
timestamp: 2025-12-24T00:36:02.340324
finish_reason: stop
---

```python
self.p1=self.canvas.create_polygon(self.center-self.r,
    self.center, self.center-self.r-3,
    self.center-(4*self.r), self.center+self.r+3,
    self.center-(4*self.r), self.center+self.r,
    self.center, fill=self.dbase,
    outline=self.vdbase, tags="lever")
centerx = self.center
centery = self.center - (4*self.r)
r = self.r + 2
## Draw the end of the lever
self.r2=self.canv.create_oval(centerx-r, centery-r,
    centerx+r, centery+r, fill=self.base,
    outline=self.vdbase, width=1, tags="lever")
centerx = centerx - 1
centery = centery - 3
r = r / 3
## Draw the highlight
self.r2=self.canv.create_oval(centerx-r, centery-r,
    centerx+r, centery+r, fill=self.vlbase,
    outline=self.lbase, width=2, tags="lever")
else:
    ## Draw the toggle lever
    self.p1=self.canv.create_polygon(self.center-self.r,
        self.center, self.center-self.r-3,
        self.center+(4*self.r), self.center+self.r+3,
        self.center+(4*self.r), self.center+self.r,
        self.center, fill=self.dbase,
        outline=self.vdbase, tags="lever")
    centerx = self.center
    centery = self.center + (4*self.r)
    r = self.r + 2
    ## Draw the end of the lever
    self.r2=self.canv.create_oval(centerx-r, centery-r,
        centerx+r, centery+r, fill=self.base,
        outline=self.vdbase, width=1, tags="lever")
    centerx = centerx - 1
    centery = centery - 3
    r = r / 3
    ## Draw the highlight
    self.r2=self.canv.create_oval(centerx-r, centery-r,
        centerx+r, centery+r, fill=self.vlbase,
        outline=self.lbase, width=2, tags="lever")
self.canv.update_idletasks()

class TestSwitches(Frame, GUICommon):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        # List of metals to create
        metals = (Color.BRONZE, Color.CHROME, Color.BRASS)
        # List of switches to display, with sizes and other attributes
        switches = [(NUT_POINT, 0, STATUS_OFF, MODE_US),
```