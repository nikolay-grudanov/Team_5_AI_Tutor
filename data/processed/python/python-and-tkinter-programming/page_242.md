---
source_image: page_242.png
page_number: 242
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.66
tokens: 8656
characters: 2346
timestamp: 2025-12-24T00:38:27.891663
finish_reason: stop
---

Вот текст программы с комментариями и номерами шагов:

```python
self.img = PhotoImage(file='images/6c110_enet.gif')
setattr(glb, 'img%d % slot', self.img)
self.width  = self.img.width()
self.height = self.img.height()

C6C110_CardBlank.__init__(self, master=master, width=self.width,
    height=self.height)

xypos = [(10,180), (10,187),
    (10,195), (10,203),
    (10,210), (10,235),
    (10,242)]

self.canvas = Canvas(self.card_frame, width=self.width,
    bd=0, highlightthickness=0,
    height=self.height, selectborderwidth=0)
self.canvas.pack(side="top", fill=BOTH, expand='no')
self.canvas.create_image(0,0,anchor=NW,
    image=eval('glb.img%d' % slot))

for i, y in [(0, 0.330), (1, 0.619)]:
    setattr(self, 'j%d' % i, Enet10baseT(self.card_frame,
        fid="10Base-T-%d" % i, port=i, orient=HW_LEFT,
        status=STATUS_OFF, xwidth=15, xheight=12))
    getattr(self, 'j%d' % i).j45_frame.place(relx=0.52, rely=y, anchor=CENTER)

for i in range(len(xypos)):
    xpos,ypos = xypos[i]
    setattr(self, 'led%d' % (i+1), CLED(self.card_frame,
        self.canvas, shape=ROUND, width=4, status=STATUS_ON,
        relx=xpos, rely=ypos))

class C6C110_Chassis:
    def __init__(self, master):
        self.outer=Frame(master, borderwidth=0, bg=Color.PANEL)
        self.outer.forget()

        self.img = PhotoImage(file='images/6c110_chassis.gif')
        self.width  = self.img.width()
        self.height = self.img.height()

        self.canvas = Canvas(self.outer, width=self.width,
            height=self.height, selectborderwidth=0)
        self.canvas.pack(side="top", fill=BOTH, expand='no')
        self.canvas.create_image(0,0,anchor=NW, image=self.img)

        self.rack = Frame(self.outer, bd=0, width=self.width-84,
            height=self.height-180,
            bg=Color.CHASSIS, highlightthickness=0)
        self.rack.place(relx=0.081, rely=0.117, anchor=NW)

        x = 0.0
        for i in range(12):
            if i in [0,1,2,3,4,5]:
                card =C6C110_FDDI(self.rack, slot=i)
```

Комментарии к шагам:

1. Загрузка и установка изображения.
2. Определение позиций LED.
3. Создание холста для рисования.
4. Вставка изображения на холст.
5. Создание и размещение индикаторов состояния для сетевых портов.
6. Создание и размещение индикаторов состояния для LED.
7. Создание и размещение модулей в шасси.