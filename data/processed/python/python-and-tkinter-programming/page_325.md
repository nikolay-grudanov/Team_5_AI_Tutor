---
source_image: page_325.png
page_number: 325
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.06
tokens: 8131
characters: 1156
timestamp: 2025-12-24T00:40:17.225494
finish_reason: stop
---

CHAPTER 12

Navigation

12.1 Introduction: navigation models 300
12.2 Mouse navigation 301
12.3 Keyboard navigation: “mouseless navigation” 301
12.4 Building navigation into an application 302
12.5 Image maps 305
12.6 Summary 305

All successful GUIs provide a consistent and convenient means of navigation between their graphical elements. This short chapter covers each of these methods in detail. Some advanced navigation methods will be discussed to provide a guide to the topic. From the methods presented, you should be able to identify appropriate patterns for your application and apply the methods.

12.1 Introduction: navigation models

This chapter is all about focus. Specifically, keyboard focus, which is at the widget level and determines where keyboard events are delivered. Window focus is strictly a feature of the window manager, which is covered in more detail in “The window manager” on page 306.
There are normally two focus models:

Pointer When a widget contains the pointer, all keyboard events are directed to the widget.
Explicit The user must click on the widget to tab from widget to widget to set focus on a particular widget.