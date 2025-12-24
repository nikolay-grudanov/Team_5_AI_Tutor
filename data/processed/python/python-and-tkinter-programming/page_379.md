---
source_image: page_379.png
page_number: 379
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.90
tokens: 8378
characters: 1829
timestamp: 2025-12-24T00:42:11.473153
finish_reason: stop
---

longString = part1 + ' ' + part2 + ' ' + part3

It’s more efficient to do this with formatted strings:

longString = '%s %s %s' % (part1, part2, part3)

It is much faster, because all of the work happens in C code. Depending on the type of concatenation you are doing, you should see at least 25 percent improvement using format strings.

17.3.3 Getting nested loops right

This point has been mentioned before, and most seasoned programmers have encountered this issue at least once, but it is still worth mentioning again. When you have to iterate over a multi-dimensional object, make sure that the less-rapidly changing index is to the outside of the loop. Let’s look at a two-dimensional array with 100 columns and 25,000 rows. It really does matter which way you access it:

l = []
for row in range(25000):
    for col in range(100):
        l.append('%d.%d' % (row, col))

runs about 20 percent slower than:

l = []
for col in range(100):
    for row in range(25000):
        l.append('%d.%d' % (row, col))

However Guido van Rossum showed me this trick which beats that one by another 20 percent:

rowrange = range(100)
for col in range(25000):
    for row in rowrange:
        l.append('%d.%d' % (row, col))

This achieves the performance boost because integers in the range -1 to 100 are cached and are considerably faster. 25000 loops from 0 to 99 result in 24999 integer allocations, whereas 100 loops from 0 to 24999 result in 100*24999 allocations.

17.3.4 Eliminate module references

Every time you use a module reference, you incur a small overhead. If the references are within a loop, then some benefits can be gained. Contrast:

import time, string
start = time.time()

for i in range(5000):
    strftime = time.asctime(time.localtime(time.time()))
    lname = string.lower('UPPER')

print time.time() - start