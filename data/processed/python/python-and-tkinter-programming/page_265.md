---
source_image: page_265.png
page_number: 265
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.36
tokens: 8501
characters: 2281
timestamp: 2025-12-24T00:38:55.949639
finish_reason: stop
---

Вот текст кода с комментариями, объясняющими основные моменты:

```python
self.radio.add(text)
self.func[text] = func
self.radio.invoke('Rectangle')

def selectFunc(self, tag):
    self.currentFunc = self.func[tag]

def mouseDown(self, event):
    self.currentObject = None
    self.lastx = self.startx = self.canvas.canvasx(event.x)
    self.lasty = self.starty = self.canvas.canvasy(event.y)
    if not self.currentFunc:
        self.selObj = self.canvas.find_closest(self.startx, self.starty)[0]
        self.canvas.itemconfig(self.selObj, width=2)
        self.canvas.lift(self.selObj)

def mouseMotion(self, event):
    self.lastx = self.canvas.canvasx(event.x)
    self.lasty = self.canvas.canvasy(event.y)
    if self.currentFunc:
        self.canvas.delete(self.currentObject)
        self.currentFunc(self.startx, self.starty,
                         self.lastx, self.lasty,
                         self.foreground, self.background)

def mouseUp(self, event):
    self.lastx = self.canvas.canvasx(event.x)
    self.lasty = self.canvas.canvasy(event.y)
    self.canvas.delete(self.currentObject)
    self.currentObject = None
    if self.currentFunc:
        self.currentFunc(self.startx, self.starty,
                         self.lastx, self.lasty,
                         self.foreground, self.background)
    else:
        if self.selObj:
            self.canvas.itemconfig(self.selObj, width=1)

def drawLine(self, x, y, x2, y2, fg, bg):
    self.currentObject = self.canvas.create_line(x, y, x2, y2, fill=fg)

def drawRect(self, x, y, x2, y2, fg, bg):
    self.currentObject = self.canvas.create_rectangle(x, y, x2, y2, outline=fg, fill=bg)

def drawOval(self, x, y, x2, y2, fg, bg):
    self.currentObject = self.canvas.create_oval(x, y, x2, y2, outline=fg, fill=bg)

def initData(self):
    self.currentFunc = None
    self.currentObject = None
    self.selObj = None
    self.foreground = 'black'
```

Объяснения к номерам на странице:

3. Метод `mouseDown` обрабатывает нажатие мыши и создает объект для рисования.
4. Метод `mouseMotion` обновляет позицию объекта при движении мыши.
5. Метод `mouseUp` завершает рисование объекта и удаляет временные объекты.
6. Методы `drawLine`, `drawRect` и `drawOval` создают линии, прямоугольники и эллипсы соответственно.