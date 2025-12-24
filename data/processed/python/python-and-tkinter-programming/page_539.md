---
source_image: page_539.png
page_number: 539
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.85
tokens: 8389
characters: 2289
timestamp: 2025-12-24T00:47:07.122030
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>palette</td>
    <td>Specifies the resolution of the color cube to be allocated for displaying this image, and thus the number of colors used from the colormaps of the windows where it is displayed. The palette-spec string may be either a single decimal number, specifying the number of shades of gray to use, or three decimal numbers separated by slashes (/), specifying the number of shades of red, green and blue to use, respectively. If the first form (a single number) is used, the image will be displayed in monochrome (i.e., grayscale).</td>
    <td>integer or string</td>
    <td>'255/220/125'</td>
    <td>system dependent</td>
  </tr>
</table>

Methods

PhotoImage(option...)
Creates a photo instance using option-value pairs in option.

blank()
Blank the image; that is, set the entire image to have no data, so it will be displayed as transparent, and the background of whatever window it is displayed in will show through.

cget(option)
Returns the current value of the configuration option given by option. option may have any of the values accepted by the photoimage constructor.

configure(option=value...)
Queries or modifies the configuration options for the image. If no option is specified, returns a dictionary describing all of the available options for the image. If option is specified with no value, then the command returns a dictionary describing the one named option (this dictionary will be identical to the corresponding sublist of the value returned if no option is specified). If one or more option-value pairs are specified, then the method modifies the given option(s) to have the given value(s); in this case the method returns an empty string. option may have any of the values accepted by the photoimage constructor.

copy()
Copies the current image. Note the Tkinter method simplifies the Tk command which allows copying of a region within the image.

get(x, y)
Returns the color of the pixel at coordinates (x,y) in the image as a tuple of three integers between 0 and 255, representing the red, green and blue components respectively.

height()
Returns an integer giving the height of the image in pixels.