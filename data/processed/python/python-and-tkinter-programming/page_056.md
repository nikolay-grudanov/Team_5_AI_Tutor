---
source_image: page_056.png
page_number: 56
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.42
tokens: 8135
characters: 1203
timestamp: 2025-12-24T00:32:40.029936
finish_reason: stop
---

CHAPTER 4

Tkinter widgets

4.1 Tkinter widget tour 31
4.2 Fonts and colors 47
4.3 Pmw Megawidget tour 49
4.4 Creating new megawidgets 73

In this chapter I’ll present the widgets and facilities available to Tkinter. Pmw Python Mega-Widgets, will also be discussed, since they provide valuable extensions to Tkinter. Each Tkinter and Pmw widget will be shown along with the source code fragment that produces the display. The examples are short and simple, although some of them illustrate how easy it is to produce powerful graphics with minimal code.

This chapter will not attempt to document all of the options available to a Tkinter programmer; complete documentation for the options and methods available for each widget is presented in appendix B. Similarly, Pmw options and methods are documented in Appendix C. Uses these appendices to determine the full range of options for each widget.

4.1 Tkinter widget tour

The following widget displays show typical Tkinter widget appearance and usage. The code is kept quite short, and it illustrates just a few of the options available for the widgets. Sometimes one or more of a widget’s methods will be used, but this only scratches the surface. If