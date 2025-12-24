---
source_image: page_478.png
page_number: 478
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.71
tokens: 8312
characters: 2222
timestamp: 2025-12-24T00:45:03.110366
finish_reason: stop
---

Methods

Bitmap(option...)
Creates a bitmap instance using option-value pairs in option.

cget(option)
Returns the current value of the configuration option given by option. option may have any of the values accepted by the bitmap constructor.

configure(option=value...)
Queries or modifies the configuration options for the image. If no option is specified, returns a dictionary describing all of the available options for imageName. If option is specified with no value, then the command returns a dictionary describing the one named option (this dictionary will be identical to the corresponding sublist of the value returned if no option is specified). If one or more option-value pairs are specified, then the method modifies the given option(s) to have the given value(s); in this case the method returns an empty string. option may have any of the values accepted by the bitmap constructor.

height()
Returns an integer giving the height of the image in pixels.

type()
Returns the type of image as a string (the value of the type argument to image create when the image was created).

width()
Returns an integer giving the width of the image in pixels.

Button

Description
The button class defines a new window and a button widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the button such as its colors, font, text, and initial relief. The button method returns the identity of the new widget. At the time this method is invoked, the button’s parent must exist.

A button is a widget that displays a textual string, bitmap or image. If text is displayed, it must all be in a single font, but it can occupy multiple lines on the screen (if it contains new-lines or if wrapping occurs because of the wrapLength option) and one of the characters may optionally be underlined using the underline option. It can display itself in either of three different ways, according to the state option: it can be made to appear raised, sunken, or flat; and it can be made to flash. When a user invokes the button (by pressing mouse button 1 with the cursor over the button), then the activate callback specified in the command option is invoked.