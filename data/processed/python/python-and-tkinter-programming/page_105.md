---
source_image: page_105.png
page_number: 105
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.67
tokens: 8325
characters: 1853
timestamp: 2025-12-24T00:34:19.049232
finish_reason: stop
---

Next, the slave is positioned within the parcel. If the available space results in a smaller parcel than the size of the slave, it may be squeezed or cropped, depending on the requested options. In this example, the slave is smaller than the available space and its height is increased to fill the available parcel. Figure 5.1(4) shows the available space for more slaves. In figure 5.1(5) we pack another slave with side=LEFT and fill=BOTH options. Again, the available parcel is larger than the size of the slave (figure 5.1(6)) so the widget is grown to fill the available space. The effect is shown in figure 5.1(7).

Here is a simple example of using the pack method, shown in figure 5.2:

Example_5_1.py

from Tkinter import *

class App:
    def __init__(self, master):
        Button(master, text='Left').pack(side=LEFT)
        Button(master, text='Center').pack(side=LEFT)
        Button(master, text='Right').pack(side=LEFT)

root = Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Pack - Example 1")
display = App(root)
root.mainloop()

Code comments

① The side=LEFT argument tells the Packer to start locating the widgets in the packing list from the left-hand side of the container. In this case the container is the default Toplevel shell created by the Tk initializer. The shell shrinks or expands to enclose the packed widgets.

Figure 5.3 Packer accommodates requested widget sizes

Enclosing the widgets in a frame has no effect on the shrink-wrap effect of the Packer. In this example (shown in figure 5.3), we have increased the length of the text in the middle button and the frame is simply stretched to the requested size.

Example_5_2.py

fm = Frame(master)
Button(fm, text='Left').pack(side=LEFT)
Button(fm, text='This is the Center button').pack(side=LEFT)
Button(fm, text='Right').pack(side=LEFT)
fm.pack()