---
source_image: page_370.png
page_number: 370
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.04
tokens: 8343
characters: 2192
timestamp: 2025-12-24T00:41:46.470999
finish_reason: stop
---

The basic rules to be followed with color are these:

1 If you need to distinguish a graphic item, select color as the last method.
2 Use color to draw the user to the most important features on the screen.
3 Remember that your user might be color blind* and might not perceive color contrast in the same way as you do.
4 Create optimal contrast between your graphic components. You should avoid 100% contrast in most cases.†
5 Avoid reverse video (light on dark) except where you must draw attention to a graphic component. A good example of reverse video is to indicate a validation error in an input field.

As an illustration of how color selection can become a problem, take a look at figure 16.11. Although it is not possible to see the direct effect of color on the page, the color scheme chosen is quite pleasing, in warm tones of brown, olive green and cream. However, an application with GUIs implemented with these colors would prove tiring in practice, though it might look good for a short demonstration. The major problem is the use of low-contrast reverse video in the entry fields. Incidentally, the colors used in this application were adapted from a commercial application; I’m sure the designer was proud of the result that had been produced.

![Figure 16.11 Problems with color combinations](./images/figure_16_11.png)

Figure 16.11 Problems with color combinations

* It is relatively easy to design color use to accommodate individuals with color-blindness. Do not use primary colors; mix each color with varying amounts of red, green, and blue so that the overall chrominance varies. The overall effect will not appear greatly different for individuals with normal color vision, but it will appear distinct for those with color blindness. If you have an application which is in a mission critical environment and might be used by individuals with color blindness, it may be prudent to have your GUI checked out by someone with less-than-perfect vision.

† Not all monitors display black on white as clearly as they display black on grey (or some other light color combination). Try black on 90% gray, for example. (Note that 90% gray is really 90% white and 10% black).