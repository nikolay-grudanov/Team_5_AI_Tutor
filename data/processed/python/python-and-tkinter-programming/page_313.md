---
source_image: page_313.png
page_number: 313
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.73
tokens: 8656
characters: 2046
timestamp: 2025-12-24T00:40:26.858590
finish_reason: stop
---

(6,77),(7,125),(8,220),(9,550),(10,560),(11,0)],
color='green', size=10)

line3 = GraphBars([(0,0),(1,145),(2,151),(3,147),(4,22),(5,31),
    (6,77),(7,125),(8,220),(9,550),(10,560),(11,0)],
    color='blue', size=10)
line3a = GraphLine([(1,145),(2,151),(3,147),(4,22),(5,31),
    (6,77),(7,125),(8,220),(9,550),(10,560)],
    color='black', width=1, smooth=0)

line4 = GraphBars([(0,0),(1,145),(2,151),(3,147),(4,22),(5,31),
    (6,77),(7,125),(8,220),(9,550),(10,560),(11,0)],
    color='blue', size=10)
line4a = GraphLine([(1,145),(2,151),(3,147),(4,22),(5,31),
    (6,77),(7,125),(8,220),(9,550),(10,560)],
    color='black', width=2, smooth=1)

graphObject  = GraphObjects([linela, line1])
graphObject2 = GraphObjects([line2])
graphObject3 = GraphObjects([line3a, line3])
graphObject4 = GraphObjects([line4, line4a])

f1 = Frame(root)
f2 = Frame(root)

graph  = GraphBase(f1, 500, 350, relief=SUNKEN, border=2)
graph.pack(side=LEFT, fill=BOTH, expand=YES)
graph.draw(graphObject, 'automatic', 'automatic')

graph2= GraphBase(f1, 500, 350, relief=SUNKEN, border=2)
graph2.pack(side=LEFT, fill=BOTH, expand=YES)
graph2.draw(graphObject2, 'automatic', 'automatic')

graph3= GraphBase(f2, 500, 350, relief=SUNKEN, border=2)
graph3.pack(side=LEFT, fill=BOTH, expand=YES)
graph3.draw(graphObject3, 'automatic', 'automatic')

graph4= GraphBase(f2, 500, 350, relief=SUNKEN, border=2)
graph4.pack(side=LEFT, fill=BOTH, expand=YES)
graph4.draw(graphObject4, 'automatic', 'automatic')

f1.pack()
f2.pack()

# --- Code Removed ---------------------------------------------------------------

Code comments

1 There’s not much to explain here; I think that the changes are fairly self-explanatory. However, anchor is worthy of a brief note. In the case of the sine/cosine curve, we want the bars to start on zero. This is the anchor value. If we don’t set it, we’ll draw from the x-axis regardless of its value.

self.anchor = scale[1]*self.attributes.get('anchor', 0.0) + shift[1]

2 The bargraph has some slightly different options that need to be set.