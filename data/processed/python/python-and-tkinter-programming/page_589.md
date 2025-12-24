---
source_image: page_589.png
page_number: 589
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.66
tokens: 8197
characters: 1390
timestamp: 2025-12-24T00:48:35.500515
finish_reason: stop
---

specified by the entry_textvariable option, this method should be called after the set() method of the variable is called. If this is not done in this case, the entry widget background will not be set correctly.

clear()
Removes all text from the entry widget. Equivalent to setentry('').

invoke()
Invokes the command specified by the command option as if the RETURN key had been pressed and returns the result.

setentry(text)
Sets the contents of the entry widget to text and carries out validation as if the text had been entered by the user. If the text is invalid, the entry widget will not be changed and the invalidcommand function will be called.

valid()
Returns true if the contents of the entry widget are valid.

Group

Description
This megawidget consists of an interior frame with an exterior ring border and an identifying tag displayed over the top edge of the ring. The programmer can create other widgets within the interior frame.

Inheritance
Group inherits from Pmw.MegaWidget.

Group options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>tagindentl</td>
    <td>The distance from the left edge of the ring to the left side of the tag component.</td>
    <td>distance</td>
    <td>10</td>
  </tr>
</table>

Components

groupchildsite
The frame which can contain other widgets to be grouped.