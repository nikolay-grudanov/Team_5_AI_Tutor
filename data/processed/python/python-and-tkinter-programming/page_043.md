---
source_image: page_043.png
page_number: 43
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.09
tokens: 8147
characters: 1280
timestamp: 2025-12-24T00:32:17.436238
finish_reason: stop
---

CHAPTER 3

Building an application

3.1 Calculator example: key features 21
3.2 Calculator example: source code 21
3.3 Examining the application structure 27
3.4 Extending the application 28

Most books on programming languages have followed Kernigan and Ritchie’s example and have presented the obligatory “Hello World” example to illustrate the ease with which that language may be applied. Books with a GUI component seem to continue this tradition and present a “Hello GUI World” or something similar. Indeed, the three-line example presented on page 13 is in that class of examples.

There is a growing trend to present a calculator example in recent publications. In this book I am going to start by presenting a simple calculator (you may add the word obligatory, if you wish) in the style of its predecessors. The example has been written to illustrate several Python and Tkinter features and to demonstrate the compact nature of Python code.

The example is not complete because it accepts only mouse input; in a full example, we would expect keyboard input as well. However, it does work and it demonstrates that you do not need a lot of code to get a Tkinter screen up and running. Let’s take a look at the code that supports the screen:

Figure 3.1 A simple calculator