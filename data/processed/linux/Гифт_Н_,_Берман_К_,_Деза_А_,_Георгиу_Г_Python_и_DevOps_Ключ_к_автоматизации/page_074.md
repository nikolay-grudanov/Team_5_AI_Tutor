---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.22
tokens: 7463
characters: 1674
timestamp: 2025-12-24T03:02:53.992685
finish_reason: stop
---

Этот модуль производит синтаксический разбор формата JSON и возвращает данные в виде соответствующих структур данных Python:

In [13]: from pprint import pprint

In [14]: pprint(policy)
{'Statement': {'Action': 'service-prefix:action-name',
    'Condition': {'DateGreaterThan':
        {'aws:CurrentTime': '2017-07-01T00:00:00Z'},
        'DateLessThan':
        {'aws:CurrentTime': '2017-12-31T23:59:59Z'}},
    'Effect': 'Allow',
    'Resource': '*'},
'Version': '2012-10-17'}

Модуль pprint автоматически форматирует объекты Python для вывода в консоль. Выводимые им данные обычно намного удобнее для чтения и анализа вложенных структур данных.

Теперь можно работать с данными с исходной структурой из файла. Например, вот так можно изменить ресурс, доступом к которому управляет эта стратегия, на S3:

In [15]: policy['Statement']['Resource'] = 'S3'
In [16]: pprint(policy)
{'Statement': {'Action': 'service-prefix:action-name',
    'Condition': {'DateGreaterThan':
        {'aws:CurrentTime': '2017-07-01T00:00:00Z'},
        'DateLessThan':
        {'aws:CurrentTime': '2017-12-31T23:59:59Z'}},
    'Effect': 'Allow',
    'Resource': 'S3'},
'Version': '2012-10-17'}

С помощью метода json.dump можно записать ассоциативный массив Python в JSON-файл. Вот так можно обновить только что модифицированный нами файл стратегии:

In [17]: with open('service-policy.json', 'w') as opened_file:
    ...:     policy = json.dump(policy, opened_file)
    ...:
    ...:
    ...:
    ...:

В файлах конфигурации нередко применяется и еще один язык — YAML, представляющий собой расширенную версию JSON, но в более сжатом формате, в котором пробелы используются так же, как в Python.