---
source_image: page_022.png
page_number: 22
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.70
tokens: 8216
characters: 1663
timestamp: 2025-12-24T00:31:49.967780
finish_reason: stop
---

conventions

Example code plays a very important role in Python and Tkinter Programming. Many programming books feature short, simple examples which illustrate one or two points very well—but really do little. In this book, the examples may be adapted for your own applications or even used just as they are. Most of the examples are intended to be run stand-alone as opposed to being run interactively. Most examples include markers in the body of the code which correspond to explanations which follow. For example:

def mouseDown(self, event):
    self.currentObject = None
    self.lastx = self.startx = self.canvas.canvasx(event.x)
    self.lasty = self.starty = self.canvas.canvasy(event.y)
    if not self.currentFunc:
        self.selObj = self.canvas.find_closest(self.startx,
            self.starty)[0]
        self.canvas.itemconfig(self.selObj, width=2)
    self.canvas.lift(self.selObj)

Code comments
① The mouseDown method deselects any currently selected object. The event returns x and y coordinates for the mouse-click as screen coordinates. The canvasx and canvasy methods of the Canvas widget ...
② If no drawing function is selected, we are in select mode and we search to locate the nearest object on the canvas and select it. This method of ...

Occasionally, I have set portions of code in bold code font to highlight code which is of special importance in the code example.
In a number of examples where the code spans several pages I have interspersed code explanations within the code sequence so that the explanatory text appears closer to the code that is being explained. The marker numbering is continuous within any given example.