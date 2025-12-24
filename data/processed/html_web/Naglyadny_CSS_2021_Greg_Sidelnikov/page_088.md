---
source_image: page_088.png
page_number: 88
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.40
tokens: 7145
characters: 773
timestamp: 2025-12-24T09:22:28.610874
finish_reason: stop
---

Все значения градиента CSS передаются в свойство background. Вот пример создания простого линейного градиента:

001 background: linear-gradient(black, white);

Ниже можно будет увидеть, как с помощью этой функции и ее значений создается градиент.

12.2. Типы градиентов

Рассмотрим разные стили градиента и визуализируем тип эффектов градиента, а также рассмотрим их применение.

linear-gradient(black, white)        linear-gradient(yellow, red)

Это простой линейный градиент. Слева: от черного к белому. Справа: от желтого к красному.

Горизонтальные градиенты можно создать, указав начальное значение to left (налево) или to right (направо), в зависимости от желаемого направления:

linear-gradient (to left, black, white)        linear-gradient (to right, black, white)