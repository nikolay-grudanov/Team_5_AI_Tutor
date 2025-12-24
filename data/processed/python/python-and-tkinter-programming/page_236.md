---
source_image: page_236.png
page_number: 236
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.43
tokens: 8674
characters: 2521
timestamp: 2025-12-24T00:38:10.826158
finish_reason: stop
---

self.on = 1
# now update the status
self.canvas.itemconfig(self.bnc, fill=self.Colors[self.status])
self.canvas.itemconfig(self.pins, fill=self.Colors[self.status])
self.bnc_frame.update_idletasks()
if self.blink:
    self.bnc_frame.after(self.blinkrate * 1000, self.update)

Now, we complete the example by defining the layout of the T3 Access card:

class StandardLEDs(GUICommon):
    def __init__(self, master=None, bg=Color.CARD):
        for led, label, xpos, ypos, state in [(
            'flt', 'Flt', 0.3, 0.88, 1),
            ('pwr', 'Pwr', 0.7, 0.88, 2)]:
            setattr(self, led, LED(self.card_frame, shape=ROUND, width=8,
                status=state, bg=bg))
            getattr(self, led).led_frame.place(relx=xpos, rely=ypos,
                anchor=CENTER)
            Label(self.card_frame, text=label, font=("verdana", 4),
                fg="white", bg=bg).place(relx=xpos, rely=(ypos+0.028),
                anchor=CENTER)

class T3AccessCard(CardBlank, StandardLEDs):
    def __init__(self, master, width=1, height=1):
        CardBlank.__init__(self, master=master, width=width, height=height)
        bg=master['background']
        StandardLEDs.__init__(self, master=master, bg=bg)
        for port, lbl, tag, ypos in [
            (1,'RX1','T3AccessRX', 0.30),
            (2,'TX1','T3AccessTX', 0.40),
            (3,'RX2','T3AccessRX', 0.65),
            (4,'TX2','T3AccessRX', 0.75)]:
            setattr(self, 'bnc%d' % port, BNC(self.card_frame,
                fid=tag,port=port))
            getattr(self, 'bnc%d' % port).bnc_frame.place(relx=0.5,
                rely=ypos,anchor=CENTER))
            Label(self.card_frame, text=lbl,
                font=("verdana", 6), fg="white",
                bg=bg).place(relx=0.5,rely=(ypos+0.045),anchor=CENTER)
        for led, lbl, xpos, ypos, state in [
            ('rxc','RXC',0.3,0.18,2),
            ('oos','OOS',0.7,0.18,1),
            ('flt','FLT',0.3,0.23,1),
            ('syn','SYN',0.7,0.23,2),
            ('rxc','RXC',0.3,0.53,2),
            ('oos','OOS',0.7,0.53,1),
            ('flt','FLT',0.3,0.58,1),
            ('syn','SYN',0.7,0.58,2)]:
            setattr(self, led, LED(self.card_frame, shape=ROUND, width=8,
                status=state, bg=bg))
            getattr(self, led).led_frame.place(relx=xpos, rely=ypos,
                anchor=CENTER)
            Label(self.card_frame, text=lbl,
                font=("verdana", 4), fg="white",
                bg=bg).place(relx=xpos, rely=(ypos+0.028),anchor=CENTER)