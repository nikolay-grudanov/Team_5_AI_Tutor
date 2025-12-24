---
source_image: page_102.png
page_number: 102
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.31
tokens: 8146
characters: 1266
timestamp: 2025-12-24T00:34:04.504044
finish_reason: stop
---

CHAPTER 5

Screen layout

5.1 Introduction to layout 77
5.2 Packer 79
5.3 Grid 86
5.4 Placer 90
5.5 Summary 94

GUI layout is an often-misunderstood area; a programmer could conceivably waste a lot of time on it. In this chapter, the three geometry managers, Pack, Grid and Place are covered in detail. Some advanced topics, including approaches to variable-size windows and the attendant problems of maintaining visually attractive and effective interfaces, will be presented.

5.1 Introduction to layout

Geometry managers are responsible for controlling the size and position of widgets on the screen. In Motif, widget placement is handled by one of several manager widgets. One example is the Constraint Widget class which includes the XmForm widget. Here, layout is controlled by attaching the widget by one, or more, of the top, bottom, left or right sides to adjacent widgets and containers. By choosing the appropriate combinations of attachments, the programmer can control a number of behaviors which determine how the widget will appear when the window is grown or shrunk.

Tk provides a flexible approach to laying out widgets on a screen. X defines several manager class widgets but in Tk, three geometry managers may be used. In fact, it is possible to