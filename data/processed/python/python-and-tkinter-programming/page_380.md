---
source_image: page_380.png
page_number: 380
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.65
tokens: 8190
characters: 1278
timestamp: 2025-12-24T00:41:57.598792
finish_reason: stop
---

with:

import time, string
start = time.time()

asct      = time.asctime
ltime     = time.localtime
now       = time.time
lower     = string.lower
for i in range(5000):
    strtime = asct(ltime(now()))
    lname = lower('UPPER')

print time.time() - start

Although the second form has more code, it runs a little faster. In a real application with reasonable constructs, the improvement can be worthwhile.

17.3.5 Use local variables

Now, there’s a contradiction! Earlier I was encouraging you not to use local variables, but if you do it right, you can get another performance boost, because *local* variables are accessed faster than *global* variables.

If we recode the last example to use a function so that the variables are local, we see another small performance boost:

import time, string
start = time.time()

def local():
    asct      = time.asctime
    time      = time.localtime
    now       = time.time
    lower     = string.lower

    for i in range(20000):
        strtime = asct(ltime(now()))
        lname = lower('UPPER')
ocal()
print time.time() - start

Similarly, you may improve performance if you do a method lookup outside a loop.
Compare:

r = []
for item in biglist:
    r.append(item)

with:

r = []
a = r.append
for item in biglist:
    a(item)