---
source_image: page_116.png
page_number: 116
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.48
tokens: 8438
characters: 2343
timestamp: 2025-12-24T00:34:43.041649
finish_reason: stop
---

buttons. It is quite easy to build a little application like this; again, we use PIL to provide support for images.

It would be possible to use pack to lay out the window (and, of course, grid would work if the image spanned most of the columns) but place provides some useful behavior when windows are resized. The Buttons in figure 5.21 are attached to relative positions, which means that they stay in the same relative position as the dimensions of the window change. You express relative positions as a real number with 0.0 representing minimum x or y and 1.0 representing maximum x or y. The minimum values for the axes are conventional for window coordinates with x0 on the left of the screen and y0 at the top of the screen. If you run scrapbook.py, test the effect of squeezing and stretching the window and you will notice how the buttons reposition. If you squeeze too much you will cause the buttons to collide, but somehow the effect using place is more acceptable than the clipping that occurs with pack. Here is the code for the scrapbook.

scrapbook.py

from Tkinter import *
import Image, ImageTk, os

class Scrapbook:
    def __init__(self, master=None):
        self.master = master
        self.frame = Frame(master, width=400, height=420, bg='gray50',
                           relief=RAISED, bd=4)

        self.lbl = Label(self.frame)
        self.lbl.place(relx=0.5, rely=0.48, anchor=CENTER)

        self.images = []
        images = os.listdir("images")

        xpos = 0.05
        for i in range(10):
            Button(self.frame, text='%d' % (i+1), bg='gray10',
                   fg='white', command=lambda s=self, img=i: \
                   s.getImg(img)).place(relx=xpos, rely=0.99, anchor=S)
            xpos = xpos + 0.08
            self.images.append(images[i])

        Button(self.frame, text='Done', command=self.exit,
               bg='red', fg='yellow').place(relx=0.99, rely=0.99, anchor=SE)
        self.frame.pack()
        self.getImg(0)

    def getImg(self, img):
        self.masterImg = Image.open(os.path.join("images",
                                                 self.images[img]))
        self.masterImg.thumbnail((400, 400))
        self.img = ImageTk.PhotoImage(self.masterImg)
        self.lbl['image'] = self.img

    def exit(self):
        self.master.destroy()

root = Tk()