---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.83
tokens: 11644
characters: 1801
timestamp: 2025-12-24T01:38:48.633612
finish_reason: stop
---

Вызываемый объект, порождающий значения по умолчанию, хранится в атрибуте экземпляра default_factory.

Пример 3.5. index_default.py: использование экземпляра defaultdict вместо метода setdefault

"""Строит индекс, отображающий слово на список его вхождений"""

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)  # Создаем defaultdict, задав в качестве default_factory конструктор list.
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)  # Если слова word еще нет в index, то вызывается функция default_factory, которая порождает отсутствующее значение — в данном случае пустой список. Это значение присваивается index[word] и возвращается, так что операция .append(location) всегда завершается успешно. Если атрибут default_factory не задан, то в случае отсутствия ключа, как обычно, возбуждается исключение KeyError.

# напечатать в алфавитном порядке
for word in sorted(index, key=str.upper):
    print(word, index[word])

Атрибут default_factory объекта defaultdict вызывается только для того, чтобы предоставить значение по умолчанию при обращении к методу __getitem__ и только к нему. Например, если dd — объект класса defaultdict и k — отсутствующий ключ, то при вычислении выражения dd[k] происходит обращение к default_factory для создания значения по умолчанию, а вызов dd.get(k) все равно возвращает None.

А почему defaultdict обращается к default_factory? Всему виной специальный метод __missing__, который поддерживается всеми стандартными типами отображений. Его мы и обсудим далее.