---
source_image: page_299.png
page_number: 299
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.17
tokens: 8170
characters: 1167
timestamp: 2025-12-24T00:39:36.789010
finish_reason: stop
---

self.im = Image.new("P", (self.width, self.height), 0)
self.d = ImageDraw.ImageDraw(self.im)
self.d.setfill(0)

3 At the center of the computational loop, we select a color and set the corresponding pixel to that color.

    cidx = int(distance % self.ncolors)
    self.pixel(x, y, cidx)

4 When complete, we add the palette to the image, save it as a GIF file, and then load the image as a Tkinter PhotoImage.

    self.im.putpalette(self.rgb.getpalette())
    self.im.save("out.gif")
    self.img = PhotoImage(file="out.gif")
    self.label['image'] = self.img

5 The pixel method is very simple. We set the color of the ink and place the pixel at the specified x, y coordinate.

    def pixel(self, x, y, color):
        self.d.setink(color)
        self.d.point((x, y))

Running fractal.py on a moderately fast workstation will generate an 800×600 pixel image in about 2-3 minutes. If you are interested, you will find slowfractal.py online. This version is written using Tkinter canvas methods and it takes considerably longer to complete.

![Fractal Demonstration window showing a colorful fractal image](../images/ch10_13.png)

Figure 10.13 Generating fractals