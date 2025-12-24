---
source_image: page_378.png
page_number: 378
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.27
tokens: 8270
characters: 1647
timestamp: 2025-12-24T00:42:03.789338
finish_reason: stop
---

Most of the suggestions in this section are pretty straightforward. You may also find useful suggestions by reading the Python news group (see “Python News Group” on page 626).

17.3.1 Importing modules

You can execute an import statement almost anywhere in your program. Conventionally, most import statements occur at the start of the program. Sometimes you may want to delay the import of a module that is required infrequently until there is a need for it. Python handles repeated imports of the same module properly, but there is a slight cost when this occurs. If possible, avoid repeatedly importing the same module. Let’s look at a hypothetical example:

Example_17_1.py

import time
start = time.time()

def splitter():
    import string
    list = string.split('A B C D E F G H', ' ')

for i in range(123456):
    splitter()

print time.time() - start

Compare this with:

Example_17_2.py

import time
import string

start = time.time()

def splitter():
    list = string.split('A B C D E F G H', ' ')

for i in range(123456):
    splitter()

print time.time() - start

If you run Example_17_1.py and then Example_17_2.py a few times, you will find that Example_17_2.py runs more than twice as fast as Example_17.1.py. By the way, don’t try to do an if not stringLoaded: import string; stringLoaded = TRUE construct within the splitter function. It will not work because of scoping; the string module reference gets removed each time the function returns.

17.3.2 Concatenating strings

Until recent releases of Python, the documentation did not spell out the use of formatted strings, so strings were frequently concatenated like this: