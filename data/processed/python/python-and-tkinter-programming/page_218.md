---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.78
tokens: 8630
characters: 2599
timestamp: 2025-12-24T00:37:46.646571
finish_reason: stop
---

Вот текст программы с комментариями, объясняющими, что делает каждая строка:

```python
self.reference = Entry(self.frame1, width=12)
self.reference.pack(side=LEFT, fill=X, expand=1)
self.add = Button(self.frame1, text='Add', command=self.addMap)
self.add.pack(side=RIGHT, fill=None, expand=0)
self.frame2 = Frame(self.root, bd=2, relief=RAISED)
self.frame2.pack(fill=X)
self.done = Button(self.frame2, text='Build ImageMap',
                   command=self.buildMap)
self.done.pack(side=TOP, fill=None, expand=0)

Widget.bind(self.canvas, "<Button-1>", self.mouseDown)
Widget.bind(self.canvas, "<Button1-Motion>", self.mouseMotion)
Widget.bind(self.canvas, "<Button1-ButtonRelease>", self.mouseUp)

def mouseDown(self, event):
    self.startx = self.canvas.canvasx(event.x)
    self.starty = self.canvas.canvasy(event.y)

def mouseMotion(self, event):
    x = self.canvas.canvasx(event.x)
    y = self.canvas.canvasy(event.y)
    if (self.startx != event.x) and (self.starty != event.y) :
        self.canvas.delete(self.rubberbandBox)
        self.rubberbandBox = self.canvas.create_rectangle(
            self.startx, self.starty, x, y, outline='white', width=2)
        self.root.update_idletasks()

def mouseUp(self, event):
    self.endx = self.canvas.canvasx(event.x)
    self.endy = self.canvas.canvasy(event.y)
    self.reference.focus_set()
    self.reference.selection_range(0, END)

def addMap(self):
    self.coordinatedata.append(self.reference.get(),
                               self.startx, self.starty,
                               self.endx, self.endy)

def buildMap(self):
    filename = os.path.splitext(self.file)[0]
    ofd = open('%s.py' % filename, 'w')
    ifd = open('image1.inp')
    lines = ifd.read()
    ifd.close()
    ofd.write(lines)

    for ref, sx,sy, ex,ey in self.coordinatedata:
        ofd.write("    self.iMap.addRegion(((%5.1f,%5.1f),"
                  "(%5.1f,%5.1f)), '%s')\n" % (sx,sy, ex,ey, ref))

    ofd.write('\n%s\n' % ('#' * 70))
    ofd.write('if __name__ == "__main__":\n')
    ofd.write('    root = Tk()\n')
    ofd.write('    root.title("%s")\n' % self.file)
    ofd.write('    imageTest = ImageTest(root, width=%d, height=%d,\n'
```

Комментарии к каждой строке:

2. Повязка событий мыши с функциями обработки событий.
3. Обработка нажатия левой кнопки мыши.
4. Обработка движения мыши.
5. Обновление виджета при движении мыши.
6. Обработка отпускания кнопки мыши.
7. Добавление данных в список координат.
8. Открытие файла для записи.
9. Чтение исходного файла.
10. Запись данных в файл.
11. Закрытие файла и создание основной функции.