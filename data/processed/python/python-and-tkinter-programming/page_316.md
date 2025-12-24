---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.17
tokens: 8591
characters: 2113
timestamp: 2025-12-24T00:40:25.657268
finish_reason: stop
---

def draw(self, canvas):
    for object in self.objects:
        object.draw(canvas, self.multiple) ⑥

# --- Code Removed ---------------------------------------------------------------

if __name__ == '__main__':
    root = Tk()
    root.title('Graph Widget - Piechart')

    pie1 = GraphPie([(0,21),(1,77),(2,129),(3,169),(4,260),(5,377),
                     (6,695),(7,434)])

    pie2 = GraphPie([(0,5),(1,22),(2,8),(3,45),(4,22),
                     (5,9),(6,40),(7,2),(8,56),(9,34),
                     (10,51),(11,43),(12,12),(13,65),(14,22),
                     (15,15),(16,48),(17,16),(18,45),(19,19),
                     (20,33)], fillstyle='gray50', width=2)

    pie3 = GraphPie([(0,5),(1,22),(2,8),(3,45),(4,22),
                     (5,9),(6,40),(7,2),(8,56),(9,34),
                     (10,51),(11,43),(12,12),(13,65),(14,22),
                     (15,15),(16,48),(17,16),(18,45),(19,19),
                     (20,33)])

    pieline4 = GraphLine([(0,21),(1,77),(2,129),(3,169),(4,260),
                          (5,377),(6,695),(7,434)], width=3)
    pielines4 = GraphSymbols([(0,21),(1,77),(2,129),(3,169),(4,260),
                              (5,377),(6,695),(7,434)],
                             marker='square', fillcolor='yellow')

    graphObject1 = GraphObjects([pie1])
    graphObject2 = GraphObjects([pie2])
    graphObject3 = GraphObjects([pie3])
    graphObject4 = GraphObjects([pie1, pieline4, pielines4])

    f1 = Frame(root)
    f2 = Frame(root)

    graph1= GraphBase(f1, 300, 300, relief=SUNKEN, border=2)
    graph1.pack(side=LEFT, fill=BOTH, expand=YES)
    graph1.draw(graphObject1)

# --- Code Removed ---------------------------------------------------------------

Code comments

① The pie chart implementation assigns a spectrum of colors to the slices of the pie, one color value per slice. This gives a reasonable appearance for a small number of slices.

    colors = Pmw.Color.spectrum(len(self.scaled))

② This code adjusts the position of the pie chart for cases where we are displaying the pie chart along with other graphs:

    adj = 0
    if multi: adj = 15