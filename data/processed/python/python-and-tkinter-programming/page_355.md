---
source_image: page_355.png
page_number: 355
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.39
tokens: 8291
characters: 1949
timestamp: 2025-12-24T00:41:22.646217
finish_reason: stop
---

a particular timing sequence; for network applications there are timed events (in particular, time-outs which may be short enough to occur while single-stepping).

Since many of the applications that I have worked on have fallen into these categories, I have developed a method which usually avoids the pitfalls I have described. I say usually because even though adding print statements to an application only slightly increases the overall execution time, it still has an effect on CPU usage, output either to a file or stdout and the overall size of the code.

By all means try the tools that are available—they are very good. If you get results that have you totally confused, discouraged, or angry, try print statements!

15.2 A simple example

Many of the examples in this book use try ... except clauses to trap errors in execution. This is a good way of writing solid code, but it can make life difficult for the programmer if there are errors, since an error will cause Python to branch to the except section when an error occurs, possibly masking the real problem.

Python has one downside to testing a program: even though the syntax may be correct when Python compiles to bytecode, it may not be correct at runtime. Hence we need to locate and fix such errors. I have doctored one of the examples used earlier in the book to introduce a couple of runtime errors. This code is inside a try ... except clause with no defined exception; this is not a particularly good idea, but it does help the example, because it is really difficult to find the location of the error.

Let’s try running debug1.py:

C:> python debug1.py
An error has occurred!

To add insult to injury, we still get part of the expected output, as shown in figure 15.1.

![A screenshot of a plot window labeled 'Simple Plot - Version 3 - Smoothed' with a vertical axis and horizontal axis ranging from 0 to 100.](./images/figure_15_1.png)

Figure 15.1 Debugging stage one