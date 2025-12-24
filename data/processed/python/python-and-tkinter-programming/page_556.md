---
source_image: page_556.png
page_number: 556
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.32
tokens: 8458
characters: 2429
timestamp: 2025-12-24T00:47:41.727421
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
    <td>tabs</td>
    <td>Specifies a set of tab stops for the window. The option’s value consists of a list of screen distances giving the positions of the tab stops. Each position may optionally be followed in the next list element by one of the keywords LEFT, RIGHT, CENTER, or NUMERIC; these all specify how to justify text relative to the tab stop. LEFT is the default; it causes the text following the tab character to be positioned with its left edge at the tab position. RIGHT means that the right edge of the text following the tab character is positioned at the tab position, and CENTER means that the text is centered at the tab position. NUMERIC means that the decimal point in the text is positioned at the tab position; if there is no decimal point then the least significant digit of the number is positioned just to the left of the tab position; if there is no number in the text then the text is right-justified at the tab position. For example, tabs=(2c, left, 4c, 6c, center) creates three tab stops at two-centimeter intervals; the first two use left justification and the third uses center justification. If the list of tab stops does not have enough elements to cover all of the tabs in a text line, then Tk extrapolates new tab stops using the spacing and alignment from the last tab stop in the list. The value of the tabs option may be overridden by -tabs options in tags. If no -tabs option is specified, or if it is specified as an empty list, then Tk uses default tabs spaced every eight (average size) characters.</td>
    <td>string</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>wrap</td>
    <td>Specifies how to handle lines in the text that are too long to be displayed in a single line of the text’s window. The value must be NONE or CHAR or WORD. A wrap mode of None means that each line of text appears as exactly one line on the screen; extra characters that don’t fit on the screen are not displayed. In the other modes each line of text will be broken up into several screen lines if necessary to keep all the characters visible. In CHAR mode a screen line break may occur after any character; in WORD mode a line break will only be made at word boundaries.</td>
    <td>constant</td>
    <td>"char"</td>
    <td>char NONE</td>
  </tr>
</table>