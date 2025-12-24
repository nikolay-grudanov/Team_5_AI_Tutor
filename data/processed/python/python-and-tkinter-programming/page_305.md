---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.28
tokens: 8130
characters: 1094
timestamp: 2025-12-24T00:39:50.349786
finish_reason: stop
---

Figure 11.4 Simple graph widget: lines only

class GraphPoints:
    def __init__(self, points, attr):
        self.points = points
        self.scaled = self.points
        self.attributes = {}
        for name, value in self._attributes.items():
            try:
                value = attr[name]
            except KeyError: pass
            self.attributes[name] = value

    def boundingBox(self):
        return minBound(self.points), maxBound(self.points)

    def fitToScale(self, scale=(1,1), shift=(0,0)):
        self.scaled = []
        for x,y in self.points:
            self.scaled.append((scale[0]*x)+shift[0],\
                (scale[1]*y)+shift[1])

class GraphLine(GraphPoints):
    def __init__(self, points, **attr):
        GraphPoints.__init__(self, points, attr)
        _attributes = {'color': 'black',
                       'width': 1,
                       'smooth': 0,
                       'splinesteps': 12}

    def draw(self, canvas):
        color = self.attributes['color']
        width = self.attributes['width']
        smooth = self.attributes['smooth']