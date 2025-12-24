---
source_image: page_373.png
page_number: 373
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.84
tokens: 8111
characters: 1113
timestamp: 2025-12-24T00:41:42.727617
finish_reason: stop
---

CHAPTER 17

Programming for performance

17.1 Everyday speedups 348
17.2 Tkinter performance 350
17.3 Python techniques 352
17.4 Application profiling 357
17.5 Python extensions 359
17.6 Summary 360

Current computer systems have a great capability to support interpreter-based applications such as the Python/Tkinter applications that are presented in this book. This chapter provides both arguments to refute skeptical readers and evidence to support converted readers; it includes case studies to illustrate real-world applications. Since Tkinter is a good example of how effective C extensions to Python can be, I’ll introduce extension-building methods to mitigate adverse performance for complex applications.

17.1 Everyday speedups

If you are conscientious, there is no reason for Python to perform badly. Unfortunately, you can do many things to guarantee that your application will not present the user with acceptable performance and responsiveness. However, you may be able to produce Python programs that rival the performance of compiled C++ if you work hard to avoid a number of key problem areas.