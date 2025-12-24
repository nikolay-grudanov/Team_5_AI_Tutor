---
source_image: page_266.png
page_number: 266
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.85
tokens: 8233
characters: 1695
timestamp: 2025-12-24T00:38:43.638096
finish_reason: stop
---

self.background = 'white'

def close(self):
    self.quit()

def createInterface(self):
    AppShell.AppShell.createInterface(self)
    self.createButtons()
    self.initData()
    self.createBase()

if __name__ == '__main__':
    draw = Draw()
    draw.run()

Code comments

1 This example is completely pointer-driven so it relies on binding functionality to mouse events. We bind click, movement and release to appropriate member functions.

    Widget.bind(self.canvas, "<Button-1>", self.mouseDown)
    Widget.bind(self.canvas, "<Button1-Motion>", self.mouseMotion)
    Widget.bind(self.canvas, "<Button1-ButtonRelease>", self.mouseUp)

2 This simple example supports three basic shapes. We build Pmw.RadioSelect buttons to link each of the shapes with an appropriate drawing function. Additionally, we define a selection option which allows us to click on the canvas without drawing.

3 The mouseDown method deselects any currently selected object. The event returns x- and y-coordinates for the mouse-click as screen coordinates. The canvasx and canvasy methods of the Canvas widget convert these screen coordinates into coordinates relative to the canvas.

    def mouseDown(self, event):
        self.currentObject = None
        self.lastx = self.startx = self.canvas.canvasx(event.x)
        self.lasty = self.starty = self.canvas.canvasy(event.y)

Converting the x- and y-coordinates to canvas coordinates is a step that is often forgotten when first coding canvas-based applications. Figure 10.3 illustrates what this means.

![Figure 10.3 Relationship between screen and canvas coordinates](./figures/figure_10_3.png)

Figure 10.3 Relationship between screen and canvas coordinates