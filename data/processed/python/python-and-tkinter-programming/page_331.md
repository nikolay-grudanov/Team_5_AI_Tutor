---
source_image: page_331.png
page_number: 331
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.23
tokens: 8150
characters: 1176
timestamp: 2025-12-24T00:40:33.248098
finish_reason: stop
---

CHAPTER 13

The window manager

13.1 What is a window manager? 306
13.2 Geometry methods 307
13.3 Visibility methods 308
13.4 Icon methods 309
13.5 Protocol methods 309
13.6 Miscellaneous wm methods 310

Even though it is possible to build applications that have no direct communication with the window manager, it is useful to have an understanding of the role that the window manager (wm) has in X Window, Win32 and MacOS environments. This chapter covers some of the available wm facilities and presents examples of their use.

13.1 What is a window manager?

If you already know the answer to that question, you may want to skip ahead. It is perfectly possible to develop complex GUI-based applications without knowing anything about the window manager. However, many of the attributes of the displayed GUI are determined by the window manager.

Window managers exist in one form or another for each of the operating systems; examples are mwm (Motif), dtwm (CDE) and ovwm (OpenView). In the case of Win32, the window manager is just part of the operating system rather than being a separate application. The main functions that window managers typically support are these: