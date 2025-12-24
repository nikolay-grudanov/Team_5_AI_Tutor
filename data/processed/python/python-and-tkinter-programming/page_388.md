---
source_image: page_388.png
page_number: 388
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.18
tokens: 8245
characters: 1784
timestamp: 2025-12-24T00:42:16.102080
finish_reason: stop
---

Code comments

1 The constructor creates a simple dispatch dictionary that will be used to select a particular method to be called.

2 The service method is the dispatcher for this skeleton server. Naturally, a real implementation would be more complex.

3 Each of the four service methods start the same method in a new thread, passing the input argument and an identifier.

def serviceA(self, argin):
    thread.start_new_thread(self.engine, (argin,'B'))

Note that start_new_thread expects arguments to the method to be supplied as a tuple.

4 The example service engine is pretty simple; it just loops and prints to stdout.

5 The call time.sleep(0.0001) is important because it ensures that the thread blocks for a very short time, allowing other threads to run. See below for further notes on this subject.

6 The call to time.sleep as the final line of the example is also very important for reasons that will be explained below.

If you run thread1.py, you’ll see output to stdout which should look something like figure 18.1. The output is ugly, but it can be used to illustrate a few points about threads and the way that the code layout can affect behavior.

![Screenshot of command prompt window showing output from running thread1.py](./images/figure_18_1.png)

Figure 18.1 Output from running thread1.py

This example starts four threads that loop 500 times, printing a few characters in each iteration. Depending on the way that the scheduler is implemented for the operating system in use, each process will receive a finite timeslice in which to execute. In a non-threaded system, doing input/output operations will suspend the process until the operation completes, thereby allowing other processes to run. With threads, we have a similar situation except that other