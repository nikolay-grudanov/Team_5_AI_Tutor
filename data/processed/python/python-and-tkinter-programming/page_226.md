---
source_image: page_226.png
page_number: 226
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.11
tokens: 8499
characters: 2948
timestamp: 2025-12-24T00:37:46.646472
finish_reason: stop
---

Each of the cards has LEDs, connectors and passive components such as buttons, card-pullers and locking screws. Sounds like a lot? It is not as difficult as it may seem, on first analysis, and once the basic components have been built, you will observe a great deal of code reuse.

9.2 Modularity

In section 7.2 on page 129 we started to develop a class library of components such as LEDs, switches and other devices. In this chapter we are going to use an expanded library of indicators, connectors and panel devices. We will also make use of the built-in status methods of the composite widgets, which was only briefly noted in the previous examples. We will also introduce the topic of navigation in the GUI, (see “Navigation” on page 300) since our front panel should provide the administrator access to functionality bound to each of the graphical elements on the panel. A good example of such a binding is to warp the user to the list of alarms associated with an LED on the display or a configuration screen to allow him to set operational parameters for a selected port.

If you look again at figure 9.1, it is possible to identify a number of graphical components that must be developed to build the front panel. Although the configuration of each of the cards has not been revealed at this point, there are some “future” requirements for components to be displayed on the card which drives the following list:

1  A chassis consisting of the rack-mount extensions and base front panel along with passive components such as mounting screws.
2  Card slots which may be populated with a variety of cards.
3  A number of cards consisting of LEDs, connectors and other active devices along with the card front to mount the devices and other passive components such as card pullers and labels.
4  Power supply modules containing connectors, switches and LEDs.
5  Passive components such as the air-intake screens and the logo.
6  LEDs, connectors (J-45*, BNC†, FDDI‡, J-25, J-50 and power) and power switches.

9.3 Implementing the front panel

Some preparation work needs to be done to convert the notional front panel to a working system. In particular, it is necessary to calculate the sizes of screen components based on some scaling factors, since the majority of panels are much larger than typical computer screens. As the reader will observe in the following example code, the author tends to work with relative positioning on a canvas. This is a somewhat more difficult approach to widget placement

* J connectors are typically used for serial connections. The number of pins available for connection is indicated by the suffix of the connector. Common connectors are J-9, J-25, and J-50.
† A Bayonet Neil-Concelman (BNC) connector is a type of connector used to connect using coaxial cable.
‡ FDDI connectors are used to connect fiber-optic lines and to normally connect a pair of cables, one for reception and one for transmission.