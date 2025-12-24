---
source_image: page_285.png
page_number: 285
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.83
tokens: 8717
characters: 2442
timestamp: 2025-12-24T00:39:43.433257
finish_reason: stop
---

Вот текст кода с комментариями, объясняющими основные части:

```python
def arrowMove1(self, event):
    newA = (self.x2+5-int(self.canvas.canvasx(event.x)))/10
    if newA < 0: newA = 0
    if newA > 25: newA = 25
    if newA != self.a:
        self.canvas.move("box1", 10*(self.a-newA), 0)
        self.a = newA

def arrowMove2(self, event):
    newB = (self.x2+5-int(self.canvas.canvasx(event.x)))/10
    if newB < 0: newB = 0
    if newB > 25: newB = 25
    newC = (self.y+5-int(self.canvas.canvasx(event.y)+ \
        5*self.width))/10
    if newC < 0: newC = 0
    if newC > 20: newC = 20
    if newB != self.b or newC != self.c:
        self.canvas.move("box2", 10*(self.b-newB),
            10*(self.c-newC))
        self.b = newB
        self.c = newC

def arrowMove3(self, event):
    newW = (self.y+2-int(self.canvas.canvasx(event.y)))/5
    if newW < 0: newW = 0
    if newW > 20: newW = 20
    if newW != self.width:
        self.canvas.move("box3", 0, 5*(self.width-newW))
        self.width = newW

def arrowSetup(self):
    tags = self.canvas.gettags(CURRENT)
    cur = None
    if 'box' in tags:
        for tag in tags:
            if len(tag) == 4 and tag[:3] == 'box':
                cur = tag
                break
    self.canvas.delete(ALL)
    self.canvas.create_line(self.x1, self.y, self.x2, self.y,
        width=10*self.width,
        arrowshape=(10*self.a, 10*self.b, 10*self.c),
        arrow='last', fill=self.bigLine)
    xtip = self.x2-10*self.b
    deltaY = 10*self.c+5*self.width
    self.canvas.create_line(self.x2, self.y, xtip, self.y+deltaY,
        self.x2-10*self.a, self.y, xtip, self.y-deltaY,
        self.x2, self.y, width=2, capstyle='round',
        joinstyle='round')
    self.canvas.create_rectangle(self.x2-10*self.a-5, self.y-5,
        self.x2-10*self.a+5, self.y+5,
        fill=self.boxFill, outline='black',
        tags=('box1', 'box'))
    self.canvas.create_rectangle(xtip-5, self.y-deltaY-5,
        xtip+5, self.y-deltaY+5,
        fill=self.boxFill, outline='black',
```

Комментарии к частям кода:

2. Функции `arrowMove1`, `arrowMove2` и `arrowMove3` обновляют позиции объектов на холсте в зависимости от текущей мыши.
3. Функция `arrowSetup` находит и обновляет объекты с тегами 'box', создает линию с наконечником стрелки и рисует прямоугольники вокруг объектов.

4. Внутри функции `arrowSetup` создается линия с наконечником стрелки и рисуются прямоугольники вокруг объектов.