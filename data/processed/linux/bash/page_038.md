---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.94
tokens: 7306
characters: 1204
timestamp: 2025-12-23T23:02:59.919172
finish_reason: stop
---

pwd
cd ..
done

Цикл for также доступен в bash, причем в трех вариантах.

Организовать простой числовой цикл можно с использованием двойных скобок. Он очень похож на цикл for в C или Java, но с двойными скобками и с do и done вместо фигурных скобок:

for ((i=0; i < 100; i++))
do
    echo $i
done

Цикл for другого вида используется для перебора всех параметров, которые передаются сценарию оболочки (или функции в сценарии), то есть $1, $2, $3 и т. д. Обратите внимание, что ARG в args.sh можно заменить любым именем переменной по вашему выбору.

Пример 2.2. args.sh

for ARG
do
    echo here is an argument: $ARG
done

Вот вывод для примера 2.2, когда передается три параметра:

$ ./args.sh bash is fun

here is an argument: bash
here is an argument: is
here is an argument: fun

Наконец, для произвольного списка значений используйте аналогичную форму оператора for и просто назовите каждое из значений для каждой итерации цикла. Этот список может быть задан явно, например, так:

for VAL in 20 3 dog peach 7 vanilla
do
    echo $VAL
done

Значения, указанные в цикле for, также можно генерировать, вызывая другие программы или используя другие функции оболочки:

for VAL in $(ls | grep pdf) {0..5}
do