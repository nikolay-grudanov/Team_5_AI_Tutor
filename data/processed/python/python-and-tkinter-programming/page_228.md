---
source_image: page_228.png
page_number: 228
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.88
tokens: 8516
characters: 2318
timestamp: 2025-12-24T00:37:54.072406
finish_reason: stop
---

```python
self.canvas.create_oval(x-radius, y-radius,
                       x+radius, y+radius,
                       fill=self.dbase,
                       outline=self.lbase)

y = y + ssize

class PowerConnector:
    def __init__(self, master, bg=Color.PANEL):
        self.socket_frame = Frame(master, relief="raised", width=60,
                                  height=40, bg=bg, bd=4)
        inside=Frame(self.socket_frame, relief="sunken", width=56,
                     height=36, bg=Color.INSIDE, bd=2)
        inside.place(relx=.5, rely=.5, anchor=CENTER)
        ground=Frame(inside, relief="raised", width=6, height=10,
                     bg=Color.CHROME, bd=2)
        ground.place(relx=.5, rely=.3, anchor=CENTER)
        p1=Frame(inside, relief="raised", width=6, height=10,
                 bg=Color.CHROME, bd=2)
        p1.place(relx=.25, rely=.7, anchor=CENTER)
        p2=Frame(inside, relief="raised", width=6, height=10,
                 bg=Color.CHROME, bd=2)
        p2.place(relx=.75, rely=.7, anchor=CENTER)

class PowerSwitch(GUICommon):
    def __init__(self, master, label='I   0', base=Color.PANEL):
        self.base = base
        self.set_colors(master)
        self.switch_frame = Frame(master, relief="raised", width=45,
                                  height=28, bg=self.vlbase, bd=4)
        switch = Frame(self.switch_frame, relief="sunken", width=32,
                       height=22, bg=self.base, bd=2)
        switch.place(relx=0.5, rely=0.5, anchor=CENTER)
        lbl=Label(switch, text=label, font=("Verdana", 10, "bold"),
                  fg='white', bd=0, bg=self.dbase)
        lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

class PowerSupply(GUICommon):
    def __init__(self, master, width=160, height=130, bg=Color.PANEL,
                  status=STATUS_ON):
        self.base = bg
        self.set_colors(master)
        self.psu_frame = Frame(master, relief=SUNKEN, bg=self.dbase, bd=2,
                               width=width, height=height)
        Label(self.psu_frame, text='DC OK', fg='white',
              bg=self.dbase, font=('Verdana', 10, 'bold'),bd=0).place(relx=.8,
              rely=.15, anchor=CENTER)
        self.led = LED(self.psu_frame, height=12, width=12, shape=ROUND,
                       bg=self.dbase)
```

**Calculating colors**