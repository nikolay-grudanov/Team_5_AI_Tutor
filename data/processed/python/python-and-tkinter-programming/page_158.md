---
source_image: page_158.png
page_number: 158
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.86
tokens: 8457
characters: 2350
timestamp: 2025-12-24T00:35:54.879233
finish_reason: stop
---

centerx+r, centery+r,
    fill=bg, outline="")
self.canv.pack(side="top", fill='x', expand='no')

class Nut(Frame, HexNut):
    def __init__(self, master, outside=70, inset=8, frame=1, mount=1,
                 bg="gray50", nutbase=Color.CHROME, top=NUT_FLAT):
        Frame.__init__(self)
        HexNut.__init__(self, master=master, outside=outside,
                        inset=inset, frame=frame, mount=mount,
                        bg=bg, nutbase=nutbase, top=top)

class TestNuts(Frame, GUICommon):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.pack()
        self.make_widgets()
    def make_widgets(self):
        # List of Metals to create
        metals = [Color.BRONZE, Color.CHROME, Color.BRASS]
        # List of nut types to display,
        # with sizes and other attributes
        nuts = [(70, 14, NUT_POINT, 0), (70, 10, NUT_FLAT, 1),
                (40, 8, NUT_POINT, 0), (100, 16, NUT_FLAT, 1)]
        # Iterate for each metal type
        for metal in metals:
            mframe = Frame(self, bg="slategrey2")
            mframe.pack(anchor=N, expand=YES, fill=X)
            # Iterate for each of the nuts
            for outside, inset, top, mount in nuts:
                Nut(mframe, outside=outside, inset=inset,
                    mount=mount, nutbase=metal,
                    bg="slategrey2",
                    top=top).frame.pack(side=LEFT,
                        expand=YES,
                        padx=1, pady=1)

if __name__ == '__main__':
    TestNuts().mainloop()

Note Another way of handling variable data: In Example 7_2.py, we used a mechanism to allow us to draw the vertices of the polygon used for the arrowheads. In this example we employ another technique which will be used repeatedly in other examples. Because of the relative complexity of the polygon used to depict the hex nut and the fact that we have to calculate the vertices for both the point and flat forms of the nut, we use the setattr function. This allows us to set the value of an attribute of an object using a reference to the object and a string representation of the attribute.

7.2.2 Creating a switch class

It’s time for something more interesting than LEDs and nuts. Once you get started creating classes it really is hard to stop, so now let’s create some switches. Although these could be