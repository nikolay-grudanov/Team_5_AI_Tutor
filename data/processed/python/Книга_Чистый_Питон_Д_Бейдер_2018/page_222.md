---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.60
tokens: 7254
characters: 1184
timestamp: 2025-12-24T02:32:24.671787
finish_reason: stop
---

self.count = 0
def __iter__(self):
    return self
def __next__(self):
    if self.count >= self.max_repeats:
        raise StopIteration
    self.count += 1
    return self.value

И он дает нам требуемый результат. Итерации прекращаются после ряда повторений, определенных в параметре max_repeats:

>>> repeater = BoundedRepeater('Привет', 3)
>>> for item in repeater:
    print(item)
Привет
Привет
Привет

Если переписать этот последний пример цикла for...in, устранив часть синтаксического сахара, то в итоге мы получим следующий ниже расширенный фрагмент кода:

repeater = BoundedRepeater('Привет', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)

При каждом вызове функции next() в этом цикле мы выполняем проверку на исключение StopIteration и при необходимости выходим из цикла while.

Возможность написать трехстрочный цикл for...in вместо восьмистрочного цикла while представляет собой вполне хорошее улучшение. И в результате программный код становится проще для восприятия и удобнее в сопровождении. И это еще одна причина, почему в Python итераторы являются таким мощным инструментом.