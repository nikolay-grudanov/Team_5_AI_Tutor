---
source_image: page_394.png
page_number: 394
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.31
tokens: 8185
characters: 1488
timestamp: 2025-12-24T00:42:22.408572
finish_reason: stop
---

Code comments

1 We create a thread object for each of the worker threads. Note that this does not start the thread; that must be done later.
2 Once the GUI has been created, we start the threads.
3 Note that the short sleep in worker_thread1 has been commented out.

If you run thread4.py, you will see output similar to thread3.py. Interestingly, the threading implementation runs 30 percent faster than the thread version.

18.2 "after" processing

The after method has been used frequently in examples, including the threading examples above, to provide simple alarm callbacks. For X window programmers, after is similar to XtAppAddTimeOut. after_idle is similar to XtAppAddWorkProc, which provides a simple mechanism to define a background task which is executed when there are no events in the event queue (with the exception of pending after events).

Here is a simple example which illustrates using after_idle to implement a busy cursor which is displayed when the system is processing a long operation. Before starting the operation, the application displays a watch cursor* and registers a work process. When the after_idle callback is invoked, the cursor changes back to the normal one.

![Three windows showing a busy cursor example](../images/fig18-6.png)

Figure 18.6 Using after_idle to implement a busy cursor

busy_cursor.py

import time
from Tkinter import *

class AfterIdleExample:

* On Win32, the watch cursor will display the current cursor selected for the watch.