---
source_image: page_308.png
page_number: 308
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.04
tokens: 8358
characters: 1958
timestamp: 2025-12-24T00:40:04.309961
finish_reason: stop
---

plot.py (continued)

def _dot(self, c, xc, yc, ... ):
def _square(self, c, xc, yc, ... ):
def _triangle(self, c, xc, yc, ... ):
def _triangle_down(self, c, xc, yc, ... ):
def _cross(self, c, xc, yc, ... ):
def _plus(self, c, xc, yc, ... ):

# --- Code Removed ---------------------------------------------------------------

class GraphObjects:
    def __init__(self, objects):
        self.objects = objects

    def boundingBox(self):
        c1, c2 = self.objects[0].boundingBox()
        for object in self.objects[1:]:
            c1o, c2o = object.boundingBox()
            c1 = minBound([c1, c1o])
            c2 = maxBound([c2, c2o])
        return c1, c2

    def fitToScale(self, scale=(1,1), shift=(0,0)):
        for object in self.objects:
            object.fitToScale(scale, shift)

    def draw(self, canvas):
        for object in self.objects:
            object.draw(canvas)

class GraphBase(Frame):
    def __init__(self, master, width, height,
                 background='white', **kw):
        apply(Frame.__init__, (self, master), kw)
        self.canvas = Canvas(self, width=width, height=height,
                             background=background)
        self.canvas.pack(fill=BOTH, expand=YES)
        border_w = self.canvas.winfo_reqwidth() - \
            string.atoi(self.canvas.cget('width'))
        border_h = self.canvas.winfo_reqheight() - \
            string.atoi(self.canvas.cget('height'))
        self.border = (border_w, border_h)
        self.canvas.bind('<Configure>', self.configure)
        self.plotarea_size = [None, None]
        self._setsize()
        self.last_drawn = None
        self.font = ('Verdana', 10)

    def configure(self, event):
        new_width = event.width-self.border[0]
        new_height = event.height-self.border[1]
        width = string.atoi(self.canvas.cget('width'))
        height = string.atoi(self.canvas.cget('height'))
        if new_width == width and new_height == height: