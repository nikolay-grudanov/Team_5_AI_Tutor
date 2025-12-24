---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.87
tokens: 8485
characters: 2599
timestamp: 2025-12-24T00:34:37.957983
finish_reason: stop
---

Вот текст программы с комментариями, объясняющими, что делает каждая часть кода:

```python
imageEditor.py

from Tkinter import *
import sys, Pmw, Image, ImageTk, ImageEnhance

class Enhancer:
    def __init__(self, master=None, imgfile=None):
        self.master = master
        self.masterImg = Image.open(imgfile)
        self.masterImg.thumbnail((150, 150))

        self.images = [None]*9
        self.imgs = [None]*9
        for i in range(9):
            image = self.masterImg.copy()
            self.images[i] = image
            self.imgs[i] = ImageTk.PhotoImage(self.images[i].mode,
                                             self.images[i].size)

        i = 0
        for r in range(3):
            for c in range(3):
                lbl = Label(master, image=self.imgs[i])
                lbl.grid(row=r*5, column=c*2,
                         rowspan=5, colspan=2, sticky=NSEW,
                         padx=5, pady=5)
                i = i + 1

        self.original = ImageTk.PhotoImage(self.masterImg)
        Label(master, image=self.original).grid(row=0, column=6,
                                                rowspan=5, colspan=2)

        Label(master, text='Enhance', bg='gray70').grid(row=5, column=6,
                                                        colspan=2, sticky=NSEW)

        self.radio = Pmw.RadioSelect(master, labelpos = None,
                                     buttontype = 'radiobutton', orient = 'vertical',
                                     command = self.selectFunc)

        self.radio.grid(row=6, column=6, rowspan=4, colspan=2)

# --- Code Removed -------------------------------------------------------------
        Label(master, text='Variation',
              bg='gray70').grid(row=10, column=6,
                                colspan=2, sticky=NSWE)

        self.variation=Pmw.ComboBox(master, history=0, entry_width=11,
                                    selectioncommand = self.setVariation,
                                    scrolledlist_items=({'Fine','Medium Fine','Medium',
                                                         'Medium Course','Course'}))

        self.variation.selectitem('Medium')

        self.variation.grid(row=11, column=6, colspan=2)
```

Комментарии к каждой части кода:

1. Входные модули и класс Enhancer.
2. Инициализация класса Enhancer, открытие изображения и создание копий для каждого изображения.
3. Создание и размещение 9 копий изображения на экране.
4. Отображение оригинального изображения.
5. Отображение кнопки "Enhance".
6. Создание и размещение радиокнопок для выбора эффектов.