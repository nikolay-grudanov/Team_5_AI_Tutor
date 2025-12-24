---
source_image: page_102.png
page_number: 102
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.02
tokens: 5786
characters: 668
timestamp: 2025-12-24T04:06:46.256957
finish_reason: stop
---

paste [опции] [файлы]
/usr/bin    stdin stdout -file —opt —help —version

Команда paste — противоположность команды cut: она рассматривает несколько файлов как вертикальные колонки, объединяет их и выводит в стандартный поток вывода:

$ cat letters
A
B
C

$ cat numbers
1
2
3
4
5

$ paste numbers letters
1    A
2    B
3    C
4
5

$ paste letters numbers
A    1
B    2
C    3
4
5

Полезные опции

-d разделители
Использовать указанные разделители между колонками; по умолчанию используется символ табуляции. Вы можете указать одиночный символ (- d:), который будет использовать везде, либо список символов (-dxyz), которые будут использоваться последовательно в строке