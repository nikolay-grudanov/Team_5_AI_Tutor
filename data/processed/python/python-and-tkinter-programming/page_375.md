---
source_image: page_375.png
page_number: 375
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.91
tokens: 8436
characters: 2736
timestamp: 2025-12-24T00:42:04.016172
finish_reason: stop
---

Alternatively, you can pass a .pyc or .pyo file to the Python interpreter directly. On UNIX, the following script may be used:

#!/bin/sh
exec python script.pyo ${1+"$*"}

This technique may not be very effective for Win32 since the time taken to launch a batch file and start the Python interpreter may negate the increase in speed when using a .pyo file. However, if you set Explorer’s file type to execute Python when a .py file is double-clicked, then you do not need a batch file at all.

17.1.2 Using the Python optimizer

If you invoke Python with the optimize command-line option set (-O), the compiler will generate optimized bytecode. This means that the bytecode is optimized to run faster. It does so by eliminating some of the bytecode instructions (eliminating SET_LINENO from function calls and suppressing assert statements). It really depends on how many function calls and assert statements are in your code. However, it is still worth using this option to increase your application’s invocation speed even a few percentage points.

17.1.3 Examining code

Python has an unusual property: if you leave new code alone for a couple of days you can usually return to it and reduce its size. There are often opportunities to collapse code, flatten loops, or eliminate unnecessary operations. What you are doing is reducing the number of bytecode operations. This is generally possible without reducing the ability to maintain the code, so it is worth doing.

17.2 Tkinter performance

The performance of a GUI can make or break an application. Users have subconscious expectations about how fast something should happen. Even simple interfaces, such as you might see on an Automated Teller Machine (ATM), have response times set for various operations (usually feedback for every keypress, such as a beep or acknowledgment is less than two seconds and transactions are completed within ten seconds). Consistency is also important. If a GUI normally does something in one second, a user will often react adversely if it occasionally takes two or three seconds—often prompting them to repeat the button press or key entry.

However, never try to optimize an application before your application is running. What you think may be slow code might perform well in the final version. If a loop is only executed a small number of times, the effort to improve its performance may result in your overlooking more important problems.

17.2.1 Keep it short!

If you can reduce the number of lines of code in your program without reducing someone’s ability to maintain it, then you will improve performance. Take a look at this simple example:

self.label = Label(frame, text='Password:', fg='black')
self.label.pack(side=LEFT, padx=10)