---
source_image: page_540.png
page_number: 540
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.18
tokens: 8521
characters: 2690
timestamp: 2025-12-24T00:47:16.895783
finish_reason: stop
---

put(data, to=None)
Sets pixels in the image to the colors specified in data. data is used to form a two-dimensional array of pixels that are then copied into the image. data is structured as a list of horizontal rows, from top to bottom, each of which is a list of colors, listed from left to right. Each color may be specified by name (e.g., blue) or in hexadecimal form (e.g., #2376af). The to option can be used to specify the bounding box to be affected. If the tuple contains only x1 and y1, the area affected has its top-left corner at (x1,y1) and is the same size as the array given in data. If all four coordinates are given, they specify diagonally opposite corners of the affected rectangle, and the array given in data will be replicated as necessary in the x and y directions to fill the rectangle.

subsample(x, y = None)
Reduces the image in size by using only every xth pixel in the x direction and yth pixel in the y direction. Negative values will cause the image to be flipped about the y or x axes, respectively. If y is not given, the default value is the same as x.

type()
Returns the type of image as a string (the value of the type argument to image create when the image was created).

width()
Returns an integer giving the width of the image in pixels.

write(filename, options...)
Writes image data from the image to a file named filename. The following options may be specified:

<table>
  <tr>
    <th>Option</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>format</td>
    <td>string</td>
    <td>Specifies the name of the image file format handler to be used to write the data to the file. Specifically, this subcommand searches for the first handler whose name matches an initial substring of format-name and which has the capability to write an image file. If this option is not given, this subcommand uses the first handler that has the capability to write an image file.</td>
  </tr>
  <tr>
    <td>from_coords</td>
    <td>tuple</td>
    <td>Specifies a rectangular region of imageName to be written to the image file. If only x1 and y1 are specified, the region extends from (x1,y1) to the bottom-right corner of the image. If all four coordinates are given, they specify diagonally opposite corners of the rectangular region. The default, if this option is not given, is the whole image.</td>
  </tr>
</table>

zoom(x, y = None)
Magnifies the image by a factor of x in the x direction and y in the y direction. If y is not given, the default value is the same as x. With this option, each pixel in the source image will be expanded into a block of x × y pixels in the new image, all the same color. x and y must be greater than 0.