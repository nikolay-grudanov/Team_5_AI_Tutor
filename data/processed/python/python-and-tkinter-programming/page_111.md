---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.44
tokens: 8213
characters: 1483
timestamp: 2025-12-24T00:34:18.623592
finish_reason: stop
---

5.3 Grid

Many programmers consider the Grid geometry manager the easiest manager to use. Personally, I don’t completely agree, but you will be the final judge. Take a look at figure 5.17. This is a fairly complex layout task to support an image editor which uses a “by example” motif. Laying this out using the Packer requires a hierarchical approach with several nested Frames to enclose the target widgets. It also requires careful calculation of padding and other factors to achieve the final layout. It is much easier using the Grid.

![An image enhancer using Grid geometry management](image_1.png)
Figure 5.16 An image enhancer using Grid geometry management

![A dialog laid out using Grid](image_2.png)
Figure 5.17 A dialog laid out using Grid

Before we tackle laying out the image editor, let’s take a look at a simpler example. We’ll create a dialog containing three labels with three entry fields, along with OK and Cancel buttons. The fields need to line up neatly (the example is a change-password dialog). Figure 5.18 shows what the Grid manager does for us. The code is quite simple, but I have removed some less-important lines for clarity:

Example_5_14.py

class GetPassword(Dialog):
    def body(self, master):
        self.title("Enter New Password")

        Label(master, text='Old Password:').grid(row=0, sticky=W)
        Label(master, text='New Password:').grid(row=1, sticky=W)
        Label(master, text='Enter New Password Again:').grid(row=2, sticky=W)