---
source_image: page_543.png
page_number: 543
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.36
tokens: 8448
characters: 2354
timestamp: 2025-12-24T00:47:16.984856
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
    <td>x</td>
    <td>location specifies the x-coordinate within the master window of the anchor point for window. The location is specified in screen units and need not lie within the bounds of the master window.</td>
    <td>integer</td>
    <td>105</td>
    <td>0</td>
  </tr>
  <tr>
    <td>width</td>
    <td>size specifies the width for window in screen units (i.e. any of the forms accepted by Tkinter (Tk_GetPixels)). The width will be the outer width of the window including its border, if any. If size is empty, or if no width or relwidth option is specified, then the width requested internally by the window will be used.</td>
    <td>integer</td>
    <td>125</td>
    <td>natural width</td>
  </tr>
  <tr>
    <td>y</td>
    <td>location specifies the y-coordinate within the master window of the anchor point for window. The location is specified in screen units and need not lie within the bounds of the master window.</td>
    <td>integer</td>
    <td>88</td>
    <td>0</td>
  </tr>
</table>

Methods

place(option=value, ...)
The arguments consist of one or more option-value pairs that specify the way in which self’s geometry is managed. If the Placer is already managing self, then the option-value pairs modify the configuration for its window. In this form the place method returns None as the result.

place_forget()
The place_forget method causes the Placer to stop managing the geometry of window. As a side effect of this method self will be unmapped so that it doesn’t appear on the screen. If self isn’t currently managed by the Placer then the method has no effect.

place_info()
The place_info method returns a dictionary giving the current configuration of the window. The dictionary consists of option-value pairs in exactly the same form as might be specified to the place method. If the configuration of a window has been retrieved with place_info, that configuration can be restored later by first using place_forget to erase any existing information for the window and then invoking place with the saved information.

place_slaves()
The place_slaves method returns a list of all the slave windows for which self is the master. If there are no slaves for self then None is returned.