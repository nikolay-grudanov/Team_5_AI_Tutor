---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.82
tokens: 8472
characters: 2082
timestamp: 2025-12-24T00:37:47.046438
finish_reason: stop
---

self.led.led_frame.place(relx=0.8, rely=0.31, anchor=CENTER)

lsub = Frame(self.psu_frame, width=width/1.2, height=height/2,
    bg=self.dbase, bd=1, relief=GROOVE)
lsub.place(relx=0.5, rely=0.68, anchor=CENTER)

pwr=PowerConnector(lsub)
pwr.socket_frame.place(relx=0.30, rely=0.5, anchor=CENTER)
sw=PowerSwitch(lsub)
sw.switch_frame.place(relx=0.75, rely=0.5, anchor=CENTER)

class Screw(GUICommon):
    def __init__(self, master, diameter=18, base="gray40", bg=Color.PANEL):
        self.base = base

        basesize = diameter+6
        self.screw_frame = Frame(master, relief="flat", bg=bg, bd=0,
            highlightthickness=0)
        self.set_colors(self.screw_frame)

        canvas=Canvas(self.screw_frame, width=basesize, height=basesize,
            highlightthickness=0, bg=bg, bd=0)
        center = basesize/2
        r = diameter/2
        r2 = r - 4.0

        canvas.create_oval(center-r, center-r, center+r, center+r,
            fill=self.base, outline=self.lbase)
        canvas.create_rectangle(center-r2, center-0.2,
            center+r2, center+0.2,
            fill=self.dbase, width=0)
        canvas.create_rectangle(center-0.2, center-r2,
            center+0.2, center+r2,
            fill=self.dbase, width=0)
        canvas.pack(side="top", fill='x', expand='no')

class CardBlank(GUICommon):
    def __init__(self, master=None, width=20, height=396,
        appearance="raised", bd=2, base=Color.CARD):
        self.base = base
        self.set_colors(master)
        self.card_frame=Frame(master, relief=appearance, height=height,
            width=width, bg=base, bd=bd)

        top_pull = CardPuller(self.card_frame, CARD_TOP, width=width)
        top_pull.puller_frame.place(relx=.5, rely=0, anchor=N)

        bottom_pull = CardPuller(self.card_frame, CARD_BOTTOM, width=width)
        bottom_pull.puller_frame.place(relx=.5, rely=1.0, anchor=S)


Code comments
① In some of the earlier examples we used Tkinter’s internal reference to the instance of the widgets, so the following was possible:
    Button(parent, text='OK').pack(side=LEFT)