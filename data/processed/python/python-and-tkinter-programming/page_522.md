---
source_image: page_522.png
page_number: 522
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.47
tokens: 8551
characters: 2355
timestamp: 2025-12-24T00:46:39.657079
finish_reason: stop
---

Listbox

Description
The Listbox class defines a new window and creates an instance of a listbox widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the listbox such as its colors, font, text, and relief. The listbox method returns the identity of the new widget. At the time this method is invoked, the listbox’s parent must exist.

A listbox is a widget that displays a list of strings, one per line. When first created, a new listbox has no elements. Elements may be added or deleted using the methods described below. In addition, one or more elements may be selected as described below.

If a listbox is exporting its selection (see the exportSelection option), then it will observe the standard X11 protocols for handling the selection. Listbox selections are available as type STRING; the value of the selection will be the text of the selected elements, with new-lines separating the elements.

It is not necessary for all the elements to be displayed in the listbox window at once; commands described below may be used to change the view in the window. Listboxes allow scrolling in both directions using the standard xScrollCommand and yScrollCommand options. They also support scanning, as described below.

Inheritance
Listbox inherits from Widget.

Shared options

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
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
    <td>height</td>
    <td>10</td>
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
    <td>1</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>sunken</td>
  </tr>
  <tr>
    <td>selectbackground</td>
    <td>SystemHighlight</td>
  </tr>
  <tr>
    <td>selectborderwidth</td>
    <td>1</td>
  </tr>
  <tr>
    <td>selectforeground</td>
    <td>SystemHighlightText</td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td></td>
  </tr>
</table>