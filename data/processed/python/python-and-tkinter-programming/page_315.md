---
source_image: page_315.png
page_number: 315
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.19
tokens: 8482
characters: 2280
timestamp: 2025-12-24T00:40:17.435868
finish_reason: stop
---

Вот текст программы с комментариями и объяснениями:

```python
plot3.py

# --- Code Removed ---------------------------------------------------------------

class GraphPie(GraphPoints):
    def __init__(self, points, **attr):
        GraphPoints.__init__(self, points, attr)

        _attributes = {'color': 'black',
                       'width': 1,
                       'fillcolor': 'yellow',
                       'size': 2,
                       'fillstyle': '',
                       'outline': 'black'}

    def draw(self, canvas, multi):
        width = self.attributes['width']
        fillstyle = self.attributes['fillstyle']
        outline = self.attributes['outline']
        colors = Pmw.Color.spectrum(len(self.scaled))  # 1
        arguments = (canvas,)

        x1 = string.atoi(canvas.cget('width'))
        y1 = string.atoi(canvas.cget('height'))
        adj = 0
        if multi: adj = 15
        xy = 25+adj, 25+adj, x1-25-adj, y1-25-adj
        xys = 25+adj, 25+adj+10, x1-25-adj, y1-25-adj+10
        tt = 0.0
        i = 0
        for point in self.points:
            tt = tt + point[1]
        start = 0.0
        if not x1 == y1:
            canvas.create_arc(xys, start=0.0, extent=359.99,
                              fill='gray60', outline=outline,
                              style='pieslice')

        for point in self.points:
            x1, y1 = point
            extent = (y1/tt)*360.0
            canvas.create_arc(xy, start=start, extent=extent,
                              fill=colors[i], width=width,
                              outline=outline, stipple=fillstyle,
                              style='pieslice')
            start = start + extent
            i = i+1

class GraphObjects:
    def __init__(self, objects):
        self.objects = objects
        self.multiple = len(objects)-1  # 5

# --- Code Removed ---------------------------------------------------------------
```

Объяснения шагов:

1. Создание спектра цветов для каждого сегмента пирога.
2. Вычисление начальных координат и размеров окна для рисования.
3. Рисование внешнего круга (сегментов пирога) с серым заполнением.
4. Рисование внутренних сегментов пирога с выбранными цветами.
5. Инициализация класса `GraphObjects` с подсчетом количества объектов.