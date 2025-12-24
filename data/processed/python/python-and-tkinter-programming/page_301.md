---
source_image: page_301.png
page_number: 301
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.76
tokens: 8101
characters: 937
timestamp: 2025-12-24T00:39:42.955739
finish_reason: stop
---

CHAPTER 11

Graphs and charts

11.1 Simple graphs    276
11.2 A graph widget   279
11.3 3-D graphs       292
11.4 Strip charts     296
11.5 Summary          298

There was a time when the term graphics included graphs; this chapter reintroduces this meaning. Although graphs, histograms and pie charts may not be appropriate for all applications, they do provide a useful means of conveying a large amount of information to the viewer. Examples will include linegraphs, histograms, and pie charts to support classical graphical formats. More complex graph examples will include threshold alarms and indicators.

11.1 Simple graphs

Let’s start by constructing a very simple graph, without trying to make a graph class or adding too many features, so we can see how easy it can be to add a graph to an application. We’ll add more functionality later.

simpleplot.py

from Tkinter import *
root = Tk()
root.title('Simple Plot - Version 1')