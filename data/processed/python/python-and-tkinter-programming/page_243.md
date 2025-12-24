---
source_image: page_243.png
page_number: 243
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.99
tokens: 8438
characters: 2206
timestamp: 2025-12-24T00:38:16.542762
finish_reason: stop
---

Code comments

1 Most of the code resembles that for drawn panel components. The code is a little shorter, since it is not necessary to build as many components.

self.img = PhotoImage(file='images/6c110_enet.gif')
setattr(glb, 'img%d % slot', self.img)
self.width = self.img.width()
self.height = self.img.height()

In the __init__ method, we create a PhotoImage instance. It is important that this reference remains within scope. If the image gets garbage-collected, you’ll see an empty background field where you had hoped to have an image. The size of the image is obtained (in pixels) in order to construct the panels.

2 As might be expected, we build a list of tuples to contain the calculated positions of the LEDs.

xypos = [(10,180), (10,187),
...]

3 All borders, highlights, and selectionborders must be zero-width to ensure that the panels can be butted together.

self.canvas = Canvas(self.card_frame, width=self.width,
    bd=0, highlightthickness=0,
    height=self.height, selectborderwidth=0)

4 The image is created on the base canvas using the stored PhotoImage.

self.canvas.create_image(0,0,anchor=NW,
    image=eval('glb.img%d' % slot))

5 The J45 connectors are drawn over the connectors depicted in the image; this adds navigation and status properties to the otherwise passive devices.

for i, y in [(0, 0.330), (1, 0.619)]:
    setattr(self, 'j%d' % i, Enet10baseT(self.card_frame,
        fid="10Base-T-%d" % i, port=i, orient=HW_LEFT,
        status=STATUS_OFF, xwidth=15, xheight=12))
    getattr(self, 'j%d' % i).j45_frame.place(relx=0.52,
        rely=y, anchor=CENTER)

The size of the connector is passed in the constructor; this adds functionality to the J45 connectors shown earlier in the chapter.

6 The LEDs are drawn on the canvas at their designated location. Note that these use the CLED class, not the LED class, because these LEDs are drawn directly on the canvas and not within a Frame. If the LED class had been used, we would have experienced problems in attempting to fill the rectangular frame associated with the widget and the background color.

for i in range(len(xypos)):
    xpos,ypos = xypos[i]
    setattr(self, 'led%d' % (i+1), CLED(self.card_frame,