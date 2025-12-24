---
source_image: page_132.png
page_number: 132
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.32
tokens: 7113
characters: 721
timestamp: 2025-12-24T09:23:30.300590
finish_reason: stop
---

Когда мы меняем значение flex-direction на column, свойство flex-flow ведет себя точно так же, как продемонстрировано в предыдущих примерах.

19.6. Свойство justify-content

В следующем примере мы используем только три элемента в строке. Количество элементов не ограничено.

flex-direction: row
justify-content: <значение>

flex-start (по умолчанию)
flex-end
center
space-between
space-around Пример 1
space-around Пример 2
space-evenly
stretch

Эти схематичные рисунки демонстрируют поведение элементов лишь в том случае, если для свойства justify-content применяется одно из перечисленных значений.

То же свойство justify-content используется для выравнивания элементов, когда flex-direction присвоено значение column: