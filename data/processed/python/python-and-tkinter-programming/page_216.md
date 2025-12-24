---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.22
tokens: 8099
characters: 1054
timestamp: 2025-12-24T00:37:14.654858
finish_reason: stop
---

Figure 8.13 An installation wizard

8.7 Image maps

The final topic in this chapter presents an input technique which is typically used with web pages; image maps associate actions with clickable areas on an image. You could argue that this topic belongs in “Panels and machines” on page 199, but I am including it here since it is a viable method for getting input from the user.

If you take a look at “Building an application” on page 18 again, you will remember how a simple calculator was constructed using button widgets to bind user input to calculator functions. The application could be reworked using an image map; the major motivation for this would be to increase the realism of the interface by presenting an image of the calculator rather than a drawing.

One of the problems of creating image maps is that without a tool to define the targets for the map, it can be a time-consuming task to measure and input all of the coordinates. Take a look at figure 8.14. The area around each of the buttons (the targets for this case) have been out-