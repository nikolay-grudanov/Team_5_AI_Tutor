---
source_image: page_304.png
page_number: 304
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.28
tokens: 8118
characters: 1163
timestamp: 2025-12-24T00:39:49.931312
finish_reason: stop
---

Figure 11.3 Smoothing the line

simpleplot3.py

canvas.create_line(scaled, fill='black', smooth=1)

I don’t think that needs an explanation!

11.2 A graph widget

The previous examples illustrate that it is quite easy to produce simple graphs with a small amount of code. However, when it is necessary to display several graphs on the same axes, it is cumbersome to produce code that will be flexible enough to handle all situations. Some time ago Konrad Hinsen made an effective graph widget available to the Python community. The widget was intended to be used with NumPy.* With his permission, I have adapted it to make it usable with the standard Python distribution and I have extended it to support additional display formats. An example of the output is shown in figure 11.4. In the following code listing, I have removed some repetitive code. You will find the complete source code online.

plot.py

from Tkinter import *
from Canvas import Line, CanvasText
import string, math
from utils import *
from math import pi

* NumPy is Numeric Python, a specialized collection of additional modules to facilitate numeric computation where performance is needed.