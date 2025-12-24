---
source_image: page_198.png
page_number: 198
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.90
tokens: 7225
characters: 727
timestamp: 2025-12-24T09:58:34.090226
finish_reason: stop
---

22.12 Как работает JSON

элемент
    элемент ',' элементы
элемент
    ws значение ws
строка
    '"'"' символы '"'"'
символы
    '""
        символ символы
символ
    '0020' . '10FFFF' - '"'"' - '"\
    '\' переход
переход
    '"'
    '\''
    '/'
    'b'
    'n'
    'r'
    't'
    'u' hex hex hex hex
hex
    разряд
    'A' . 'F'
    'a' . 'f'
число
    int frac expr
int
    разряд
    разряды от 0 до 9
    '-' разряд
    '-' разряды от 0 до 9
разряды
    разряд
    разряд разряды
разряды
    '0'
    от 0 до 9
от 0 до 9
    '1' . '9'
frac
    '"'
    '.' разряды
expr
    '"'
    'E' знаковые разряды
    'e' знаковые разряды
знак
    '"'
    '+'
    '-'
ws
    '"'
    '0009' ws
    '000A' ws
    '000D' ws
    '0020' ws