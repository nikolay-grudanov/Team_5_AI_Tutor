---
source_image: page_505.png
page_number: 505
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.34
tokens: 11735
characters: 1698
timestamp: 2025-12-24T01:58:17.082376
finish_reason: stop
---

Использование yield from

Скрипт coroaverager3.py читает словарь, содержащий данные о весе и росте девочек и мальчиков из воображаемого седьмого класса. Например, ключу 'boys;m' соответствуют данные о росте 9 мальчиков в метрах, а ключу 'girls;kg' — данные о весе 10 девочек в килограммах. Скрипт загружает данные о каждой группе в сопрограмму averager, показанную выше, и порождает такой отчет:

$ python3 coroaverager3.py
9 boys averaging 40.42kg
9 boys averaging 1.39m
10 girls averaging 42.04kg
10 girls averaging 1.43m

Код в примере 16.17, конечно, не назовешь самым простым решением задачи, но он демонстрирует yield from в действии. В основу примера положен код из статьи «What's New in Python 3.3» (http://bit.ly/1HGrnVq).

Пример 16.17. coroaverager3.py: использование yield from для управления сопрограммой averager и печати статистического отчета

from collections import namedtuple

Result = namedtuple('Result', 'count average')

# субгенератор
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # 2
        if term is None:  # 3
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # 4

# делегирующий генератор
def grouper(results, key):  # 5
    while True:  # 6
        results[key] = yield from averager()  # 7

# клиентский код, или вызывающая сторона
def main(data):  # 8
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # 9
        next(group)  # 10
        for value in values:
            group.send(value)  # 11
        group.send(None)  # важно!  # 12
    # print(results)  # раскомментировать для отладки