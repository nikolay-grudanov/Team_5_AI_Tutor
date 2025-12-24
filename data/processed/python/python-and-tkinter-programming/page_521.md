---
source_image: page_521.png
page_number: 521
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.88
tokens: 8480
characters: 1825
timestamp: 2025-12-24T00:46:35.949073
finish_reason: stop
---

font, text, and initial relief. The label method returns the identity of the new widget. At the time this method is invoked, the label’s parent must exist.

A label is a widget that displays a textual string, bitmap or image. If text is displayed, it must all be in a single font, but it can occupy multiple lines on the screen (if it contains newlines or if wrapping occurs because of the wrapLength option) and one of the characters may optionally be underlined using the underline option. The label can be manipulated in a few simple ways, such as changing its relief or text, using the standard widget options.

Inheritance

Label inherits from Widget.

Shared options

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr><td>anchor</td><td>center</td></tr>
  <tr><td>background (bg)</td><td>SystemButtonFace</td></tr>
  <tr><td>bitmap</td><td></td></tr>
  <tr><td>borderwidth (bd)</td><td>2</td></tr>
  <tr><td>cursor</td><td></td></tr>
  <tr><td>font</td><td>(('MS', 'Sans', 'Serif'), '8')</td></tr>
  <tr><td>foreground (fg)</td><td>SystemButtonText</td></tr>
  <tr><td>height</td><td>0</td></tr>
  <tr><td>highlightbackground</td><td>SystemButtonFace</td></tr>
  <tr><td>highlightcolor</td><td>SystemWindowFrame</td></tr>
  <tr><td>highlightthickness</td><td>0</td></tr>
  <tr><td>image</td><td></td></tr>
  <tr><td>justify</td><td>center</td></tr>
  <tr><td>padx</td><td>1</td></tr>
  <tr><td>pady</td><td>1</td></tr>
  <tr><td>relief</td><td>flat</td></tr>
  <tr><td>takefocus</td><td>0</td></tr>
  <tr><td>text</td><td></td></tr>
  <tr><td>textvariable</td><td></td></tr>
  <tr><td>underline</td><td>-1</td></tr>
  <tr><td>width</td><td>0</td></tr>
  <tr><td>wraplength</td><td>0</td></tr>
</table>

Methods

There are no label methods, other than common widget methods such as configure.