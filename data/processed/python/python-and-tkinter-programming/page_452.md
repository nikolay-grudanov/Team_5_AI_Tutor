---
source_image: page_452.png
page_number: 452
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.52
tokens: 8337
characters: 1713
timestamp: 2025-12-24T00:44:11.045549
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>All widgets except:</th>
  </tr>
  <tr>
    <td>relief</td>
    <td>Specifies the 3-D effect desired for the widget. Acceptable values are RAISED, SUNKEN, FLAT, RIDGE, SOLID, and GROOVE. The value indicates how the interior of the widget should appear relative to its exterior; for example, RAISED means the interior of the widget should appear to protrude from the screen, relative to the exterior of the widget.</td>
    <td>constant</td>
    <td>RAISED<br>GROOVE</td>
    <td></td>
  </tr>
  <tr>
    <td>takefocus</td>
    <td>Determines whether the window accepts the focus during keyboard traversal (e.g., TAB and SHIFT-TAB). Before setting the focus to a window, the traversal scripts consult the value of the takefocus option. A value of 0 means that the window should be skipped entirely during keyboard traversal. 1 means that the window should receive the input focus as long as it is viewable (it and all of its ancestors are mapped). An empty value for the option means that the traversal scripts make the decision about whether or not to focus on the window: the current algorithm is to skip the window if it is disabled, if it has no key bindings, or if it is not viewable.</td>
    <td>boolean</td>
    <td>1 YES</td>
    <td></td>
  </tr>
  <tr>
    <td>width</td>
    <td>Specifies an integer value indicating the desired width of the widget, in average-size characters of the widget’s font. If the value is less than or equal to zero, to widget picks a size just large enough to hold its current text.</td>
    <td>integer</td>
    <td>32</td>
    <td>Menu</td>
  </tr>
</table>