---
source_image: page_223.png
page_number: 223
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.58
tokens: 8181
characters: 1303
timestamp: 2025-12-24T00:37:29.222316
finish_reason: stop
---

self.coords = coords
self.ref    = ref

2 Detecting when a button press occurs within a region is a simple test:
    def inside(self, x, y):
        isInside = 0
        if self.coords[0][0] <= x <= self.coords[1][0] and \
            self.coords[0][1] <= y <= self.coords[1][1]:
            isInside = 1
        return isInside

3 When we attempt to find a region, we first look in the cache that is accumulated from previous lookups:
    def getRegion(self, x, y):
        try:
            return self.cache[(x,y)]
        except KeyError:
            for region in self.regions:
                if region.inside(x, y) == 1:
                    self.cache[(x,y)] = region
                    return region.ref

Figure 8.16 shows calculator.py in action.

4 If it is not in the cache, we have to search each of the regions in turn; we cache the map if we find it:

![A screenshot of a Texas Instruments TI-82 calculator running on a computer screen](./images/calculator.gif)

Figure 8.16 Running calculator.py

8.8 Summary

This chapter has covered several types of forms and dialogs, ranging from simple fill-in-the-blank dialogs through browsers and wizards to image-mapping techniques. I hope that you will find sufficient material here so you can create forms appropriate for your own applications.