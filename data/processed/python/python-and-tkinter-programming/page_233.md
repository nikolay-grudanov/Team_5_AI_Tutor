---
source_image: page_233.png
page_number: 233
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.15
tokens: 8243
characters: 1783
timestamp: 2025-12-24T00:37:43.934212
finish_reason: stop
---

Code comments

1 If you examine the __init__ method for each of the frames in the various classes in Components_1.py, you will notice that there are no geometry-management calls. It would have been possible to pass the location to place the object or simply pack the object within the constructor, but the style of coding used here allows the user to have more control over widget geometry. This is especially true for the chassis frame; this widget was explicitly forgotten so that the screen updates are made before the chassis is realized. This improves performance considerably when a large number of graphic objects need to be drawn.

    self.chassis.outer.pack(expand=0)

Here, the chassis frame is packed, realizing the widget and drawing the contained widgets. It does make a difference!

When FrontPanel.py is run, the screen shown in figure 9.3 is displayed. This display draws remarkably fast, even though we have to construct each of the air-screen holes individually. For highly computational or memory-intensive graphics which depict purely passive components, it is probably better to use GIF or bitmap images. Some aspects of this are discussed in “GIF, BMP and overlays” on page 215. Notice how we use the intrinsic three-dimensional properties of the widgets to create some depth in the display. In general, it is best to avoid trying to totally mimic the actual device and produce some level of abstraction.

Let’s create one of the cards that will populate the chassis. The T3 Access card has four BNC connectors (two pairs of Rx/Tx connectors), four LEDs for each pair of BNC connectors, and some identifying labels. Every card in the chassis has a power (PWR) and fault (FLT) LED.

![Basic router chassis](../images/fig9-3.png)

Figure 9.3 Basic router chassis