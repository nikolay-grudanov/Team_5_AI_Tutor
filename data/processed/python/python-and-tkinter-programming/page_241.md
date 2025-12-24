---
source_image: page_241.png
page_number: 241
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.79
tokens: 8164
characters: 1241
timestamp: 2025-12-24T00:37:57.272970
finish_reason: stop
---

Figure 9.8 EC6110 Switch. The Highlighted area is magnified.
Photo courtesy Cabletron Systems

The task of creating modular panels is somewhat easier than creating similar panels with drawn components. Constructing a system with images requires the following steps:

1 Photograph the device with an empty card rack, if possible.
2 Photograph the device with cards inserted (singly, if possible) at the same scale.
3 Crop the card images so that they exactly define a card face.
4 Create a class for each card type, loading appropriate graphics and overlays for active components (LEDs, annunciators, etc.) and navigable components (connectors, buttons, etc.).
5 Create a chassis population based on configuration.
6 Write the rest of the supporting code.

In the following code, just a sample of the code will be presented. The full source code may be obtained online.

Components_4.py

class C6C110_CardBlank(GUICommon):
    def __init__(self, master=None, width=10, height=10,
                 appearance=FLAT, bd=0):
        self.card_frame=Frame(master, relief=appearance, height=height,
                              width=width, bd=bd, highlightthickness=0)

class C6C110_ENET(C6C110_CardBlank):
    def __init__(self, master, slot=0):