---
source_image: page_359.png
page_number: 359
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.74
tokens: 8064
characters: 865
timestamp: 2025-12-24T00:41:13.359962
finish_reason: stop
---

Clearly, you could add more detail, timestamps and other data that may help you if you encounter problems when you start running your code. Planning for the need to debug is often easier at the time you write the code than when you have pressure to deliver.

15.4 A Tkinter explorer

In “Building an application” on page 18 I suggested a technique for hiding access to a debug window. This often works well, since you have immediate access to the tool, usually without restarting the application. I’m including an example here (the code is available online) which pops up if an error is output to stderr. Then you can look at the source, change variables in the namespace or even launch another copy of the application to check it out. Here are a series of screenshots:

![An embedded debug tool](https://i.imgur.com/3Q5z5QG.png)

Figure 15.4 An embedded debug tool