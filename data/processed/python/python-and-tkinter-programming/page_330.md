---
source_image: page_330.png
page_number: 330
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.26
tokens: 8088
characters: 1055
timestamp: 2025-12-24T00:40:26.858568
finish_reason: stop
---

12.5 Image maps

In “Image maps” on page 191, we looked at an implementation of image maps. It used pointer clicks to detect regions on the image and to select mapped areas. This technique cannot support mouseless operation, so if this is necessary, you have some work to do.

One solution is to overlay the image with objects that can take focus, then you can tab from object to object. This does work (the application shown on page 232 uses this technique to place buttons over button images on a ray-traced image), but it does require much more planning and code.

12.6 Summary

This chapter is another illustration of the fact that an application developer should consider its end-users carefully. If you are developing an application for a single group of users on uniform hardware platforms, then it may not be necessary to think about providing alternate means for navigating the GUIs. However, if you have no control of the end-user’s environment you can change their perception of your application greatly by allowing alternate navigation models.