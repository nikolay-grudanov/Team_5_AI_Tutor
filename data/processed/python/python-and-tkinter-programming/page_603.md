---
source_image: page_603.png
page_number: 603
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.88
tokens: 8515
characters: 2386
timestamp: 2025-12-24T00:49:14.285927
finish_reason: stop
---

NoteBook

Description
This widget replaces NoteBookR and NoteBookS in release 0_8_3 and later.

A notebook contains a set of tabbed pages. At any one time only one of these pages (the selected page) is visible, with the other pages being hidden “beneath” it. Another page in the notebook may be displayed by clicking on the tab attached to the page. The tabs are displayed along the top edge.

Optionally, the notebook may be displayed without tabs. In this case, another selection widget, such as Pmw.OptionMenu, may be used to select the pages.

Inheritance
NoteBook inherits from Pmw.MegaArchetype.

NoteBook options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>borderwidth</td>
    <td>The width of the border drawn around each tab and around the selected page.</td>
    <td>integer</td>
    <td>2</td>
  </tr>
  <tr>
    <td>createcommand</td>
    <td>Specifies a function to call when a page is selected for the first time. The function is called with a single argument, which is the name of the selected page, and it is called before the raisecommand function. This allows the creation of the page contents to be deferred until the page is first displayed.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>lowercommand</td>
    <td>Specifies a function to call when the selected page is replaced with a new selected page. The function is called with a single argument, which is the name of the previously selected page, and it is called before the createcommand or raisecommand functions.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>pagemargin</td>
    <td>The margin around the selected page inside the notebook’s page border.</td>
    <td>pixels</td>
    <td>4</td>
  </tr>
  <tr>
    <td>raisecommand</td>
    <td>Specifies a function to call when a new page is selected. The function is called with a single argument, which is the name of the selected page.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>tabpos</td>
    <td>Specifies the location of the tabs. If n, tabs are created for each page and positioned at the top of the notebook. If None, no tabs are created, in which case another selection widget can be used to select pages by calling the selectpage() method.</td>
    <td>string</td>
    <td>'n'</td>
  </tr>
</table>