---
source_image: page_384.png
page_number: 384
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.95
tokens: 8207
characters: 1685
timestamp: 2025-12-24T00:42:03.820369
finish_reason: stop
---

If you take a look at the output, you can see the three drawing-related routines that we saw earlier. They are responsible for about 20 percent of the overall cumulative time, so you can see that little of anything we have control over will really improve this application. However, your application might have many more opportunities for improvement.

You may also use some very simple benchmarking techniques to determine if a piece of code may be optimized by taking a particular approach. You just have to time a sequence of code. For example:

import time
...
def function():
    ...
start = time.clock(); function(); print round(time.clock() - start, 3)

Always use time.clock() for benchmarking, since it provides CPU time, as opposed to elapsed time

17.5 Python extensions

In “Extending Python” on page 313, we looked at building Python extensions, primarily as a way of extending functionality. In the area of performance improvements, extensions can be used to replace interpreted Python with compiled C. You first need to profile your application, as shown above. If you find candidate routines, you may be able to rewrite them in C. Remember that some of the power of Python comes from its high-level constructs. Sometimes it is difficult to reproduce such facilities in C—in fact the C-code may end up being less efficient than Python.

There are, however, plenty of places where adding an extension module to alleviate a bottleneck is worthwhile. Moderate floating-point operations, trigonometric operations and matrix operations are good candidates. In certain cases, complex dictionary processes may be faster to implement as C-calling-Python rather than pure Python.