---
source_image: page_377.png
page_number: 377
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.39
tokens: 8498
characters: 3045
timestamp: 2025-12-24T00:42:08.912140
finish_reason: stop
---

Avoid ripple in your applications if at all possible (ripple was introduced on page 154). Badly-designed interdependence between fields can consume a lot of system resources and the user will find it has limited value.

17.2.4 Fast initialization

It is important that your screens are drawn as quickly as possible. Users often judge an application by its response times; in some cases, flawless applications are viewed as buggy if the users experience long delays with no apparent progress after they have selected an operation. In some of the examples, I’ve included comments about delaying the packing of Frame widgets until the widgets contained within them have been completed. The purpose of doing this is to prevent the negotiation, which is inherent in the way that the geometry managers operate, from happening on-screen every time a new widget is added. If you delay the negotiation until all widgets have been created, you will see much better performance at startup

17.2.5 Throttling events

Window systems generate a lot of events for certain types of actions. Two such actions are moving the mouse and holding down the SHIFT key (if your system is configured to auto-repeat held keys). Try running Example_6_2.py and try those actions—you may be surprised at the rate at which the events are generated. If all you are interested in is the x/y location of the mouse and little computation is being triggered, then it is not a problem. However, if each event triggers redrawing a complex object, then you may have a performance problem.

You can do a number of things to handle a high rate of arrivals:

1 Throttle the events so that the code responds to fewer occurrences; this may be done using a timer so that updates are performed every few hundred milliseconds, for example. Alternatively, you may use a counter, so that every ten events are processed, as an example. The latter method is more difficult to implement and it usually requires a combination of a timer and a counter.

2 Reduce the drawing overhead. If the events are the result of a mouse drag, for example, you may be able to simplify what is drawn until the mouse is released. As an example, draw an outline or ghost of the object while the drag is in progress.

3 Suppress unrelated events. For example, dragging an object may cause a number of events to be generated as you cross other objects. Unless they are related to the drag, they might as well be ignored.

17.3 Python techniques

One or two techniques have already been suggested in “Everyday speedups” on page 348. In this section, we’ll look at some Python-specific coding methods that usually result in more efficient code. However, before you go into every application that you’ve written already, be aware that you should not make changes unless there are grounds to do so. If you don’t see a problem, don’t correct it! See “Application profiling” on page 357 to learn how you can identify bottlenecks in your applications. If this technique identifies places to improve your code, then go ahead.