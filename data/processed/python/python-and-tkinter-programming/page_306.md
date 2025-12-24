---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.49
tokens: 8514
characters: 2252
timestamp: 2025-12-24T00:40:11.552406
finish_reason: stop
---

Вот текст кода с комментариями, объясняющими основные части:

```python
steps = self.attributes['splinesteps']
arguments = (canvas,)
if smooth:
    for i in range(len(self.points)):
        x1, y1 = self.scaled[i]
        arguments = arguments + (x1, y1)
else:
    for i in range(len(self.points)-1):
        x1, y1 = self.scaled[i]
        x2, y2 = self.scaled[i+1]
        arguments = arguments + (x1, y1, x2, y2)
apply(Line, arguments, {'fill': color, 'width': width,
    'smooth': smooth,
    'splinesteps': steps})

class GraphSymbols(GraphPoints):
    def __init__(self, points, **attr):
        GraphPoints.__init__(self, points, attr)
    _attributes = {'color': 'black',
        'width': 1,
        'fillcolor': 'black',
        'size': 2,
        'fillstyle': '',
        'outline': 'black',
        'marker': 'circle'}
    def draw(self, canvas):
        color = self.attributes['color']
        size = self.attributes['size']
        fillcolor = self.attributes['fillcolor']
        marker = self.attributes['marker']
        fillstyle = self.attributes['fillstyle']
        self._drawmarkers(canvas, self.scaled, marker, color,
            fillstyle, fillcolor, size)
    def _drawmarkers(self, self, c, coords, marker='circle',
        color='black', fillstyle='', fillcolor='', size=2):
        l = []
        f = eval('self._' + marker)
        for xc, yc in coords:
            id = f(c, xc, yc, outline=color, size=size,
                fill=fillcolor, fillstyle=fillstyle)
            if type(id) is type(()):
                for item in id: l.append(item)
            else:
                l.append(id)
        return l
    def _circle(self, c, xc, yc, size=1, fill='',
        outline='black', fillstyle=''):
        id = c.create_oval(xc-0.5, yc-0.5, xc+0.5, yc+0.5,
            fill=fill, outline=outline,
            stipple=fillstyle)
```

Комментарии к ключевым частям кода:

4. Обработка параметров для рисования линии.
5. Обработка параметров для рисования точек.
6. Класс `GraphSymbols` наследует от `GraphPoints`.
7. Метод `__init__` класса `GraphSymbols`.
8. Атрибуты по умолчанию для точек.
9. Метод `draw` класса `GraphSymbols`.
10. Метод `_drawmarkers` класса `GraphSymbols`.
11. Метод `_circle` класса `GraphSymbols`.