---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.66
tokens: 8144
characters: 1167
timestamp: 2025-12-24T00:34:29.557269
finish_reason: stop
---

CHAPTER 6

Events, bindings and callbacks

6.1 Event-driven systems: a review 95
6.2 Tkinter events 98
6.3 Callbacks 102
6.4 Lambda expressions 103
6.5 Binding events and callbacks 104
6.6 Timers and background procedures 107
6.7 Dynamic callback handlers 107
6.8 Putting events to work 108
6.9 Summary 119

GUI applications rely heavily on events and binding callbacks to these events in order to attach functionality to widgets. I anticipate that many readers may have some familiarity with this topic. However, this may be a new area for some of you, so I will go into some detail to make sure that the subject has been fully covered. Advanced topics will be discussed, including dynamic callback handlers, data verification techniques and “smart” widgets.

6.1 Event-driven systems: a review

It quite possible to build complex GUI applications without knowing anything about the underlying event-mechanism, regardless of whether the application is running in a UNIX, Windows or Macintosh environment. However, it is usually easier to develop an application that behaves the way you want it to if you know how to request and handle events within your application.