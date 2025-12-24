---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.50
tokens: 7309
characters: 1202
timestamp: 2025-12-24T09:24:33.036044
finish_reason: stop
---

С помощью значений -start и -end можно физически переместить элемент в другое место в grid-макете. Рассмотрим пример.

![Пример перемещения элемента в grid-макете](https://i.imgur.com/3Q5z5QG.png)

background: yellow

background: yellow
grid-row-start: 2
grid-column-start: 2

Интересный факт: разработчики grid-верстки решили, что направление группировки будет незначительным. Группировка по-прежнему создается в указанной области независимо от того, указаны ли начальная или конечная точки в обратном порядке.

![Пример использования grid-row-start и grid-column-start](https://i.imgur.com/7Q5z5QG.png)

Контейнер:
grid-template-columns:
    100px 100px 100px 100px 100px 100px 100px
grid-template-rows: 100px 100px 100px 100px 100px

Элемент 8
grid-row-start: 2
grid-row-end: 4
grid-column-start: 2
grid-column-end: 6

В данном примере мы взяли элемент 8 и (избыточно) указали его местоположение, используя свойства grid-row-start и grid-column-start. Но обратите внимание, что само по себе это не оказывает важного влияния на элемент 8, поскольку тот уже находится в данном месте grid-макета в любом случае. Однако, делая это, вы можете достичь функциональности, подобной элементам span, если также