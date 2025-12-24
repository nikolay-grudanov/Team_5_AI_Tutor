---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.89
tokens: 8422
characters: 1730
timestamp: 2025-12-24T00:37:40.499055
finish_reason: stop
---

self.iMap.addRegion(((19.0,263.0),(55.0,281.0)), 'alpha')
self.iMap.addRegion(((63.0,263.0),(96.0,281.0)), 'x-t-phi')
self.iMap.addRegion(((105.0,263.0),(134.0,281.0)), 'stat')
# ----- Some lines removed for brevity------------------
self.iMap.addRegion(((24.0,467.0),(54.0,488.0)), 'on')
self.iMap.addRegion(((64.0,468.0),(97.0,486.0)), '0')
self.iMap.addRegion(((104.0,469.0),(138.0,486.0)), '.')
self.iMap.addRegion(((185.0,469.0),(220.0,491.0)), 'enter')

if __name__ == "__main__":
    root = Tk()
    root.title("calculator.gif")
    imageTest = ImageTest(root, width=237, height=513, file="calculator.gif")
    imageTest.root.mainloop()

It’s really quite simple. The image map uses the ImageMap class. This class can be readily extended to support regions other than rectangles:

imagemap.py

class Region:
    def __init__(self, coords, ref):
        self.coords = coords
        self.ref = ref

    def inside(self, x, y):
        isInside = 0
        if self.coords[0][0] <= x <= self.coords[1][0] and \
           self.coords[0][1] <= y <= self.coords[1][1]:
            isInside = 1
        return isInside

class ImageMap:
    def __init__(self):
        self.regions = []
        self.cache = {}

    def addRegion(self, coords, ref):
        self.regions.append(Region(coords, ref))

    def getRegion(self, x, y):
        try:
            return self.cache[(x,y)]
        except KeyError:
            for region in self.regions:
                if region.inside(x, y) == 1:
                    self.cache[(x,y)] = region
                    return region.ref
            return None

Code comments

1 The Region class provides a container for the target regions:
class Region:
    def __init__(self, coords, ref):