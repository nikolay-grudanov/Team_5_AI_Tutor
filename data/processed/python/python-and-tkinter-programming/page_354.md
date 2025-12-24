---
source_image: page_354.png
page_number: 354
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.82
tokens: 8195
characters: 1323
timestamp: 2025-12-24T00:41:09.486442
finish_reason: stop
---

CHAPTER 15

Debugging applications

15.1 Why print statements? 329
15.2 A simple example 330
15.3 How to debug 333
15.4 A Tkinter explorer 334
15.5 pdb 336
15.6 IDLE 336
15.7 DDD 337

Debugging is a tricky area. I know that I’m going to get some stern comments from some of my readers, but I’m going to make a statement that is bound to inflame some of them. Python is easy to debug if you insert print statements at strategic points in suspect code.

Not that some excellent debug tools aren’t available, including IDLE, which is Python’s emerging IDE, but as we shall see later there are some situations where debuggers get in the way and introduce artifacts.

In this chapter we will look at some simple techniques that really work and I’ll offer some suggestions for readers who have not yet developed a method for debugging their applications.

15.1 Why print statements?

Debugging a simple Python program using a debugger rarely causes problems—you can happily single-step through the code, printing out data as changes are made, and you can make changes to data values to experiment with known values. When you are working with GUIs, networked applications or any code where timed events occur, it is difficult to predict the exact behavior of the application. This is why: for GUIs, a mainloop dispatches events in