---
source_image: page_114.png
page_number: 114
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.22
tokens: 8436
characters: 2343
timestamp: 2025-12-24T00:34:34.501636
finish_reason: stop
---

Button(master, text='Undo',
    state='disabled').grid(row=13, column=6)

Button(master, text='Apply',
    state='disabled').grid(row=13, column=7)
Button(master, text='Reset',
    state='disabled').grid(row=14, column=6)
Button(master, text='Done',
    command=self.exit).grid(row=14, column=7)

# --- Code Removed ---------------------------------------------------------------

root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
root.title('Image Enhancement')
imgEnh = Enhancer(root, sys.argv[1])
root.mainloop()

Code comments

1 This example uses the Python Imaging Library (PIL) to create, display, and enhance images. See “Python Imaging Library (PIL)” on page 626 for references to documentation supporting this useful library of image methods.

2 Although it’s not important in illustrating the grid manager, I left some of the PIL code in place to demonstrate how it facilitates handling images. Here, in the constructor, we open the master image and create a thumbnail within the bounds specified. PIL scales the image appropriately.
    self.masterImg = Image.open(imgfile)
    self.masterImg.thumbnail((150, 150))

3 Next we create a copy of the image and create a Tkinter PhotoImage placeholder for each of the images in the 3x3 grid.

4 Inside a double for loop we create a Label and place it in the appropriate cell in the grid, adding rowspan and colspan options.
    lbl = Label(master, image=self.imgs[i])
    lbl.grid(row=r*5, column=c*2,
        rowspan=5, colspan=2, sticky=NSEW, padx=5, pady=5)
    Note that in this case the sticky option attaches the images to all sides of the grid so that the grid is sized to constrain the image. This means that the widget will stretch and shrink as the overall window size is modified.

5 Similarly, we grid a label with a different background, using the sticky option to fill all of the available cell.
    Label(master, text='Enhance', bg='gray70').grid(row=5, column=6,
        colspan=2, sticky=NSEW)

6 The Pmw RadioSelect widget is placed in the appropriate cell with appropriate spans:
    self.radio = Pmw.RadioSelect(master, labelfpos = None,
        buttontype = 'radiobutton', orient = 'vertical',
        command = self.selectFunc)
    self.radio.grid(row=6, column=6, rowspan=4, colspan=2)

7 Finally, we place the Button widgets in their allocated cells.