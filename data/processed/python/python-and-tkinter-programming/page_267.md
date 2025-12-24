---
source_image: page_267.png
page_number: 267
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.76
tokens: 8287
characters: 1989
timestamp: 2025-12-24T00:38:49.681872
finish_reason: stop
---

When the user clicks on the canvas, the click effectively goes through to the desktop and these coordinates are returned in the event. Converting to canvas coordinates returns the coordinates relative to the canvas origin, regardless of where the canvas is on the screen.

4 If no drawing function is selected, we are in select mode, and we search to locate the nearest object on the canvas and select it. This method of selection may not be appropriate for all drawing applications, since the method will always find an object, no matter where the canvas is clicked. This can lead to some confusing behavior in certain complex diagrams, so the selection model might require direct clicking on an object to select it.

    if not self.currentFunc:
        self.selObj = self.canvas.find_closest(self.startx,
                                               self.starty))
        self.canvas.itemconfig(self.selObj, width=2)
        self.canvas.lift(self.selObj)

    Having selected the object, we thicken its outline and raise (lift) it to the top of the drawing stack, as shown in figure 10.4.

![Selecting an object on a canvas](./figures/fig_10_4.png)

Figure 10.4 Selecting an object on a canvas

5 As the mouse is moved (with the button down), we receive a stream of motion events. Each of these represents a change in the bounding box for the object. Having converted the x- and y-coordinates to canvas points, we delete the existing canvas object and redraw it using the current function and the new bounding box.

    self.canvas.delete(self.currentObject)
    self.currentFunc(self.startx, self.starty,
                     self.lastx, self.lasty,
                     self.foreground, self.background)

6 The drawing methods are quite simple; they’re just creating canvas primitives within the bounding box.

    def drawLine(self, x, y, x2, y2, fg, bg):
        self.currentObject = self.canvas.create_line(x,y,x2,y2,
                                                     fill=fg)