---
source_image: page_393.png
page_number: 393
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.71
tokens: 8246
characters: 1883
timestamp: 2025-12-24T00:42:25.788872
finish_reason: stop
---

There are two points to note: The second thread is started after the widgets have been created. If the thread had been started at the same time as the first thread, the Close button would not have been created. This would have prevented the second thread from running, but it would not have caused an application failure. This important feature of threading may be used to your advantage in designing applications if it’s used reasonably. Also note that the 100 ms sleep in worker_thread2 is used to time the period of the thread and not just to release the thread.

If you run thread3.py, you will see the same basic screen which is displayed by running thread2.py, but the Close button will change color rapidly.

![Random color changes in a thread](thread3.png)

Figure 18.5 Random color changes in a thread

Python provides a higher-level interface, threading, which takes care of many of the details of getting threads to cooperate. It also removes the need to add sleep calls to make sure that threads release control to other threads. To illustrate how this may be used, we can convert thread3.py to the threading module.

thread4.py

from threading import *

class ThreadExample:
    def __init__(self, master=None):
        self.ok = 1
        # --------Code Removed---------------------------------------------
        self.master = master

        self.thread1= Thread(target=self.worker_thread1)
        self.thread2= Thread(target=self.worker_thread2)  ①

        # --------Code Removed---------------------------------------------
        self.master.after(100, self.check_digits)
        self.thread1.start()
        self.thread2.start()

        def worker_thread1(self):
            # --------Code Removed---------------------------------------------
            ## time.sleep(0.001)  ③
            # --------Code Removed---------------------------------------------