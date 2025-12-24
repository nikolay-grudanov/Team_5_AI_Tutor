---
source_image: page_234.png
page_number: 234
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.10
tokens: 8421
characters: 2127
timestamp: 2025-12-24T00:37:57.746233
finish_reason: stop
---

Here is the code to construct a BNC connector:

Components.py (fragment)

class BNC(GUICommon):
    def __init__(self, master, status=0, diameter=18,
        port=-1, fid=''):
        self.base = master['background']
        self.hitID = fid
        self.status=status
        self.blink      = 0
        self.blinkrate  = 1
        self.on         = 0
        self.onState    = None
        self.Colors     = [None, Color.CHROME, Color.ON,
            Color.WARN, Color.ALARM, '#00ffdd']

        basesize = diameter+6
        self.bnc_frame = Frame(master, relief="flat", bg=self.base,
            bd=0, highlightthickness=0, takefocus=1)
        self.bnc_frame.pack(expand=0)
        self.bnc_frame.bind('<FocusIn>', self.focus_in)
        self.bnc_frame.bind('<FocusOut>', self.focus_out)

        self.canvas=Canvas(self.bnc_frame, width=basesize,
            height=basesize, highlightthickness=0,
            bg=self.base, bd=0)
        center = basesize/2
        r = diameter/2
        self.pins=self.canvas.create_rectangle(0, center+2, basesize-1,
            10, fill=Color.CHROME)
        self.bnc=self.canvas.create_oval(center-r, center-r,
            center+r, center+r,
            fill=Color.CHROME,
            outline="black")
        r = r-3
        self.canvas.create_oval(center-r, center-r, center+r, center+r,
            fill=Color.INSIDE, outline='black')
        r = r-2
        self.canvas.create_oval(center-r, center-r, center+r, center+r,
            fill=Color.CHROME)
        r = r-3
        self.canvas.create_oval(center-r, center-r, center+r, center+r,
            fill=Color.INSIDE, outline='black')

        self.canvas.pack(side=TOP, fill=X, expand=0)
        if self.hitID:
            self.hitID = '%s.%d' % (self.hitID, port)
            for widget in [self.bnc_frame]:
                widget.bind('<KeyPress-space>', self.panelMenu)
                widget.bind('<Button-1>', self.panelMenu)
            for widget in [self.canvas]:
                widget.bind('<1>', self.panelMenu)

        def focus_in(self, event):
            self.last_bg= self.canvas.itemcget(self.bnc, 'fill')