---
source_image: page_237.png
page_number: 237
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.95
tokens: 8409
characters: 1989
timestamp: 2025-12-24T00:38:02.223357
finish_reason: stop
---

Code comments

1 We add one class to draw the LEDs that appear on each card in the rack:
    class StandardLEDs(GUICommon):
2 The T3 access card inherits from the CardBlank and StandardLEDs classes which are explicitly constructed:
    class T3AccessCard(CardBlank,StandardLEDs):
        def __init__(self, master, width=1, height=1):
            CardBlank.__init__(self, master=master, width=width, height=height) bg=master['background']
            StandardLEDs.__init__(self, master=master, bg=bg)
3 Readers who have been observing my coding style will have noticed a definite pattern; I like to create objects from lists of tuples! This example is no exception:
    for port, lbl, tag, ypos in [ (1,'RX1','T3AccessRX', 0.30),
                                    (2,'TX1','T3AccessSTX', 0.40),
                                    (3,'RX2','T3AccessRX', 0.65),
                                    (4,'TX2','T3AccessRX', 0.75)]:
        Python’s ability to unpack a tuple contained in a list of tuples provides a mechanism to compress the amount of code required to achieve a desired effect.
4 The arguments unpacked from the tuple are substituted in setattr and getattr calls:
    setattr(self, 'bnc%d' % port, BNC(self.card_frame, fid=tag,port=port))
    getattr(self, 'bnc%d' % port).bnc_frame.place(relx=0.5, rely=ypos,anchor=CENTER))
    Label(self.card_frame,text=lbl, font=("verdana", 6), fg="white", bg=bg).place(relx=0.5,rely=(ypos+0.045),anchor=CENTER)
This style of coding results in tight code. It may be a little difficult to read initially, but it is still an efficient way of creating graphic elements in a loop.

As the last step to adding the T3 card, we must modify the loop that generates blank cards to add one of the T3 Access cards:

for i in range(9):
    if i == 4:
        card =T3AccessCard(self.rack, width=incr-1, height=414)
    else:
        card =CardBlank(self.rack, width=incr-1, height=414)
    card.card_frame.place(x=x, y=0, anchor=NW)
    x = x + incr