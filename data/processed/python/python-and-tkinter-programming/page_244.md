---
source_image: page_244.png
page_number: 244
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.19
tokens: 8259
characters: 1520
timestamp: 2025-12-24T00:38:05.725825
finish_reason: stop
---

self.canvas, shape=ROUND, width=4, status=STATUS_ON, relx=xpos, rely=ypos))

Note also that we pass both the enclosing card_frame and the canvas to the constructor. This facilitates accessing the after method of the Widget base class to implement flashing.

7 Finally, we populate the card rack. For the purpose of illustration, two of the FDDI cards have been replaced with Ethernet cards. Although this does not make much sense for this ATM switch, it demonstrates the ease with which the cards may be arranged.

    x = 0.0
    for i in range(12):
        if i in [0,1,2,3,4,5]:
            card = C6C110_FDDI(self.rack, slot=i)
        elif i in [6,7,8,9]:
            card = C6C110_ENET(self.rack, slot=i)
        else:
            card = C6C110_PSU(self.rack, slot=i)
        card.card_frame.place(x=x, y=0, anchor=NW)
        x = x + card.width

Note that the actual card width is used to determine the placement of the next card, and not a calculated increment, as in the earlier example.

Running EC6110.py displays the screen shown at the right of figure 9.9. The screen at the left of this figure illustrates the unpopulated rack. As in the earlier example, provision has been made to animate the components. Clicking anywhere on the enclosing chassis activates the animated display; this is not presented here and is left for you to try.

![Cardrack implemented with GIF panels and overlaid components](https://i.imgur.com/3Q5z5QG.png)

Figure 9.9 Cardrack implemented with GIF panels and overlaid components