---
source_image: page_200.png
page_number: 200
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.83
tokens: 7332
characters: 1208
timestamp: 2025-12-24T04:50:33.896993
finish_reason: stop
---

for FILE in `/bin/ls`
do
    echo $FILE
done

Вариант с более чистым кодом:

for NAME in John Paul Ringo George ; do
    echo $NAME is my favorite Beatle
done

Каждый элемент в LIST отделен от следующего пробелом. Будьте с этим осторожны, потому что некоторые команды, такие как ls -l, выводят в строке несколько полей, каждое из которых отделено пробелом. Строка done завершает выражение for.

Заядлый программист на языке C может использовать его синтаксис для работы с циклами:

LIMIT=10
# Используются двойные скобки без знака $ в значении LIMIT,
# несмотря на то что это переменная!
for ((a=1; a <= LIMIT ; a++)) ; do
    echo "$a"
done

Циклы while...do и until...do

Еще два популярных цикла — это while...do и until...do. Вот их структуры:

while condition
do
    { body }
done

until condition
do
    { body }
done

Оператор while выполняется, пока условие выражения истинно. Оператор until выполняется до тех пор, пока условие не станет истинным, другими словами, пока оно ложно.

Пример цикла while для вывода числа 0123456789:

N=0
while [ $N -lt 10 ] ; do
    echo -n $N
    let N=$N+1
done

Вывод числа 0123456789 с циклом until:

N=0
until [ $N -eq 10 ] ; do
    echo -n $N
    let N=$N+1
done