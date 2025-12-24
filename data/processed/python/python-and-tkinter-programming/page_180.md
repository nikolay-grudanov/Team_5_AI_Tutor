---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.16
tokens: 8076
characters: 1068
timestamp: 2025-12-24T00:36:09.621598
finish_reason: stop
---

8.2 A standard application framework

One of the problems with designing forms is that some features are common to most applications. What we need is a standard application framework which can be adapted to each application; this should result in moderate code reuse. Many applications fit the general form shown in figure 8.7. In addition, we need the ability to provide busy cursors *, attach balloon help and help messages to fields, supply an about... message and add buttons with appropriate callbacks. To support these needs, I’ll introduce AppShell.py, which is a fairly versatile application framework capable of supporting a wide range of interface needs. Naturally, this framework cannot be applied to all cases, but it can go a long way to ease the burden of developing effective interfaces.

* A busy cursor is normally displayed whenever an operation takes more than a few hundred milliseconds, it is often displayed as a watch or hourglass. In some cases the application may also inhibit button-presses and other events until the operation has completed.