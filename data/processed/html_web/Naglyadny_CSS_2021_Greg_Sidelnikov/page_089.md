---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.20
tokens: 7276
characters: 1032
timestamp: 2025-12-24T09:22:39.416332
finish_reason: stop
---

Можно запускать градиенты и в углах, чтобы создавать диагональные цветовые переходы. Достичь этого эффекта позволяют значения to top left (вверх и налево), to top right (вверх и направо), to bottom left (вниз и налево) и to bottom right (вниз и направо):

![Примеры линейных градиентов с различными направлениями](https://i.imgur.com/3Q5z5QG.png)

linear-gradient (to top left, black, white)
linear-gradient (to top right, black, white)
linear-gradient (to bottom left, black, white)
linear-gradient (to bottom right, black, white)

Если угла 45 градусов недостаточно, то можно указать произвольный градус в диапазоне от 0 до 360 непосредственно для линейного градиента linear-gradient(30deg, black, white).

Обратите внимание: в следующем примере градиент постепенно меняет направление от потока вниз, к левой стороне, когда угол изменяется в прогрессии от 10 до 90 градусов:

![Примеры линейных градиентов с различными углами](https://i.imgur.com/3Q5z5QG.png)

10deg   20deg   30deg   40deg   50deg   60deg   70deg   80deg   90deg