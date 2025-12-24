---
source_image: page_709.png
page_number: 709
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.59
tokens: 11654
characters: 1537
timestamp: 2025-12-24T02:07:15.585091
finish_reason: stop
---

Глава 3: сравнение битовых представлений хешей

Скрипт container_perftest_datagen.py (пример А.2) генерирует фикстуры данных для скрипта из примера А.1.

Пример А.2. container_perftest_datagen.py: генерирует файлы, содержащие массивы уникальных чисел с плавающей точкой, для использования в примере А.1

"""
Генерировать данные для теста производительности контейнера
"""

import random
import array

MAX_EXPONENT = 7
HAYSTACK_LEN = 10 ** MAX_EXPONENT
NEEDLES_LEN = 10 ** (MAX_EXPONENT - 1)
SAMPLE_LEN = HAYSTACK_LEN + NEEDLES_LEN // 2

needles = array.array('d')

sample = {1/random.random() for i in range(SAMPLE_LEN)}
print('initial sample: %d elements' % len(sample))

# дополнить выборку, если были отброшены дубликаты
while len(sample) < SAMPLE_LEN:
    sample.add(1/random.random())

print('complete sample: %d elements' % len(sample))

sample = array.array('d', sample)
random.shuffle(sample)

not_selected = sample[:NEEDLES_LEN // 2]
print('not selected: %d samples' % len(not_selected))
print('writing not_selected.arr')
with open('not_selected.arr', 'wb') as fp:
    not_selected.tofile(fp)

selected = sample[NEEDLES_LEN // 2:]
print('selected: %d samples' % len(selected))
print('writing selected.arr')
with open('selected.arr', 'wb') as fp:
    selected.tofile(fp)

Глава 3: сравнение битовых представлений хешей

В примере А.3 приведен простой скрипт, показывающий, как отличаются битовые представления хешей близких чисел с плавающей точкой (например, 1.0001, 1.0002 и т. д.). Результат его работы показан в примере 3.16.