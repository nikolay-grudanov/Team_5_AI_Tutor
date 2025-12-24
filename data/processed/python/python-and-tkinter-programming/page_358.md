---
source_image: page_358.png
page_number: 358
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.70
tokens: 8499
characters: 2134
timestamp: 2025-12-24T00:41:35.900782
finish_reason: stop
---

That looks Okay, but let’s check it out:

scaled = []
    for x,y in [(12, 56), (20, 94), (33, 98), (45, 120), (61, 180),
                (75, 160), (98, 223)]:
        s = 100 + 3*x, 250 - (4*y)/5
        print "x,y = %d,%d" % (s[0], s[1])
        scaled.append(s)

Now, run debug6.py:

C:> python debug6.py
x,y - 136,206
x,y - 160,175
x,y - 199,172
x,y - 235,154
x,y - 283,106
x,y - 325,122
x,y - 394,72

Yes, that looks right (blast!). We need to look further:

canvas.create_line(scaled, fill='black', smooth=1)
for xs,ys in scaled:
    canvas.create_oval(x-6,y-6,x+6,y+6, width=1,
                        outline='black', fill='SkyBlue2')

I’ll save you any more pain on this example. Obviously it was contrived and I’m not usually so careless. I meant to use xs and ys as the scaled coordinates, but I used x and y in the canvas.create_oval method. Since I had used x and y earlier, I did not get a NameError, so we just used the last values. I’m sure that you will take my word that if the changes are made, the code will now run!

15.3 How to debug

The ability to debug is really as important as the ability to code. Some programmers have real problems in debugging failing code, particularly when the code is complex. The major skill in debugging is to ignore the unimportant and focus on the important. The secondary skill is to learn how to gain the major skill.

Really, you want to confirm that the code is producing the values you expect and following the paths you expect. This is why using print statements (or using a debugger where appropriate) to show the actual values of variables, pointers and the like is a good idea. Also, putting tracers into your code to show which statements are being executed can quickly help you focus on problem areas.

If you are proficient with an editor such as emacs it is really easy to insert debugging statements into your code. If you have the time and the inclination, you can build your code so that it is ready to debug. Add statements which are only executed when a variable has been set. For example:

...
if debug > 2:
    print('location: var=%d, var2=%s' % (var, var2))