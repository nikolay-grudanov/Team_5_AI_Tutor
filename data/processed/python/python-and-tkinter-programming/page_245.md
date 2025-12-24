---
source_image: page_245.png
page_number: 245
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.35
tokens: 8369
characters: 2404
timestamp: 2025-12-24T00:38:16.349110
finish_reason: stop
---

9.5 And now for a more complete example

The previous examples have illustrated the overall methods for developing GUI representation of panels and other devices. To further develop this theme we will look at a simple but quite useful example.

Many digital multimeters have serial interfaces which allow connection to a computer. I own a RadioShack 22-168A multimeter, which is shown in figure 9.10. The meter has 24 ranges that provide AC/DC voltage and current measurements, resistance, capacitance, frequency counting and other functions. The meter implements a simple serial protocol which allows the currently-displayed value to be polled. Using a simple encoding scheme the current range selection can be deduced.

Implementing a GUI to display the current state of the meter’s display is not particularly difficult. It is displaying the range that has been selected that introduces a challenge. One solution would be to display just the LCD panel at the top of the meter and then display the current range as text, either in the LCD or elsewhere. However this does not attempt to achieve photorealism and does not make for a particularly interesting example for you, the reader!

The solution we are going to implement is to animate the selector knob on the meter so that it reflects the actual appearance of the meter to the user. This requires quite a lot of work, but, as you will see later, it results in an attractive GUI.

These are the steps that we will go through to prepare a series of overlaid GIF images for the selector, as illustrated in figure 9.11:

1. Obtain the base image with the selector at one position.
2. Crop the selector as a rectangular selection.
3. Retouch the image to remove the pixels surrounding the selector.
4. Fill the background with a distinct color.
5. Rotate the image 15 degrees.
6. Crop the image to the same size as the original selection.
7. Save the image as a transparent GIF image, using the colormap entry corresponding to the surroundings of the selector as the transparent color (the last image in the series, figure 9.11(7), demonstrates the effect of displaying the overlaid image).

You have probably judged me as criminally insane to propose generating 24 rotated GIF images simply to show an accurate view of the actual multimeter. Perhaps you are right, but please reserve your final judgement until after you have seen the finished result!