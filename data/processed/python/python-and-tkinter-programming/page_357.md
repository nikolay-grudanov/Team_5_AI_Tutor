---
source_image: page_357.png
page_number: 357
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.13
tokens: 8107
characters: 661
timestamp: 2025-12-24T00:41:09.864242
finish_reason: stop
---

That’s not what I meant! Decrementing 1 pixel at a time will not work!. If you look at the line of code before the print statement, you will see that I meant to multiply by 40 not just add 40. So let’s make the changes and run debug5.py:

C:> python debug5.py

No errors, again, but not the result I expected (see figure 15.3) the “blobs” are supposed to be on the line. Let’s look at the bit of code that’s supposed to plot the points:

scaled = []
for x,y in [(12, 56), (20, 94), (33, 98), (45, 120), (61, 180),
            (75, 160), (98, 223)]:
    scaled.append(100 + 3*x, 250 - (4*y)/5)

Figure 15.2 Debugging stage two

Figure 15.3 Debugging, stage three