---
source_image: page_514.png
page_number: 514
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.77
tokens: 8485
characters: 2319
timestamp: 2025-12-24T00:46:19.806364
finish_reason: stop
---

PAGES then the view adjusts by number screenfuls. If number is negative then characters farther to the left become visible; if it is positive then characters farther to the right become visible.

Font class

Inheritance
    Inherits from None.

Description
    The Font class provides several facilities for dealing with fonts, such as defining named fonts and inspecting the actual attributes of a font. The class defines several methods.

Shared options
    None.

Options specific to Font

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>family</td>
    <td>The case-insensitive font family name. Tk guarantees to support the font families named Courier (a monospaced “typewriter” font), Times (a serifed “newspaper” font), and Helvetica (a sans-serif “European” font). The most closely matching native font family will automatically be substituted when one of the above font families is used. The name may also be the name of a native, platform-specific font family; in that case it will work as desired on one platform but may not display correctly on other platforms. If the family is unspecified or unrecognized, a platform-specific default font will be chosen.</td>
    <td>string</td>
    <td>'Times'</td>
    <td>'MS'</td>
  </tr>
  <tr>
    <td>font</td>
    <td>Font specifier in X-font format or as a (family, size, style) tuple.</td>
    <td>font</td>
    <td>'MS'</td>
    <td>(('MS', 'Sans', 'Serif'), '8')</td>
  </tr>
  <tr>
    <td>overstrike</td>
    <td>The value is a boolean flag that specifies whether a horizontal line should be drawn through the middle of characters in this font. The default value for overstrike is false.</td>
    <td>Boolean</td>
    <td>1</td>
    <td>FALSE</td>
    <td>FALSE</td>
  </tr>
  <tr>
    <td>size</td>
    <td>The desired size of the font. If the size argument is a positive number, it is interpreted as a size in points. If size is a negative number, its absolute value is interpreted as a size in pixels. If a font cannot be displayed at the specified size, a nearby size will be chosen. If size is unspecified or zero, a platform-dependent default size will be chosen.</td>
    <td>integer</td>
    <td>12, -16</td>
    <td></td>
    <td></td>
  </tr>
</table>