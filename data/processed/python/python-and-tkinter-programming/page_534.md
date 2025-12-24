---
source_image: page_534.png
page_number: 534
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.10
tokens: 8664
characters: 2678
timestamp: 2025-12-24T00:47:09.353366
finish_reason: stop
---

relief. The message method returns the identity of the new widget. At the time this method is invoked, the message’s parent must exist.

A message is a widget that displays a textual string. A message widget has three special features. First, it breaks up its string into lines in order to produce a given aspect ratio for the window. The line breaks are chosen at word boundaries wherever possible (if not even a single word will fit on a line, then the word will be split across lines). Newline characters in the string will force line breaks; they can be used, for example, to leave blank lines in the display.

The second feature of a message widget is justification. The text may be displayed left-justified (each line starts at the left side of the window), centered on a line-by-line basis, or right-justified (each line ends at the right side of the window).

The third feature of a message widget is that it handles control characters and non-printing characters specially. Tab characters are replaced with enough blank space to line up on the next 8-character boundary. Newlines cause line breaks. Other control characters (ASCII code less than \(0 \times 20\)) and characters not defined in the font are displayed as a four-character sequence \xhhh where hh is the two-digit hexadecimal number corresponding to the character. In the unusual case where the font doesn’t contain all of the characters in 0123456789abcdefghijklmnopqrstuvwxyz then control characters and undefined characters are not displayed at all.

Inheritance

Message inherits from Widget.

Shared options

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>anchor</td>
    <td>center</td>
  </tr>
  <tr>
    <td>background (bg)</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>borderwidth (bd)</td>
    <td>2</td>
  </tr>
  <tr>
    <td>cursor</td>
    <td></td>
  </tr>
  <tr>
    <td>font</td>
    <td>(('MS', 'Sans', 'Serif'), '8')</td>
  </tr>
  <tr>
    <td>foreground (fg)</td>
    <td>SystemButtonText</td>
  </tr>
  <tr>
    <td>highlightbackground</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>highlightcolor</td>
    <td>SystemWindowFrame</td>
  </tr>
  <tr>
    <td>highlightthickness</td>
    <td>0</td>
  </tr>
  <tr>
    <td>justify</td>
    <td>left</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>flat</td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td>0</td>
  </tr>
  <tr>
    <td>text</td>
    <td></td>
  </tr>
  <tr>
    <td>textvariable</td>
    <td></td>
  </tr>
  <tr>
    <td>width</td>
    <td>0</td>
  </tr>
</table>