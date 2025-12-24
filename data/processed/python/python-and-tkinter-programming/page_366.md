---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.08
tokens: 8124
characters: 1169
timestamp: 2025-12-24T00:41:28.019024
finish_reason: stop
---

Figure 16.4  ComboBox widget

Figure 16.5 shows our example with the fields split into appropriate subfields.
Unfortunately, this change has now cluttered our interface and the composition is now rather confusing to the end user. We have to make a further adjustment to separate the logical field groups and to help the user to navigate the interface. In figure 16.6, we introduce whitespace between the three groups.

Figure 16.5  Splitting fields into sub-fields

This achieves the desired effect, but we can improve the effect further by drawing a graphic around each of the logical groups. This can be achieved in a number of ways:

1  Use available 3-D graphic relief options with containers. Tkinter frames allow sunken, raised, groove and ridge, for example.
2  Draw a frame around the group. This is commonly seen in Motif GUIs, usually with an accompanying label in the frame.
3  Arrange for the background color of the exterior of the frame to be displayed in a different color from the inside of the frame. Note that this kind of differentiation is suitable for only a limited range of interface types.

Figure 16.6  Separating logical groups with whitespace