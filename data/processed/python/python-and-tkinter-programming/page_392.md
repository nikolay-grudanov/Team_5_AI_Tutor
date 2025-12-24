---
source_image: page_392.png
page_number: 392
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.62
tokens: 8132
characters: 1203
timestamp: 2025-12-24T00:42:17.291468
finish_reason: stop
---

Figure 18.4 Threaded GUI application

With one thread going, we can try adding another thread. Since this example is not really very useful directly, we can make it do something pretty useless to illustrate multiple threads. We’ll just change the color of the Close button every 100 milliseconds with random colors. Here are the changes that have to be made to the code:

thread3.py

import time, thread, random
from Tkinter import *

class ThreadExample:
    def __init__(self, master=None):
        # --------Code Removed---------------------------------------------
        self.btn.pack(side=TOP, pady=5)
        thread.start_new_thread(self.worker_thread2, ())
        self.master.after(100, self.check_digits)

    def worker_thread1(self):
        # --------Code Removed---------------------------------------------

    def worker_thread2(self):
        while self.ok:
            self.btn.configure(background=self.color())
            time.sleep(0.1)

    def color(self):
        rc = random.choice
        return '%#02x%02x%02x' % (rc(range(0,255)), rc(range(0,255)),
                                 rc(range(0,255)))

    # --------Code Removed---------------------------------------------