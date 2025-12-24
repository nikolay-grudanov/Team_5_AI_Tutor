---
source_image: page_515.png
page_number: 515
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.78
tokens: 8480
characters: 2592
timestamp: 2025-12-24T00:46:26.856051
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
    <td>slant</td>
    <td>The amount the characters in the font are slanted away from the vertical. Valid values for slant are roman and italic. A roman font is the normal, upright appearance of a font, while an italic font is one that is tilted some number of degrees from upright. The closest available slant to the one specified will be chosen. The default slant is roman.</td>
    <td>constant</td>
    <td>ITALIC</td>
    <td>NORMAL</td>
  </tr>
  <tr>
    <td>underline</td>
    <td>The value is a boolean flag that specifies whether characters in this font should be underlined.</td>
    <td>Boolean</td>
    <td>TRUE 0</td>
    <td>FALSE</td>
  </tr>
  <tr>
    <td>weight</td>
    <td>The nominal thickness of the characters in the font. The value NORMAL specifies a normal weight font, while BOLD specifies a bold font. The closest available weight to the one specified will be chosen.</td>
    <td>constant</td>
    <td>BOLD</td>
    <td>NORMAL</td>
  </tr>
</table>

Methods

actual(option=None)
Returns information about the the actual attributes that are obtained when font is used on the window’s display; the actual attributes obtained may differ from the attributes requested due to platform-dependant limitations, such as the availability of font families and pointsizes. If option is omitted, returns all actual font attributes as a dictionary. If option is specified, returns the value of that attribute.

cget(option)
Queries the desired attribute, option, for the current font.

configure(**options)
Queries or modifies the desired attributes for the current font. If no option is specified, returns a dictionary describing all the options and their values for fontname. If a single option is specified with no value, then it returns the current value of that attribute. If one or more option-value pairs are specified, then the method modifies the given named font to have the given values; in this case, all widgets using that font will redisplay themselves using the new attributes for the font.

copy()
Returns a copy of the actual font.

measure(text)
Measures the amount of space the string text would use in the given font when displayed in the current font. The return value is the total width in pixels of text, not including the extra pixels used by highly exagerrated characters such as cursive “f.” If the string contains newlines or tabs, those characters are not expanded or treated specially when measuring the string.