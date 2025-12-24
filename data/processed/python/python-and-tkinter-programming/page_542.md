---
source_image: page_542.png
page_number: 542
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.45
tokens: 8568
characters: 2828
timestamp: 2025-12-24T00:47:23.843535
finish_reason: stop
---

Вот таблица с описанием опций и их значений:

| Option | Description | Units | Typical | Default |
|--------|-------------|-------|---------|---------|
| height | value specifies the height for window in screen units. The height will be the outer dimension of the window including its border, if any. If no height or relheight option is specified, then the height requested internally by the window will be used. | integer | 134 | Natural size |
| in_    | value specifed the identity of the window relative to which window is to be placed. Master must either be window’s parent or a descendant of window’s parent. In addition, master and window must both be descendants of the same top-level window. These restrictions are necessary to guarantee that window is visible whenever master is visible. | widget | fred | parent |
| relheight | value specifies the height for window. In this case the height is specified as a floating-point number relative to the height of the master: 0.5 means window will be half as high as the master, 1.0 means window will have the same height as the master, and so on. If both height and relheight are specified for a slave, their values are summed. For example, relheight 1.0 height 2 makes the slave 2 pixels shorter than the master. | float | 0.45 | 1.0 |
| relwidth | value specifies the width for window. In this case the width is specified as a floating-point number relative to the width of the master: 0.5 means window will be half as wide as the master, 1.0 means window will have the same width as the master, and so on. If both width and relwidth are specified for a slave, their values are summed. For example, relwidth 1.0 width 5 makes the slave 5 pixels wider than the master. | float | 0.5 | 1.0 |
| relx   | location specifies the x-coordinate within the master window of the anchor point for window. In this case the location is specified in a relative fashion as a floating-point number: 0.0 corresponds to the left edge of the master and 1.0 corresponds to the right edge of the master. location need not be in the range 0.0 - 1.0. If both x and relx are specified for a slave then their values are summed. For example, relx 0.5 × 2 positions the left edge of the slave 2 pixels to the left of the center of its master. | float | 0.66 | 0.0 |
| rely   | location specifies the y-coordinate within the master window of the anchor point for window. In this case the value is specified in a relative fashion as a floating-point number: 0.0 corresponds to the top edge of the master and 1.0 corresponds to the bottom edge of the master. location need not be in the range 0.01.0. If both y and rely are specified for a slave then their values are summed. For example, rely 0.5 × 3 positions the top edge of the slave 3 pixels below the center of its master. | float | 0.34 | 0.0 |