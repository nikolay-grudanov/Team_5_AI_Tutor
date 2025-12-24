---
source_image: page_103.png
page_number: 103
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.02
tokens: 8606
characters: 3684
timestamp: 2025-12-24T00:34:33.310224
finish_reason: stop
---

use the managers with each other (although there are some rather important rules about how one goes about this). Tk achieves this flexibility by exploiting the X behavior that says widget geometry is determined by the geometry managers and *not* by the widgets themselves. Like X, if you do not manage the widget, it will not be drawn on the screen, although it will exist in memory.

Geometry managers available to Tkinter are these: the Packer, which is the most commonly used manager; the Grid, which is a fairly recent addition to Tk; the Placer, which has the least popularity, but provides the greatest level of control in placing widgets. You will see examples of all three geometry managers throughout the book. The geometry managers are available on all architectures supported by Tkinter, so it is not necessary to know anything about the implementation of the architecture-dependent toolkits.

**5.1.1 Geometry management**

Geometry management is a quite complex topic, because a lot of negotiation goes on between widgets, their containers, windows and the supporting window manager. The aim is to lay out one or more *slave* widgets as subordinates of a *master* widget (some programmers prefer to refer to *child* widgets and *parents*). *Master* widgets are usually containers such as a Frame or a Canvas, but most widgets can act as masters. For example, place a button at the bottom of a frame. As well as simply locating slaves within masters, we want to control the behavior of the widget as more widgets are added or when the window is shrunk or grown.

The negotiation process begins with each slave widget requesting width and height adequate to display its contents. This depends on a number of factors. A button, for example, calculates its required size from the length of text displayed as the label and the selected font size and weight.

Next, the master widget, along with its geometry manager, determines the space available to satisfy the requested dimensions of the slaves. The available space may be more or less than the requested space, resulting in squeezing, stretching or overlapping of the widgets, depending on which geometry manager is being employed.

Next, depending on the design of the window, space within a master’s *master* must be apportioned between all *peer* containers. The results depend on the geometry manager of the peer widgets.

Finally, there is negotiation between the toplevel widget (normally the toplevel shell) and the window manager. At the end of negotiations the available dimensions are used to determine the final size and location in which to draw the widgets. In some cases there may not be enough space to display all of the widgets and they may not be realized at all. Even after this negotiation has completed when a window is initialized, it starts again if any of the widgets change configuration (for example, if the text on a button changes) or if the user resizes the window. Fortunately, it is a lot easier to use the geometry managers than it is to discuss them!

A number of common schemes may be applied when a screen is designed. One of the properties of the Packer and to a lesser extent the Grid, is that it is possible to allow the geometry manager to determine the final size of a window. This is useful when a window is created dynamically and it is difficult to predict the population of widgets. Using this approach, the window changes size as widgets are added or removed from the display. Alternatively, the designer might use the Placer on a fixed-size window. It really depends on the effect that is wanted.

Let’s start by looking at the Packer, which is the most commonly used manager.