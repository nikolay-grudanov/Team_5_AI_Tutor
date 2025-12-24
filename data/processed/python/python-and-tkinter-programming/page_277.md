---
source_image: page_277.png
page_number: 277
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.72
tokens: 8818
characters: 3326
timestamp: 2025-12-24T00:39:27.596701
finish_reason: stop
---

Данная программа создает окно с прокруткой, используя модуль Tkinter. В ней определен класс `ScrolledCanvas`, который создает холст с прокруткой и рисует на нем прямоугольники. Прямоугольники создаются в цикле по координатам (i, j), где i и j изменяются от 0 до 19 и 0 до 9 соответственно. Каждый прямоугольник имеет текстовое поле с индексами (i, j). Если пользователь щелкает на одном из прямоугольников, индексы этого прямоугольника выводятся на консоль.

Код разбит на три основные части:

1. Создание холста с прокруткой и привязка горизонтальной и вертикальной прокрутки к холstu.
2. Настройка сетки и создание прямоугольников на холсте.
3. Обработка событий мыши для выделения и перетаскивания прямоугольников.

Вот полный код программы:

```python
cscroll.py

from Tkinter import *

class ScrolledCanvas:
    def __init__(self, master, width=500, height=350):
        Label(master, text="This window displays a canvas widget "
            "that can be scrolled either using the scrollbars or "
            "by dragging with button 3 in the canvas. If you "
            "click button 1 on one of the rectangles, its indices "
            "will be printed on stdout.",
            wraplength="4i", justify=LEFT).pack(side=TOP)
        self.control=Frame(master)
        self.control.pack(side=BOTTOM, fill=X, padx=2)
        Button(self.control, text='Quit', command=master.quit).pack()

        self.grid = Frame(master)
        self.canvas = Canvas(master, relief=SUNKEN, borderwidth=2,
            scrollregion=('-11c', '-11c', '50c', '20c'))
        self.hscroll = Scrollbar(master, orient=HORIZONTAL,
            command=self.canvas.xview)
        self.vscroll = Scrollbar(master, command=self.canvas.yview)

        self.canvas.configure(xscrollcommand=self.hscroll.set,
            yscrollcommand=self.vscroll.set)

        self.grid.pack(expand=YES, fill=BOTH, padx=1, pady=1)
        self.grid.rowconfigure(0, weight=1, minsize=0)
        self.grid.columnconfigure(0, weight=1, minsize=0)
        self.canvas.grid(padx=1, in_=self.grid, pady=1, row=0,
            column=0, rowspan=1, columnspan=1, sticky='news')
        self.vscroll.grid(padx=1, in_=self.grid, pady=1, row=0,
            column=1, rowspan=1, columnspan=1, sticky='news')
        self.hscroll.grid(padx=1, in_=self.grid, pady=1, row=1,
            column=0, rowspan=1, columnspan=1, sticky='news')

        self.oldFill = None

        bg = self.canvas['background']
        for i in range(20):
            x = -10 + 3*i
            y = -10
            for j in range(10):
                self.canvas.create_rectangle('%dc'%x, '%dc'%y,
                    '%dc'%(x+2), '%dc'%(y+2), outline='black',
                    fill=bg, tags='rect')
                self.canvas.create_text('%dc'%(x+1), '%dc'%(y+1),
                    text='%d,%d'%(i,j), anchor=CENTER,
                    tags=('text', 'rect'))
                y = y + 3
        self.canvas.tag_bind('rect', '<Any-Enter>', self.scrollEnter)
        self.canvas.tag_bind('rect', '<Any-Leave>', self.scrollLeave)
        self.canvas.bind_all('<1>', self.scrollButton)
        self.canvas.bind('<3>', lambda e, s=self: s.canvas.scan_mark(e.x, e.y))
        self.canvas.bind('<B3-Motion>', lambda e, s=self: s.canvas.scan_dragto(e.x, e.y))

CHAPTER 10  DRAWING BLOBS AND RUBBER LINES
```