---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.02
tokens: 8439
characters: 2425
timestamp: 2025-12-24T00:39:16.102534
finish_reason: stop
---

Code comments

1 This example illustrates how dimensions may be specified in any valid Tkinter distance and converted to pixels (in this case as a floating point number),
self.right = c.winfo_fpixels('13c')

2 Similarly, we can create an object using absolute measurements (in this case, centimeters). This can be useful if you are working directly from a drawing and you have a ruler!
    c.create_line('1c', '0.5c', '1c', '1c', '13c', '1c',
                  '13c', '0.5c', width=1)

3 Tkinter sometimes hides the capability of the underlying Tk function. In this case we are adding two tags, active and tab, to the newly-created object newTab.
    newTab = self.mkTab(x, y)
    self.canvas.addtag_withtag('active', newTab)
    self.canvas.addtag_withtag('tab', newTab)
    The addtag_withtag method hides the fact that the withtag argument applies to both tags and ids, which are being passed here.

4 moveTab has a lot of work to do, since the user can create new tabs, as well as move and delete existing ones. If I weren’t following Ousterhout’s example, I would probably reduce the complexity here.

5 The ruler arranges to snap the tab to the nearest 0.25 cm (self.grid). The canvasx method takes an optional argument, which defines the resolution with which the conversion to canvas coordinates is to be made.
    cx = self.canvas.canvasx(x, self.grid)

6 If the pointer moves between the top and bottom range of the ruler, we snap the vertical position of the tab and fill it with a distinctive color so that it is readily identified.
    cy = self.top+2
    self.canvas.itemconfig('active', fill=self.activeStyle,
                          stipple=self.activeStipple)

7 If we have moved outside the bounds of top and bottom, we push it out further and fill it with a distinctive color stippling so that it becomes a ghost.
    cy = cy-self.size-2
    self.canvas.itemconfig('active', fill=self.deleteStyle,
                          stipple=self.deleteStipple)

8 As with moving the tab, releasing it requires multiple actions.

9 If the tab is marked for deletion (it isn’t at the snapped-to y-value) the object is deleted.
    if self.y != self.top+2:
        self.canvas.delete('active')

10 Otherwise, we fill the tab with a normal color and delete the active tag.
    self.canvas.itemconfig('active', fill=self.normalStyle,
                          stipple=self.activeStipple)
    self.canvas.dtag('active')