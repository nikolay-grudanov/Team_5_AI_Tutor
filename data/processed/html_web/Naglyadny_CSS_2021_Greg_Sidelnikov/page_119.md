---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.65
tokens: 7124
characters: 632
timestamp: 2025-12-24T09:23:14.388093
finish_reason: stop
---

Трансформация перемещения может занять процент от размера элемента. Ниже показан перевод в проценты в зависимости от размеров элемента:

![Пример трансформации перемещения](../images/119_1.png)

translate(50%, 10px) rotate(5deg)
translate(30px, 10px) rotate(5deg)

Относительные элементы сохраняют свое положение в документе даже после вращения:

![Пример сохранения относительного положения](../images/119_2.png)

Вращение элемента между другими не влияет на их положение. Края будут перекрываться:

![Пример перекрытия краев при вращении](../images/119_3.png)

translate(30px, 10px) rotate(0deg)
translate(30px, 10px) rotate(5deg)