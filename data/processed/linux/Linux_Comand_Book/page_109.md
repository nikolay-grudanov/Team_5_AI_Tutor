---
source_image: page_109.png
page_number: 109
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.85
tokens: 5918
characters: 1031
timestamp: 2025-12-24T04:07:00.926460
finish_reason: stop
---

Вывести второе и четвертое слова каждой строки.

$ awk '{print $2, $4}' myfile

Вывести все строки короче 60 символов.

$ awk '{length($0) < 60}' myfile

sed
Аналогично awk, sed - это механизм поиска по шаблону, который может выполнять операции над строками текста. Его синтаксис тесно связан с синтаксисом vim и строчного редактора ed.
Вот несколько тривиальных примеров.
    Вывести файл, в котором все вхождения строки "red" будут заменены строкой "hat".

$ sed 's/red/hat/g' myfile

Вывести файл, у которого будут удалены первые 10 строк.

$ sed 'l,10d' myfile

m4
m4 - это язык обработки макросов. Он ищет ключевые слова в файле и заменяет их заданными значениями. Например, для файла:

$ cat myfile
My name is NAME and I am AGE years old
ifelse(QUOTE,yes,No matter where you go... there you are)

команда m4 заменит слова NAME, AGE и QUOTE.

$ m4 -DNAME=Sandy myfile
My name is Sandy and I am AGE years old
$ m4 -DNAME=Sandy -DAGE=25 myfile
My name is Sandy and I am 25 years old
$ m4 -DNAME=Sandy -DAGE=25 -DQUOTE=yes myfile