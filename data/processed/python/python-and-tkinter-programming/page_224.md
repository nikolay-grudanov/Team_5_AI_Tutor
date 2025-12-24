---
source_image: page_224.png
page_number: 224
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.44
tokens: 8163
characters: 1311
timestamp: 2025-12-24T00:37:27.341694
finish_reason: stop
---

CHAPTER 9

Panels and machines

9.1 Building a front panel 199
9.2 Modularity 201
9.3 Implementing the front panel 201
9.4 GIF, BMP and overlays 215
9.5 And now for a more complete example 220
9.6 Virtual machines using POV-Ray 232
9.7 Summary 236

This chapter is where Tkinter gets to be FUN! (Maybe I should find a hobby!) Network management applications have set a standard for graphical formats; many hardware device manufacturers supply a software front-panel display showing the current state of LEDs, connectors and power supply voltages—anything that has a measurable value. In general, such devices are SNMP-capable, although other systems exist. This model may be extended to subjects which have no mechanical form—even database applications can have attractive interfaces. The examples presented in this chapter should be useful for an application developer needing a framework for alternative user interfaces.

9.1 Building a front panel

Let’s construct a hypothetical piece of equipment. The task is to present a front-panel display of a switching system (perhaps an ATM switch or a router) to an administrator. The display will show the current state of the interfaces, line cards, processors and other components. For the purposes of the example, we shall assume that the device is SNMP-capable