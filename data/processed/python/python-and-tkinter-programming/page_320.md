---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.31
tokens: 8469
characters: 2040
timestamp: 2025-12-24T00:40:33.412239
finish_reason: stop
---

Вот текст программы, представленный на странице:

```python
lasthv = self.maxY*self.yfactor
xadj    = float(self.xincr)/4.0
lowv    = self.lowThresh*self.yfactor
for datum in rowdata:
    lside = datum*self.yfactor
    color = self.spectrum[cidx]
    if datum <= self.lowThresh:
        color = self.transform(color, 0.8)
    elif datum >= self.highThresh:
        color = self.transform(color, 1.2)

    self.canvas.create_polygon(rootx, rooty, rootx, rooty-lside,
        rootx-self.hrowoff, rooty-lside+self.vrowoff,
        rootx-self.hrowoff, rooty+self.vrowoff,
        rootx, rooty, fill=color, outline=color,
        width=self.xincr)
    base = min(min(lside, lasthv), lowv)
    self.canvas.create_line(rootx-xadj, rooty-lside,
        rootx-xadj-self.hrowoff, rooty-lside+self.vrowoff,
        rootx-xadj-self.hrowoff, rooty+self.vrowoff-base,
        fill='black', width=1)
    lasthv = lowv = lside

    cidx = cidx + 1
    rootx = rootx + self.xincr

def makeData(self, number, min, max):
    import random
    data = []
    for i in range(number):
        data.append(random.choice(range(min, max)))
    return data

def demo(self):
    for i in range(self.rows):
        data = self.makeData(100, 4, 99)
        self.plotData(i, data)
        self.root.update()

def close(self):
    self.quit()

def createInterface(self):
    AppShell.AppShell.createInterface(self)
    self.createButtons()
    self.initData()
    self.createBase()

if __name__ == '__main__':
    graph = Graph3D()
    graph.root.after(100, graph.demo)
    graph.run()
```

Эта программа создает интерактивный график с использованием библиотеки AppShell и модуля `random`. В ней реализованы следующие функции:

1. `makeData`: генерирует случайные числа в заданном диапазоне.
2. `demo`: генерирует данные и отображает их на графике.
3. `close`: закрывает окно программы.
4. `createInterface`: создает интерфейс программы.
5. `__main__`: запускает программу при ее выполнении.

Программа также использует методы `plotData` и `update` для обновления графика.