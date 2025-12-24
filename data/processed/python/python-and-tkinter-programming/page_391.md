---
source_image: page_391.png
page_number: 391
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.12
tokens: 8421
characters: 2039
timestamp: 2025-12-24T00:42:34.757036
finish_reason: stop
---

# Next approximation
p, q, k = k*k, 2l*k+1l, k+1l
a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
# Print common digits
d, d1 = a/b, a1/b1
while d == d1:
    self.digits.append(`int(d)`)
    a, a1 = 10l*(a%b), 10l*(a1%b1)
    d, d1 = a/b, a1/b1
    time.sleep(0.001)

def shutdown(self):
    self.ok =0
    self.master.after(100, self.master.quit)

def check_digits(self):
    self.digits_calculated = len(self.digits)
    diff = self.digits_calculated - self.digits_displayed
    ix = self.digits_displayed
    for i in range(diff):
        self.text.insert(END, self.digits[ix+i])
    self.digits_displayed = self.digits_calculated
    self.master.title('%d digits of pi' % self.digits_displayed)
    self.master.after(100, self.check_digits)

root = Tk()
root.option_readfile('optionDB')
example = ThreadExample(root)
root.mainloop()

Code comments

1 The worker_thread, which continuously updates digits of pi, is started up as before, with start_new_thread.
2 We are using after to place a timed event on the event queue. Using this technique allows a delay without blocking the mainloop.
3 Again, a small sleep is added at the end of the worker_thread’s loop to ensure that the mainloop gets to spin (see below for more detail).
4 To ensure an orderly shutdown of the application, we set the ok flag, which will cause the worker_thread to exit and wait for 100 ms before killing the GUI. A more realistic application might need additional methods.
5 after events are one-shot events; you must put an event back on the queue if the timed event is to be repetitive.

If you run thread2.py, you will see a screen similar to figure 18.4. Digits are appended to the text widget at approximately 100ms intervals. You may wish to experiment and comment out the sleep in the worker_thread. When you run the code, you will see that the application takes much longer to respond to a click on the Close button—the worker_thread gets a complete timeslice to run before getting suspended, so the event queue for GUI events gets drained less frequently.