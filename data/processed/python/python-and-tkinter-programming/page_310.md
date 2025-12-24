---
source_image: page_310.png
page_number: 310
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.21
tokens: 8261
characters: 1583
timestamp: 2025-12-24T00:39:59.610852
finish_reason: stop
---

Code comments (continued)

12 The GraphObjects class defines the collection of graph symbologies for each graph. In particular, it is responsible for determining the common bounding box for all of the lines.

13 fitToScale scales each of the lines to the calculated bounding box.

14 Finally, the draw method renders each of the graphs in the composite.

15 GraphBase is the base widget class which contains each of the composites. As you will see later, you may combine different arrangements of graph widgets to produce the desired effect.

16 An important feature of this widget is that it redraws whenever the parent container is resized. This allows the user to shrink and grow the display at will. We bind a configure event to the configure callback.

plot.py (continued)

self.canvas.bind('<Configure>', self.configure)
if __name__ == '__main__':
    root = Tk()
    di = 5.*pi/5.
    data = []
    for i in range(18):
        data.append((float(i)*di,
                     (math.sin(float(i)*di)-math.cos(float(i)*di))))
    line = GraphLine(data, color='gray', smooth=0)
    linea = GraphLine(data, color='blue', smooth=1, splinesteps=500)
    graphObject = GraphObjects([line, linea])
    graph = GraphBase(root, 500, 400, relief=SUNKEN, border=2)
    graph.pack(side=TOP, fill=BOTH, expand=YES)
    graph.draw(graphObject, 'automatic', 'automatic')
    Button(root, text='Clear', command=graph.clear).pack(side=LEFT)
    Button(root, text='Redraw', command=graph.replot).pack(side=LEFT)
    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
    root.mainloop()