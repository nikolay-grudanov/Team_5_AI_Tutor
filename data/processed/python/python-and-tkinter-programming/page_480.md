---
source_image: page_480.png
page_number: 480
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.27
tokens: 8290
characters: 1825
timestamp: 2025-12-24T00:45:08.596135
finish_reason: stop
---

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>default</td>
    <td>Specifies one of three states for the default ring (button): NORMAL, ACTIVE, or DISABLED. In ACTIVE state, the button is drawn with the platform-specific appearance for a default button. In NORMAL state, the button is drawn with the platform-specific appearance for a non-default button, leaving enough space to draw the default button appearance. The NORMAL and ACTIVE states will result in buttons of the same size. In DISABLED state, the button is drawn with the non-default button appearance without leaving space for the default appearance. The DISABLED state may result in a smaller button than the ACTIVE state.</td>
    <td>constant</td>
    <td>NORMAL<br>"disabled"</td>
    <td>disabled</td>
  </tr>
</table>

Methods

flash()
Flashes the button. This is accomplished by redisplaying the button several times, alternating between active and normal colors. At the end of the flash the button is left in the same normal/active state as when the method was invoked. This method is ignored if the button’s state is disabled.

invoke()
Invokes the callback associated with the button, if there is one. The return value is the return value from the callback, or an empty string if no callback is associated with the button. This method is ignored if the button’s state is disabled.

tkButtonDown(*ignored)
tkButtonEnter(*ignored)
tkButtonInvoke(*ignored)
tkButtonLeave(*ignored)
tkButtonUp(*ignored)
These methods are really only useful if you are writing your own event-handling for buttons. Their function is to set the button’s appearance as if the default actions had occurred. They may also be useful in simulating user interaction with a GUI.