---
source_image: page_390.png
page_number: 390
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.72
tokens: 8377
characters: 2135
timestamp: 2025-12-24T00:42:29.414888
finish_reason: stop
---

up an atomic* operation, the result of another thread executing the same code path can be disastrous. If it is important that threads maintain atomic operations, you need to use locks (semaphores or mutexes†) to prevent another thread from gaining access to shared data. You can find some examples of locking in the standard Python distribution in the Demo/threads directory.

18.1.2 GUI threads

The decision to use threads with a GUI must be made with some caution. In general, a system that uses threads must ensure that the GUI is updated from within the main thread, which includes the mainloop. The following example is an adaptation of wpi.py, of one of the threading examples in the standard Python distribution. The example has a main thread which creates a GUI and starts the mainloop, and a thread which continuously calculates successive digits of pi. In addition, the example uses Tkinter’s event loop to update the GUI periodically.

thread2.py

# Display digits of pi in a window, calculating in a separate thread.
# Compare with wpi.py in Demo/threads/wpi.py.

import sys
import time
import thread
from Tkinter import *

class ThreadExample:
    def __init__(self, master=None):
        self.ok = 1
        self.digits = []
        self.digits_calculated = 0
        self.digits_displayed = 0
        self.master = master

        thread.start_new_thread(self.worker_thread, ()) ①

        self.frame = Frame(master, relief=RAISED, borderwidth=2)
        self.text = Text(self.frame, height=26, width=50)
        self.scroll = Scrollbar(self.frame, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.text.pack(side=LEFT)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.frame.pack(padx=4, pady=4)
        Button(master, text='Close', command=self.shutdown).pack(side=TOP)

        self.master.after(100, self.check_digits) ②

    def worker_thread(self):
        k, a, b, a1, b1 = 21, 41, 11, 121, 41
        while self.ok:

* Atomic operations complete in their entirety before any other process or thread can follow the same code path.
† Mutual exclusion locks.