---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.08
tokens: 5865
characters: 873
timestamp: 2025-12-24T04:09:14.251831
finish_reason: stop
---

while [ $i -It 3 ]' .
do
echo "$i"
i=~expr $i +1' done
$ ./myscript
0
1
2

Цикл until повторяется до тех порка, пока условие не начнет выполнятся (т. е. пока оно не вернет значение "истина"):
until команда Пока команда возвращает ненулевое значение do
тело done
Например:
i = 0
until t $i -gt 3 ]
do
echo "$i"
i=4expr $i + Γ done
$ ./myscript
0
1
2

Цикл for итерирует по значениям из списка.
for переменная in список do
тело done
Например:
for name in Tom Jack Harry do
echo "$name - мой друг" done
$ ./myscript Tom - мой друг Jack - мой друг Harry - мой друг

Цикл for особенно удобен для обработки списков файлов, например всех файлов определенного типа в текущей директории.
for file in *.doc do
echo "$file - это отвратительный файл Microsoft Word" done
Для бесконечного цикла используйте цикл while с условием true ("истина") или цикл until с условием false ("ложь").