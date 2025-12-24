---
source_image: page_307.png
page_number: 307
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.32
tokens: 8336
characters: 2085
timestamp: 2025-12-24T00:40:00.111379
finish_reason: stop
---

Code comments

1 The GraphPoints class defines the points and attributes of a single plot. As you will see later, the attributes that are processed by the constructor vary with the type of line style. Note that the self._attributes definitions are a requirement for subclasses.

2 boundingBox returns the top-left and bottom-right coordinates by scanning the coordinates in the points data. The convenience functions are in utils.py.

3 fitToScale modifies the coordinates so that they fit within the scale determined for all of the lines in the graph.
    def fitToScale(self, scale=(1,1), shift=(0,0)):
        self.scaled = []
        for x,y in self.points:
            self.scaled.append((scale[0]*x)+shift[0],\
                (scale[1]*y)+shift[1])
    Note that we supply tuples for scale and shift. The first value is for \( x \) and the second is for \( y \).

4 The GraphLine class defines methods to draw lines from the available coordinates.

5 The draw method first extracts the appropriate arguments from the attributes dictionary.

6 Depending on whether we are doing smoothing, we supply start-end-coordinates for line segments (unsmoothed) or a sequence of coordinates (smoothed).

7 We then apply the arguments and the keywords to the canvas Line method. Remember that the format of the Line arguments is really:
    Line(*args, **keywords)

8 GraphSymbols is similar to GraphLine, but it outputs a variety of filled shapes for each of the \( x \)-\( y \) coordinates.

9 The draw method calls the appropriate marker routine through the generic _drawmarkers method:
    self._drawmarkers(canvas, self.scaled, marker, color,
        fillstyle, fillcolor, size)

10 _drawmarkers evaluates the selected marker method, and then it builds a list of the symbols that are created.
    f = eval('self._'+marker)
    for xc, yc in coords:
        id = f(c, xc, yc, outline=color, size=size,
            fill=fillcolor, fillstyle=fillstyle)

11 I have included just one of the shapes that can be drawn by the graph widget. The full set are in the source code available online.