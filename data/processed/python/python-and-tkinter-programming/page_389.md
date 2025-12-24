---
source_image: page_389.png
page_number: 389
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.13
tokens: 8438
characters: 2614
timestamp: 2025-12-24T00:42:29.356247
finish_reason: stop
---

threads within the process run when a thread does I/O. However, printing to stdout does not qualify as blocking I/O (at least when running simple Python scripts), so the thread continues to process instructions until it ends its timeslice or actually does some blocking I/O.

If you look at the fragment of output shown in figure 18.1, you will see that when the example is run with the short sleep after each print, we switch to the next thread and do one print. The result is that the output cycles in blocks of four prints, one from each thread, as shown within the gray boxes in figure 18.1.

![Figure 18.2 Effect of running threads with a sleep after each print](https://i.imgur.com/3Q5z5QG.png)

Figure 18.2 Effect of running threads with a sleep after each print

If you remove the time.sleep call after the print statement, you will change the example’s runtime behavior. Running the example again will produce output similar to the fragment shown in figure 18.3. Notice how one of the threads has completed the loop during a timeslice and that the next thread outputs characters sequentially.

![Figure 18.3 Effect of running threads without sleeping after each print](https://i.imgur.com/3Q5z5QG.png)

Figure 18.3 Effect of running threads without sleeping after each print

The last time.sleep call is very important. There is no mainloop in this program since there is no GUI; if you omit the sleep, the main thread will exit, and the child threads will be killed. This problem can be infuriating when you first start programming threads. Nothing seems to work and until you realize that the main thread is just exiting, you will run the application repeatedly—sometimes getting variable results.

Now, this very simplistic example relies on the fact that data sharing between the threads is not an issue. In fact, we’re lucky that it works at all. If you look at the engine method, you’ll notice the for loop. The controlled variable, i, might appear to be shared between the threads, but in reality it is not; each thread creates a new reference to the controlled variable, since local variables on a thread’s stack are thread-local. It is probably not a good idea to rely on such features to build threaded applications—there are too many rules to be followed and broken.

The problem, stated simplistically, is that you cannot predict when a thread will get preempted* and if this happens when you’re halfway through a series of instructions which make

* When a running process is stopped to allow another process to run (a process exchange), it is normally referred to as having been “preempted.”