---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.78
tokens: 7123
characters: 590
timestamp: 2025-12-24T02:35:53.683567
finish_reason: stop
---

for letter in ['c', 'a', 't']:
    print(letter)

Вывод
с
а
т

Этап 3: Наконец, letter указывает на t, список уничтожается

for letter in ['c', 'a', 't']:
    print(letter)

Вывод
с
а
т

Этап 4: Символы с и а уничтожаются, символ t остается

Рис. 15.2. Цикл for продолжается, а после вывода 't' он завершается. В этот момент литерал списка уничтожается в ходе уборки мусора. Так как на 'c' и 'a' указывает только список, они тоже уничтожаются. Однако переменная letter продолжает указывать на 't'. Python не уничтожает эту переменную, и она продолжит существовать после завершения цикла for