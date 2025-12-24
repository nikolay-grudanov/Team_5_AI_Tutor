---
source_image: page_188.png
page_number: 188
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.36
tokens: 7153
characters: 709
timestamp: 2025-12-24T09:24:41.714475
finish_reason: stop
---

23.7. Свойство animation-timing-function

Динамика задается свойством animation-timing-function, которое придает вашей анимации индивидуальность. Это делается путем регулировки скорости анимации в любой заданной точке на временной шкале. Важными являются начальная, средняя и конечная точки. Каждый тип замедления определяется функцией кривой Безье.

animation-timing-function: linear
cubic-bezier(0, 0, 1, 1);
Сохраняет постоянную скорость от начала до конца

animation-timing-function: ease
cubic-bezier(0.25, 0.1, 0.25, 1);
Начинается медленно, ускоряется, замедляется в конце <по умолчанию>

animation-timing-function: ease-in
cubic-bezier(0.42, 0, 1, 1);
Устанавливает эффект перехода с медленным стартом