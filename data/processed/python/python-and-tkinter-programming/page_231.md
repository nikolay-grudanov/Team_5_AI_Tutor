---
source_image: page_231.png
page_number: 231
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.00
tokens: 8570
characters: 2128
timestamp: 2025-12-24T00:37:57.706596
finish_reason: stop
---

anchor=[NE,SE][torb])
Screw(self.puller_frame, diameter=10, base=self.base,
    bg=self.lbase).screw_frame.place(relx=0.3, rely=[0.2,0.8][torb],
        anchor=CENTER)

class Chassis:
    def __init__(self, master):
        self.outer=Frame(master, width=540, height=650,
            borderwidth=2, bg=Color.PANEL)
        self.outer.forget()

        self.inner=Frame(self.outer, width=490, height=650,
            borderwidth=2, relief=RAISED, bg=Color.PANEL)
        self.inner.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.rack = Frame(self.inner, bd=2, width=325, height=416,
            bg=Color.CHASSIS)
        self.rack.place(relx=0.985, rely=0.853, anchor=SE)

        incr = 325/9
        x = 0.0
        for i in range(9):
            card =CardBlank(self.rack, width=incr-1, height=414)
            card.card_frame.place(x=x, y=0, anchor=NW)
            x = x + incr

        self.img = PhotoImage(file='images/logo.gif')
        self.logo=Label(self.outer, image=self.img, bd=0)
        self.logo.place(relx=0.055, rely=0.992, anchor=SW)

        for x in [0.02, 0.98]:
            for y in [0.0444, 0.3111, 0.6555, 0.9711]:
                screw = Screw(self.outer, base="gray50")
                screw.screw_frame.place(relx=x, rely=y, anchor=CENTER)

        self.psu1 = PowerSupply(self.inner)
        self.psu1.psu_frame.place(relx=0.99, rely=0.004, anchor=NE)
        self.psu2 = PowerSupply(self.inner)
        self.psu2.psu_frame.place(relx=0.65, rely=0.004, anchor=NE)

        self.psu2.led.turnoff()

        screen1 = Screen(self.inner, width=150, height=600, bg=Color.PANEL)
        screen1.screen_frame.place(relx=0.16, rely=0.475, anchor=CENTER)
        screen2 = Screen(self.inner, width=330, height=80, bg=Color.PANEL)
        screen2.screen_frame.place(relx=0.988, rely=0.989, anchor=SE)

7 Creating blank cards

8 Deactivating LED

Code comments (continued)

4 In the CardPuller class we obtain the base color from the parent widget, rather than passing it in the constructor.

def __init__(self, master, torb, width=20):
    self.base = master['background']
    self.set_colors(master)