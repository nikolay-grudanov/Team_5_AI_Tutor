---
source_image: page_623.png
page_number: 623
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.28
tokens: 8377
characters: 2135
timestamp: 2025-12-24T00:49:33.740866
finish_reason: stop
---

Methods

interior()
Returns the frame within which the programmer may create widgets to be scrolled. This is the same as component('frame').

reposition()
Updates the position of the frame component in the clipper and updates the scrollbar.
    Usually, this method does not need to be called explicitly, since the position of the frame component and the scrollbars are automatically updated whenever the size of the frame or clipper components change or the user clicks in the scrollbars. However, if horizflex or vertflex is expand, the megawidget cannot detect when the requested size of the frame increases to greater than the size of the clipper. Therefore, this method should be called when a new widget is added to the frame (or a widget is increased in size) after the initial megawidget construction.

ScrolledListBox

Description
This megawidget consists of a standard listbox widget with optional scrollbars which can be used to scroll the listbox. The scrollbars can be dynamic, which means that a scrollbar will only be displayed if it is necessary—if the listbox does not contain enough entries, the vertical scrollbar will be automatically hidden and if the entries are not wide enough, the horizontal scrollbar will be automatically hidden.

Inheritance
ScrolledListBox inherits from Pmw.MegaWidget.

ScrolledListBox options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>dblclickcommand</td>
    <td>This specifies a function to call when mouse button 1 is double clicked over an entry in the listbox component.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>hscrollmode</td>
    <td>The horizontal scroll mode. If none, the horizontal scrollbar will never be displayed. If static, the scrollbar will always be displayed. If dynamic, the scrollbar will be displayed only if necessary.</td>
    <td>constant</td>
    <td>'dynamic'</td>
  </tr>
  <tr>
    <td>items</td>
    <td>A tuple containing the initial items to be displayed by the listbox component.</td>
    <td>(string, ...)</td>
    <td>()</td>
  </tr>
</table>