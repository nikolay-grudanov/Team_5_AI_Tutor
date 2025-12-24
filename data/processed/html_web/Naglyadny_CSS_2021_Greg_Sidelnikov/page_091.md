---
source_image: page_091.png
page_number: 91
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.69
tokens: 7260
characters: 850
timestamp: 2025-12-24T09:22:43.020018
finish_reason: stop
---

Повторяющиеся узоры для линейных и радиальных градиентов могут быть созданы с помощью свойств repeating-linear-gradient и repeating-radial-gradient соответственно. Вы можете указать столько повторяющихся значений цвета в строке, сколько необходимо. Просто не забудьте разделить их запятой!

repeating-linear-gradient (white 100px; black 200px; white 300px);
repeating-radial-gradient (white 100px; black 200px; white 300px);

Наконец, самый усовершенствованный тип градиента можно создать с помощью ряда значений HSL. Значения HSL не имеют именованных или RGB-эквивалентов, они рассчитываются по шкале от 0 до 300. См. пояснение далее.

linear-gradient hsl(0,100%,50%), hsl(50,100%,50%), hsl(100,100%,50%), hsl(150,100%,50%), hsl(200,100%,50%), hsl(250,100%,50%), hsl(300,100%,50%)
linear-gradient hsl(0,100%,50%), hsl(50,100%,50%), hsl(300,100%,50%)