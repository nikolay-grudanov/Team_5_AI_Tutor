---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.55
tokens: 7223
characters: 945
timestamp: 2025-12-24T09:24:41.565392
finish_reason: stop
---

Превратим желтый квадрат в бирюзовый круг. Как только класс .классАнимации назначен элементу, анимация начнет воспроизводиться. Класс ссылается на имяАнимации. Это значение должно совпадать с именем, заданным директивой @keyframes. Анимация настроена на 3 с, или 3000 мс. Примечание: динамика добавляет изюминку вашей анимации с помощью кривой, описывающей относительную скорость анимации в определенном месте на временной шкале.

Исходное изображение
width: 100px;
height: 100px;
border: 1px solid black;
background: yellow;

Полученное изображение
border-radius: 50px;
background: teal;

@keyframes имяАнимации {
    0% { border-radius: 0; background: yellow; }
    100% { border-radius: 50px; background: teal; }
}

.классАнимации {
    animation-name: имяАнимации;
    animation-fill-mode: forwards;
    animation: normal 3000ms ease;
}

Далее рассмотрим сглаживание (плавность) и все другие свойства CSS-анимаций на основе простого примера.