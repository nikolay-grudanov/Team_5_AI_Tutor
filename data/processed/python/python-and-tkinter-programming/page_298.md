---
source_image: page_298.png
page_number: 298
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.38
tokens: 8290
characters: 1691
timestamp: 2025-12-24T00:39:47.533452
finish_reason: stop
---

float(x)/float(self.width)*self.range,
    self.origin.imag - \
        float(y) / float(self.height)*self.range)
    # calculate z = (z +k) * (z + k) over and over
    for iteration in range(self.depth):
        real_part = z.real + k.real
        imag_part = z.imag + k.imag
        del z
        z = complex(real_part * real_part - imag_part * \
            imag_part, 2 * real_part * imag_part)
        distance = z.real * z.real + z.imag * z.imag
        if distance >= self.maxDistance:
            cidx = int(distance % self.ncolors)
            self.pixel(x, y, cidx)
            break
    self.updateProgress(y)
self.updateProgress(self.height, self.height)
self.im.putpalette(self.rgb.getpalette())
self.im.save("out.gif")
self.img = PhotoImage(file="out.gif")
self.label['image'] = self.img

def pixel(self, x, y, color):
    self.d.setink(color)
    self.d.point((x, y))

def save(self):
    self.save = TRUE
    self.updateMessageBar('Saved as "out.gif"')

def close(self):
    if not self.save:
        os.unlink("out.gif")
    self.quit()

def createInterface(self):
    AppShell.AppShell.createInterface(self)
    self.createButtons()
    self.initData()
    self.createDisplay()

if __name__ == '__main__':
    fractal = Fractal()
    fractal.root.after(10, fractal.createImage())
    fractal.run()

Code comments
① The Palette class is responsible for creating a random palette (loadpalette) and generating an RGB list for inclusion in the GIF image (getpalette).
② We create a new image, specifying pixel mode (P), and we instantiate the ImageDraw class, which provides basic drawing functions to the image. We fill the image with black, initially with the setfill method.