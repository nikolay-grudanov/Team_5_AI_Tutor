---
source_image: page_122.png
page_number: 122
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.12
tokens: 7325
characters: 1067
timestamp: 2025-12-24T09:23:36.938972
finish_reason: stop
---

18 3D-трансформации

3D-трансформации могут преобразовать обычные HTML-элементы в трехмерные, добавляя перспективу.

18.1. Свойство rotateX

Повернем элемент по оси X, используя свойство transform: rotateX.

Перспектива > 25 %
perspective: 100px;
perspective-origin: 75% 50%

Перспектива
perspective: 100px;
perspective-origin: 50% 50%
(по умолчанию)

Перспектива < 50 %
perspective: 100px;
perspective-origin: 25% 50%

perspective: 200px;
perspective-origin: 75% 50%

perspective: 200px;
perspective-origin: 50% 50%
(по умолчанию)

perspective: 200px;
perspective-origin: 25% 50%
transform: rotateX(45deg)

perspective: 300px;
perspective-origin: 75% 50%

perspective: 300px;
perspective-origin: 50% 50%
(по умолчанию)

perspective: 300px;
perspective-origin: 25% 50%

Каждая строка в данном примере показывает, что происходит с HTML-элементом, когда его перспектива изменяется с 100 на 200 пикселов, а затем на 300 сверху вниз с использованием свойства perspective. Свойство perspective-origin также служит для изображения уклона, созданного при смещении источника.