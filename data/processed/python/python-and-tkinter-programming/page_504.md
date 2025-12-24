---
source_image: page_504.png
page_number: 504
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.64
tokens: 8572
characters: 2365
timestamp: 2025-12-24T00:46:11.601794
finish_reason: stop
---

Inheritance
Inherits from Widget, Canvas.

Shared options

<table>
  <tr>
    <th>Option</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>anchor</td>
    <td>CENTER</td>
  </tr>
  <tr>
    <td>fill</td>
    <td>transparent</td>
  </tr>
  <tr>
    <td>width</td>
    <td>1</td>
  </tr>
</table>

Options specific to Text

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>font</td>
    <td>Specifies the font to use for the text item. FontName may be any string acceptable to Tkinter. If this option isn’t specified, it defaults to a system-dependent font.</td>
    <td>font</td>
    <td>'Verdana'</td>
    <td>(('MS', 'Sans', 'Serif'), '8')</td>
  </tr>
  <tr>
    <td>justify</td>
    <td>Specifies how to justify the text within its bounding region. Must be one of the values LEFT, RIGHT, or CENTER. This option will only matter if the text is displayed as multiple lines.</td>
    <td>constant</td>
    <td>RIGHT</td>
    <td>LEFT</td>
  </tr>
  <tr>
    <td>stipple</td>
    <td>Indicates that the text should be filled in a stipple pattern; bitmap specifies the stipple pattern to use. If the fill option hasn’t been specified then this option has no effect. If bitmap is an empty string (the default), then filling is done in a solid fashion.</td>
    <td>bitmap</td>
    <td>'gray25'</td>
    <td>None</td>
  </tr>
  <tr>
    <td>tags</td>
    <td>Specifies a set of tags to apply to the item. TagList consists of a tuple of tag names, which replace any existing tags for the item. TagList may be empty.</td>
    <td>tuple</td>
    <td>('tag1', 'text')</td>
    <td>None</td>
  </tr>
  <tr>
    <td>text</td>
    <td>string specifies the characters to be displayed in the text item. Newline characters cause line breaks. The characters in the item may also be changed with the insert and delete methods.</td>
    <td>string</td>
    <td>'Hello'</td>
    <td>None</td>
  </tr>
</table>

Methods

create_text(x, y, *options)
The arguments x and y specify the coordinates of a point used to position the text on the display. After the coordinates there may be any number of option-value pairs, each of which sets one of the configuration options for the item. These same option-value pairs may be used in itemconfigure method calls to change the item’s configuration.