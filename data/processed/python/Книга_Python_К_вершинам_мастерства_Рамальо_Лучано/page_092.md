---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.15
tokens: 11777
characters: 1663
timestamp: 2025-12-24T01:38:48.651760
finish_reason: stop
---

4 При задании аргумента key функции sorted мы не вызываем str.upper, а только передаем ссылку на этот метод, чтобы sorted могла нормализовать слова перед сортировкой2.

Пример 3.3. Частичная распечатка результата работы скрипта 3.2, примененного к «Дзен Python»; в каждой строке присутствует слово и список его вхождений в виде пар (номер-строки, номер-колонки)

$ python3 index0.py ../../data/zen.txt
a [(19, 48), (20, 53)]
Although [(11, 1), (16, 1), (18, 1)]
ambiguity [(14, 16)]
and [(15, 23)]
are [(21, 12)]
aren [(10, 15)]
at [(16, 38)]
bad [(19, 50)]
be [(15, 14), (16, 27), (20, 50)]
beats [(11, 23)]
Beautiful [(3, 1)]
better [(3, 14), (4, 13), (5, 11), (6, 12), (7, 9), (8, 11), (17, 8), (18, 25)]
...

Три строчки, относящиеся к обработке occurrences в примере 3.2, можно заменить одной, воспользовавшись методом dict.setdefault. Пример 3.4 ближе к оригинальному примеру Алекса Мартелли.

Пример 3.4. index.py: применение метода dict.setdefault для выборки и обновления списка вхождений слова в индекс; в отличие от примера 3.2 понадобилась только одна строчка

"""Строит индекс, отображающий слово на список его вхождений"""
import sys
import re
WORD_RE = re.compile('\w+')
index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)  # напечатать в алфавитном порядке

2 Здесь мы видим пример использования метода в качестве полноценной функции, подробнее эта тема обсуждается в главе 5.