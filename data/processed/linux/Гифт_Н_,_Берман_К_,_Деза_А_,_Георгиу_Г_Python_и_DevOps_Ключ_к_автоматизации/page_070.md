---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.37
tokens: 7404
characters: 1553
timestamp: 2025-12-24T03:02:47.085179
finish_reason: stop
---

In [3]: text = open_file.read()
In [4]: len(text)
Out[4]: 476909

In [5]: text[56]
Out[5]: 's'

In [6]: open_file
Out[6]: <_io.TextIOWrapper name='bookofdreams.txt' mode='r' encoding='UTF-8'>

In [7]: open_file.close()

По завершении работы с файлом желательно его закрывать. Python закрывает файлы при выходе из области видимости, но до тех пор они занимают ресурсы и могут оказаться недоступными для других процессов.

Можно также читать файлы с помощью метода readlines: он читает файл и разбивает его содержимое по символам перевода строк. Он возвращает список строковых значений, каждое из которых содержит одну строку исходного текста:

In [8]: open_file = open(file_path, 'r')
In [9]: text = open_file.readlines()
In [10]: len(text)
Out[10]: 8796

In [11]: text[100]
Out[11]: 'science, when it admits the possibility of occasional hallucinations\n'

In [12]: open_file.close()

Файлы удобно открывать с помощью операторов with. При этом не требуется закрывать их явно. Python сам закроет файл и освободит выделенные под него ресурсы в конце отформатированного с помощью отступов блока:

In [13]: with open(file_path, 'r') as open_file:
    ...:     text = open_file.readlines()
    ...:

In [14]: text[101]
Out[14]: 'in the sane and healthy, also admits, of course, the existence of\n'

In [15]: open_file.closed
Out[15]: True

В различных операционных системах — разные экранированные символы для обозначения конца строки: в Unix-системах — \n, а в Windows — \r\n. Python преобразует их в \n при открытии файла как текстового. Если открывать как