---
source_image: page_538.png
page_number: 538
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.11
tokens: 8502
characters: 2271
timestamp: 2025-12-24T00:47:09.112272
finish_reason: stop
---

Image data for a photo image can be obtained from a file or a string, or it can be supplied from C code through a procedural interface. At present, only GIF and PPM/PGM formats are supported, but an interface exists to allow additional image file formats to be added easily. A photo image is transparent in regions where no image data has been supplied.

Inheritance

Inherits from Image.

Shared options

<table>
  <tr>
    <th>Option</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>width</td>
    <td>requested width</td>
  </tr>
  <tr>
    <td>height</td>
    <td>requested height</td>
  </tr>
</table>

Options specific to PhotoImage

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>data</td>
    <td>Specifies the contents of the image as a string. The format of the string must be one of those for which there is an image file format handler that will accept string data (currently GIF). If both the data and file options are specified, the file option takes precedence.</td>
    <td>string</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>file</td>
    <td>filename gives the name of a file that is to be read to supply data for the photo image. The file format must be one of those for which there is an image file format handler that can read data (currently GIF, PGM and PPM).</td>
    <td>string</td>
    <td>"icon.gif"</td>
    <td></td>
  </tr>
  <tr>
    <td>format</td>
    <td>Specifies the name of the file format for the data specified with the data or file option.</td>
    <td>string</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>gamma</td>
    <td>Specifies that the colors allocated for displaying this image in a window should be corrected for a non-linear display with the specified gamma exponent value. (The intensity produced by most CRT displays is a power function of the input value, to a good approximation; gamma is the exponent and is typically around 2). The value specified must be greater than zero. The default value is 1 (no correction). In general, values greater than 1 will make the image lighter, and values less than 1 will make it darker.</td>
    <td>float</td>
    <td>1.2</td>
    <td>1.0</td>
  </tr>
</table>