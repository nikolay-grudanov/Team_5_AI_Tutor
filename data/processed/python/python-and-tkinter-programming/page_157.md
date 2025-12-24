---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.26
tokens: 8491
characters: 2430
timestamp: 2025-12-24T00:35:58.067160
finish_reason: stop
---

```python
class HexNut(GUICommon):
    def __init__(self, master, frame=1, mount=1, outside=70, inset=8,
                 bg=Color.PANEL, nutbase=Color.BRONZE,
                 top=NUT_FLAT, takefocus=0, x=-1, y=-1):
        points = [ '%d-r2,%d+r,%d+r2,%d+r,%d+r+2,%d,%d+r2,%d-r,\n\
                   %d-r2,%d-r,%d-r-2,%d,%d-r2,%d+r',
                   '%d,%d-r-2,%d+r,%d-r2,%d+r,%d+r2,%d,%d+r+2,\n\
                   %d-r,%d+r2,%d-r,%d-r2,%d,%d-r-2' ]
        self.base   = nutbase
        self.status = STATUS_OFF
        self.blink  = 0
        self.set_colors()
        basesize = outside+4
        if frame:
            self.frame = Frame(master, relief="flat", bg=bg, bd=0,
                               highlightthickness=0,
                               takefocus=takefocus)
            self.frame.pack(expand=0)
            self.canv=Canvas(self.frame, width=basesize, bg=bg,
                             bd=0, height=basesize,
                             highlightthickness=0)
        else:
            self.canv = master      # it was passed in...
        center = basesize/2
        if x >= 0:
            centerx = x
            centery = y
        else:
            centerx = centery = center
        r = outside/2
        ## First, draw the mount, if needed
        if mount:
            self.mount=self.canv.create_oval(centerx-r, centery-r,
                                            centerx+r, centery+r,
                                            fill=self.dbase,
                                            outline=self.vdbase)
        ## Next, draw the hex nut
        r = r - (inset/2)
        r2 = r/2
        pointlist = points[top] % (centerx,centery,centerx,centery,
                                   centerx,centery,centerx,centery,
                                   centerx,centery,centerx,centery,
                                   centerx,centery)
        setattr(self, 'hexnut', self.canv.create_polygon(pointlist,
                                                        outline=self.dbase, fill=self.lbase))
        ## Now, the inside edge of the threads
        r = r - (inset/2)
        self.canv.create_oval(centerx-r, centery-r,
                              centerx+r, centery+r,
                              fill=self.lbase, outline=self.vdbase)
        ## Finally, the background showing through the hole
        r = r - 2
        self.canv.create_oval(centerx-r, centery-r,
```