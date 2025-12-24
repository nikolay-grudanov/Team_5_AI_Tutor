---
source_image: page_153.png
page_number: 153
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.60
tokens: 11781
characters: 1872
timestamp: 2025-12-24T01:41:43.467154
finish_reason: stop
---

Двухрежимный API

Двухрежимный API

В стандартной библиотеке есть функции, которые принимают в качестве аргументов значения типа str или bytes и ведут себя по-разному в зависимости от типа. Примеры имеются в модулях re и os.

str и bytes в регулярных выражениях

Если при построении регулярного выражения был задан аргумент типа bytes, то образцам вида \d или \w будут соответствовать только ASCII-символы. Наоборот, если был задан аргумент типа str, то этим образцам будут соответствовать цифры и буквы в смысле Unicode, а не только ASCII. В примере 4.22 и на рис. 4.4 показано сопоставление букв, ASCII-цифр, надстрочных индексов и тамильских цифр с образцами типа str и bytes.

Пример 4.22. ramanujan.py: сравнение поведения простых регулярных выражений с аргументами типа str и bytes

import re

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
    " as 1729 = 1^3 + 12^3 = 9^3 + 10^3.")

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n ')
print('Numbers')
print('  str :', re_numbers_str.findall(text_str))
print('  bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print('  str :', re_words_str.findall(text_str))
print('  bytes:', re_words_bytes.findall(text_bytes))

1 Первые два регулярных выражения типа str.
2 Последние два регулярных выражения типа bytes.
3 Текст Unicode, в котором производится поиск, содержит тамильские цифры числа 1729 (логическая строка продолжается до правой закрывающей скобки).
4 Эта строка конкатенируется с предыдущей на этапе компиляции (см. раздел 2.4. «Конкатенация строковых литералов» (http://bit.ly/1IqE2vH) справочного руководства по языку Python).
5 Для поиска с помощью регулярного выражения типа bytes необходима строка типа bytes.