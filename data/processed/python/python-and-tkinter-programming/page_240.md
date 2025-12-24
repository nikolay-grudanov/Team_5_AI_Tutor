---
source_image: page_240.png
page_number: 240
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.72
tokens: 8396
characters: 2341
timestamp: 2025-12-24T00:38:07.875324
finish_reason: stop
---

op = random.choice(range(0, len(ops)-1))

pstr = 'st_wid[%d].%s()' % (choice, ops[op])
self.cobj = compile(pstr, 'inline', 'exec')
self.rack.after(50, self.doit)

def doit(self):
    exec(self.cobj)
    self.rack.after(50, self.animate(None))

![Animated widgets](figure_9.7.png)

Figure 9.7 Animated widgets

If you run FrontPanel_3.py and click on the logo, you will activate the animation. Of course, it is difficult to depict the result of this in a black-and-white printed image, but you should be able to discern differences in the shading of the controls on the panels—especially the J45 connectors on the fourth panel from the left in figure 9.7.

Of course, there is quite a lot of work to turn a panel such as this into a functional system. You would probably use a periodic SNMP poll of the device to get the state of each of the components and set the LEDs appropriately. In addition, you might monitor the content of the card rack to detect changes in hardware, if the device supports “hot pull” cards. Finally, menus might be added to the ports to give access to configuration utilities.

9.4 GIF, BMP and overlays

The panels and machines introduced in the previous section used drawn interfaces. With a little effort, it is possible to produce a panel or machine that closely resembles the actual device. In some cases, it is necessary to have a little artistic flair to produce a satisfactory result, so an alternate approach must be used. Sometimes, it can be easier to use photographs of the device to produce a totally accurate representation of it; this is particularly true if the device is large. In this section I will provide you with a number of techniques to merge photographic images with GUIs.

Let’s begin by taking a look at the front panel of the Cabletron SmartSwitch 6500 shown in figure 9.8. If you contrast the magnified section in this figure with the components in figure 9.6, you may notice that the drawn panel shows clearer detail, particularly for text labels. However, if you consider the amount of effort required to develop code to precisely place the components on the panels, the photo image is much easier. In addition, the photo image reproduces every detail, no matter how small or complex, and it has strong three-dimensional features which are time-consuming to recreate with drawn panels.