---
source_image: page_371.png
page_number: 371
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.59
tokens: 8356
characters: 2344
timestamp: 2025-12-24T00:41:52.173886
finish_reason: stop
---

16.2.3 Size considerations

Apart from the need to ensure that a GUI works at different screen resolutions, consideration must be made to determine whether the user is permitted to change the size of the displayed GUI. Having designed a well-proportioned screen, it can be difficult to allow the user to change the size of the display at will. In many cases it is better to disallow resizing of the screen rather than attempting to maintain an effective GUI regardless of what the user requests (see “Geometry methods” on page 307 for details about how to do this).

In the examples presented earlier in this chapter, resizing was handled by assigning one field on each line to stretch if the window was made larger. This is generally appropriate, but it may result in strange screen appearances. Shrinking a window is much harder to handle and may be impossible.

If the screen does not contain scrolled widgets (text, lists, etc.), it is probably better to fix the size of the window and maintain optimal layout.

16.3 Alternative graphical user interfaces

The elements of GUI design described above are appropriate for most applications, but a specific application might need to break the rules to achieve a desired effect. Let me present a case study. I was contracted to develop a crew-scheduling system for an airline’s pilots. Most of the airline’s administrators are, or have been pilots, so I wanted to design an interface that would have impact for such individuals. Figure 16.12 illustrates one of the screens that was delivered. This interface breaks many of the rules that have been presented above, but it was highly acclaimed by the airline. For readers who have not sat in the cockpit of an airplane, the interface is made to resemble a communication stack (radios) in an airplane. In this interface, the main displays utilize reverse video and a pixel font which is not uncommon in systems of this type. The panel is ray-traced to provide an extreme 3-D appearance (this technique was covered in “Virtual machines using POV-Ray” on page 232). Although it’s not apparent in the black-and-white illustration, the interface contains many colored elements. Again, this is consistent with the systems that are being mimicked.

![An interface for targeted users](../images/fig16_12.png)

Figure 16.12 An interface for targeted users