---
source_image: page_287.png
page_number: 287
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.15
tokens: 8369
characters: 2185
timestamp: 2025-12-24T00:39:22.148396
finish_reason: stop
---

Code comments

1 This example has to create many bindings:
   1 An <Enter> callback to color the grab handle.
   2 A <Leave> callback to remove the added color.
   3 A <Button-1> (<1>) callback for each of the grab handles.
   4 A <B1-Motion> callback for a common callback for each of the grabs.
   5 An <Any-ButtonRelease-1> callback to process the final location of the grab.

2 The responsibility of each of the three arrowMove methods is to validate that the value is within bounds and then draw the grab at the current location.

3 Since we have three separate boxes (box1, box2 and box3) we need to implement a simple search algorithm within the tags to determine which box created the event:

    if 'box' in tags:
        for tag in tags:
            if len(tag) == 4 and tag[:3] == 'box':
                cur = tag
                break

4 We then create a line using the supplied width and the appropriate arrowshape values.

    The remainder of the code is responsible for updating the values of the dimensions on the screen and drawing the example arrows. Since this example illustrates 1-to-1 translation of Tk to Tkinter, I have not attempted to optimize the code. I am certain that some of the code can be made more succinct.

10.6 Some finishing touches

We are going to extend the capability of draw3.py to add some additional functionality and provide some features that may be useful if you use this example as a template for your own code. This is what has been added:

1 Menu options to create New drawings and Open existing ones.
2 A Menu option to save drawings with a supplied filename (Save As).
3 A Menu option to save an existing drawing to its file (Save).
4 A Move operation to allow an object to be moved about the canvas.
5 Stretch operations with eight grab handles.

The following code example is derived from draw3.py, which was presented on page 245. I have removed much of the common code, so that this example is not too long, but note that this example has a lot to do!

draw4.py

from Tkinter import *
import Pmw, AppShell, math, time, string, marshal
from cursornames import *
from toolbarbutton import ToolBarButton
from tkFileDialog import *