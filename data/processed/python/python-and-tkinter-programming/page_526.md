---
source_image: page_526.png
page_number: 526
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.47
tokens: 8401
characters: 1811
timestamp: 2025-12-24T00:46:39.219810
finish_reason: stop
---

yview_moveto(fraction)
Adjusts the view in the window so that fraction of the total height of the listbox is off-screen to the top. fraction is a fraction between 0 and 1.

yview_scroll(number, what)
This command adjusts the view in the window up or down according to number and what. number must be an integer. what must be either UNITS or PAGES. If what is UNITS, the view adjusts up or down by number lines; if it is PAGES then the view adjusts by number screenfuls. If number is negative then earlier elements become visible; if it is positive then later elements become visible.

Menu

Button   Cascade   Checkbutton   Radiobutton

Description
The Menu class defines a new top-level window and creates an instance of a menu widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the menu such as its colors and font. The menu method returns the identity of the new widget. At the time this method is invoked, the menu’s parent must exist.

Inheritance
Menu inherits from Widget.

Shared options

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>activebackground</td>
    <td>SystemHighlight</td>
  </tr>
  <tr>
    <td>activeforeground</td>
    <td>SystemHighlightText</td>
  </tr>
  <tr>
    <td>background (bg)</td>
    <td>SystemMenu</td>
  </tr>
  <tr>
    <td>borderwidth (bd)</td>
    <td>1</td>
  </tr>
  <tr>
    <td>cursor</td>
    <td>arrow</td>
  </tr>
  <tr>
    <td>disabledforeground</td>
    <td>SystemDisabledText</td>
  </tr>
  <tr>
    <td>font</td>
    <td>('Georgia', '8')</td>
  </tr>
  <tr>
    <td>foreground (fg)</td>
    <td>SystemMenuText</td>
  </tr>
  <tr>
    <td>relief</td>
    <td>flat</td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td>0</td>
  </tr>
</table>