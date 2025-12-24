---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.21
tokens: 8344
characters: 2118
timestamp: 2025-12-24T00:37:32.078073
finish_reason: stop
---

Code comments

1 The first task is to determine the size of the image to be mapped. Since we want to display the image on a canvas, we cannot just load the image, because the canvas will not resize to fit the image. Therefore, get the size of the image and size the canvas appropriately:

self.img = PhotoImage(file=file)
self.width = self.img.width()
self.height = self.img.height()

2 Our tool implements a simple graphic selection rectangle to show the selected target area. We bind functions to mouse button press and release and also to mouse motion:

Widget.bind(self.canvas, "<Button-1>", self.mouseDown)
Widget.bind(self.canvas, "<Button1-Motion>", self.mouseMotion)
Widget.bind(self.canvas, "<Button1-ButtonRelease>", self.mouseUp)

3 mouseDown converts the x- and y-screen coordinates of the mouse button press to coordinates relative to the canvas, which corresponds to the image coordinates:

def mouseDown(self, event):
    self.startx = self.canvas.canvasx(event.x)
    self.starty = self.canvas.canvasy(event.y)

4 mouseMotion continuously updates the size of the selection rectangle with the current coordinates:

def mouseMotion(self, event):
    x = self.canvas.canvasx(event.x)
    y = self.canvas.canvasy(event.y)

    if (self.startx != event.x) and (self.starty != event.y) :
        self.canvas.delete(self.rubberbandBox)
        self.rubberbandBox = self.canvas.create_rectangle(
            self.startx, self.starty, x, y, outline='white', width=2)

5 Each time we update the selection rectangle, we have to call update_idletasks to display the changes. Doing a drag operation such as this causes a flood of events as the mouse moves, so we need to make sure that the screen writes get done in a timely fashion:

self.root.update_idletasks()

6 When the mouse button is released, we convert the coordinates of the finishing location and set focus to the entry widget to collect the identity of the map:

def mouseUp(self, event):
    self.endx = self.canvas.canvasx(event.x)
    self.endy = self.canvas.canvasy(event.y)
    self.reference.focus_set()
    self.reference.selection_range(0, END)