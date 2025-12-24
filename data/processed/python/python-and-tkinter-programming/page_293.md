---
source_image: page_293.png
page_number: 293
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.01
tokens: 8306
characters: 1660
timestamp: 2025-12-24T00:39:25.634039
finish_reason: stop
---

key, value = string.split(tag, '*')
var = transDict[key]
setattr(self, var, string.atoi(value))

This requires a little more explanation. Take a look at figure 10.11. Each of the grab handles at the four corners modifies the bounding box. The x- or y-value is associated with either BB1 or BB2. So, for example, the bottom-left grab handle is tagged with bx*1 and by*2. Additionally, the four median grab handles are constrained to stretch one side of the bounding box at a time, so we encode (as a boolean value) the axis that is free (x*1 y*0 indicates that the x-axis is free).

7 Since we need to know the current dimensions of an object’s bounding box as we grow or move the object, we store that data each time the callback is invoked.

8 When the mouse is released, we have to recalculate the bounding box and store the object’s data. This code is similar to the code for mouse movement shown in 6.

9 In addGrabHandles we begin by removing all existing grab handles from the display, along with the associated tags.

10 To construct the grab handles, we first get the current bounding box. Then we construct the handles using data contained in a list. The tags are constructed to provide the associations noted in step 6 above.

![Figure 10.11 Grab handles and their association with the bounding-box coordinates](./images/figure_10_11.png)

Figure 10.11 Grab handles and their association with the bounding-box coordinates

draw4.py (continued)

x1,y1,x2,y2 = self.canvas.bbox(tag)
for x,y, curs, tagBx, tagBy, tagX, tagY in [
    (x1,y1,TLC,      'bx*1','by*1','x*1','y*1'),
    (x2,y1,TRC,      'bx*2','by*1','x*1','y*1'),
    ---- code removed ----