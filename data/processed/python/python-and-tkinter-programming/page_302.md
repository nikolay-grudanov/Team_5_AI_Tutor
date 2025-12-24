---
source_image: page_302.png
page_number: 302
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.77
tokens: 8368
characters: 1268
timestamp: 2025-12-24T00:39:56.105269
finish_reason: stop
---

canvas = Canvas(root, width=450, height=300, bg = 'white')
canvas.pack()

Button(root, text='Quit', command=root.quit).pack()

canvas.create_line(100,250,400,250, width=2)
canvas.create_line(100,250,100,50, width=2)

for i in range(11):
    x = 100 + (i * 30)
    canvas.create_line(x,250,x,245, width=2)
    canvas.create_text(x,254, text='%d' % (10*i), anchor=N)

for i in range(6):
    y = 250 - (i * 40)
    canvas.create_line(100,y,105,y, width=2)
    canvas.create_text(96,y, text='%5.1f' % (50.*i), anchor=E)

for x,y in [(12, 56), (20, 94), (33, 98), (45, 120), (61, 180),
            (75, 160), (98, 223)]:
    x = 100 + 3*x
    y = 250 - (4*y)/5
    canvas.create_oval(x-6,y-6,x+6,y+6, width=1,
                      outline='black', fill='SkyBlue2')

root.mainloop()

Code comments

① Here we add the ticks and labels for the x-axis. Note that the values used are hard-coded—we have made little provision for reuse!

    for i in range(11):
        x = 100 + (i * 30)
        canvas.create_line(x,250,x,245, width=2)
        canvas.create_text(x,254, text='%d' % (10*i), anchor=N)

Notice how we have set this up to increment \( x \) in units of 10.

![Simple two-dimensional graph](https://i.imgur.com/3Q5z5QG.png)

Figure 11.1 Simple two-dimensional graph