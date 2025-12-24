---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.55
tokens: 5830
characters: 765
timestamp: 2025-12-24T04:09:13.887674
finish_reason: stop
---

while true do
echo "навсегда" done
until false do
echo "и снова навсегда" done

Вероятно, вы будете использовать операторы break или exit для того, чтобы завершить эти циклы при выполнении какого-нибудь условия.

Break и Continue
Команда break осуществляет выход из текущего цикла.
Рассмотрим простой скрипт myscript.
for name in Tom Jack Harry do
echo $name
echo "снова" done echo "все сделано"
$ ./myscript
Tom
снова
Jack    . : ■
снова
Harry
снова
все сделано
А теперь с оператором break.
for name in Tom Jack Harry do
echo $name
if [ "$name" = "Jack" ]
then break
fi
echo "снова" done echo "все сделано"
Tom
снова
Jack    Выполнен оператор break
все сделано
Команда continue форсирует переход цикла к следующей итерации.
for name in Tom Jack Harry do
echo $name