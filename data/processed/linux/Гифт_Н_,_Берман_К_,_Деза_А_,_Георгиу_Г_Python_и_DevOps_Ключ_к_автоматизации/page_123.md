---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.93
tokens: 7163
characters: 783
timestamp: 2025-12-24T03:03:52.005350
finish_reason: stop
---

[5 rows x 12 columns]

$ python -W nuclearcli.py cluster --num 2

Clustered DataFrame
    TEAM   GMS   ...   COUNTY   cluster
0   Chicago Bulls   41   ...   Cook   1
1   Dallas Mavericks   41   ...   Dallas   1
2   Sacramento Kings   41   ...   Sacramento   0
3   Miami Heat   41   ...   Miami-Dade   1
4   Toronto Raptors   41   ...   York-County   1
[5 rows x 12 columns]

Упражнения

• Напишите с помощью sys сценарий, который выводит текст «командная строка» только тогда, когда запущен из командной строки.

• Создайте с помощью библиотеки click утилиту командной строки, принимающую в качестве аргумента название и выводящую его в случае, если оно не начинается с символа p.

• Воспользуйтесь fire для обращения к методам в уже существующем сценарии Python из командной строки.