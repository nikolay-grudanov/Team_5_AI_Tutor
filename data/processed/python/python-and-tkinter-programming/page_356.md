---
source_image: page_356.png
page_number: 356
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.11
tokens: 8411
characters: 1720
timestamp: 2025-12-24T00:41:28.468478
finish_reason: stop
---

To start debugging, we have two alternatives: we can put print statements in the code to find out where we last executed successfully, or we can disable the try ... except. To do this, quickly edit the file like this:

    if 1:
#        try:
#-----------------Code removed---------------------------------------------
#        except:
#            print 'An error has occurred!'

Putting in the if 1: and commenting out the except clause means that you don’t have to redo the indentation—which would probably cause even more errors. Now, if you run debug2.py, you’ll get the following result:

C:> python debug2.py
Traceback (innermost last):
    File "debug2.py", line 41, in ?
        main()
    File "debug2.py", line 23, in main
        canvas.create_line(100,y,105,y, width=2)
NameError: y

So, we take a look at the section of code and see the following:

for i in range(6):
    x = 250 - (i + 40)
    canvas.create_line(100,y,105,y, width=2)
    canvas.create_text(96,y, text='%5.1f' % (50.*i), anchor=E)

Okay, it’s my fault! I cut and pasted some of the code and left x as the variable. So I’ll change the x to y and reinstate the try ... except (that’s obviously the only problem!).

Now, let’s run debug3.py:

C:> python debug3.py

No errors, but the screen is nothing like I expect—take a look at figure 15.2! Clearly the y-axis is not being created correctly, so let’s print out the values that are being calculated:

for i in range(6):
    y = 250 - (i + 40)
    print "i=%d, y=%d" %(i, y)
    canvas.create_line(100,y,105,y, width=2)
    canvas.create_text(96,y, text='%5.1f' % (50.*i), anchor=E)

Now run debug4.py:

C:> python debug4.py
i=0, y=210
i=1, y=209
i=2, y=208
i=3, y=207
i=4, y=206
i=5, y=205