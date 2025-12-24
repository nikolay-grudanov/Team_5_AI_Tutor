---
source_image: page_710.png
page_number: 710
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.85
tokens: 11745
characters: 1634
timestamp: 2025-12-24T02:07:28.327221
finish_reason: stop
---

Пример A.3. hashdiff.py: показывает битовые представления хэшированных значений

import sys

MAX_BITS = len(format(sys.maxsize, 'b'))

print('%s-bit Python build' % (MAX_BITS + 1))

def hash_diff(o1, o2):
    h1 = '{:>0{}b}'.format(hash(o1), MAX_BITS)
    h2 = '{:>0{}b}'.format(hash(o2), MAX_BITS)
    diff = ''.join('!' if b1 != b2 else ' ' for b1, b2 in zip(h1, h2))
    count = '!={}'.format(diff.count('!'))
    width = max(len(repr(o1)), len(repr(o2)), 8)
    sep = '_' * (width * 2 + MAX_BITS)
    return '{!r:{width}} {}{!r:{width}} {}{!r:{width}} {}'.format(
        o1, h1, ' ' * width, diff, count, o2, h2, sep, width=width)

if __name__ == '__main__':
    print(hash_diff(1, 1.0))
    print(hash_diff(1.0, 1.0001))
    print(hash_diff(1.0001, 1.0002))
    print(hash_diff(1.0002, 1.0003))

Глава 9. Потребление оперативной памяти при наличии и отсутствии __slots__

Скрипт memtest.py использовался для демонстрации в разделе примере 9.12 из раздела «Экономия памяти с помощью атрибута класса __slots__» главы 9.

Этот скрипт принимает имя модуля в командной строке и загружает его. В предположении, что в модуле определен класс Vector, скрипт memtest.py создает список, содержащий 10 миллионов экземпляров, и печатает объем занятой памяти до и после создания списка.

Пример A.4. memtest.py: создает очень много экземпляров Vector и печатает сведения о потреблении памяти

import importlib
import sys
import resource

NUM_VECTORS = 10**7

if len(sys.argv) == 2:
    module_name = sys.argv[1].replace('.py', '')
    module = importlib.import_module(module_name)
else:
    print('Usage: {} <vector-module-to-test>'.format())