---
source_image: page_136.png
page_number: 136
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.30
tokens: 11762
characters: 1595
timestamp: 2025-12-24T01:40:57.590715
finish_reason: stop
---

Код, который должен запускаться на разных машинах или в различных ситуациях, не должен зависеть от кодировки по умолчанию. Всегда явно задавайте аргумент encoding= при открытии текстовых файлов, потому что умолчания могут зависеть от машины и даже меняться на одной и той же машине.

В примере 4.9 есть любопытная деталь: функция write в первом предложении говорит, что было записано четыре символа, а в следующей строке читается пять символов. В примере 4.10, где приведен расширенный вариант примера 4.9, объясняется этот и другие курьезы.

Пример 4.10. Более пристальное изучение запуска примера 4.9 в Windows вскрывает ошибку и показывает, как ее исправить

```python
>>> fp = open('cafe.txt', 'w', encoding='utf_8')
>>> fp ①
<_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf_8'>
>>> fp.write('café')
4 ②
>>> fp.close()
>>> import os
>>> os.stat('cafe.txt').st_size
5 ③
>>> fp2 = open('cafe.txt')
>>> fp2 ④
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='cp1252'>
>>> fp2.encoding ⑤
'cp1252'
>>> fp2.read()
'cafÃ©' ⑥
>>> fp3 = open('cafe.txt', encoding='utf_8') ⑦
>>> fp3
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='utf_8'>
>>> fp3.read()
'café' ⑧
>>> fp4 = open('cafe.txt', 'rb') ⑨
>>> fp4
<_io.BufferedReader name='cafe.txt'> ⑩
>>> fp4.read() ⑪
b'caf\xc3\xa9'
```

① По умолчанию open открывает файл в текстовом режиме и возвращает объект TextIOWrapper.
② Метод write объекта TextIOWrapper возвращает количество записанных символов Unicode.
③ Функция os.stat сообщает, что файл содержит 5 байтов; в кодировке UTF-8 буква 'é' представлена двумя байтами: 0xc3 и 0xa9.