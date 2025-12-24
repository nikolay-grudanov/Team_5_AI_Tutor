---
source_image: page_227.png
page_number: 227
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.07
tokens: 7437
characters: 1872
timestamp: 2025-12-24T04:38:19.361504
finish_reason: stop
---

команд. В режиме трассировки команд интерпретатора видно, что команда convert(1) в теле цикла выполняется столько раз, сколько слов (найденных имен файлов) было подставлено из вывода команды find(1). При этом переменная file на каждой итерации цикла () принимает очередное значение из подставленного списка. В результате последовательных подстановок разных значений переменной $file были выполнены одинаковые преобразования разных файлов изображений.

Листинг 5.45. Цикл с параметром: создание галереи миниатюр фотографий

bender@ubuntu:~$ set -x
bender@ubuntu:~$ for file in $(find DCIM -name '*.jpg')
> do
>   convert $file -resize 100x $(basename $file .jpg).mini.jpg
> done

1 ++ find DCIM -iname '*.jpg'
() + for file in '$(find DCIM -name '\''*.jpg'\'''
++ basename DCIM/DSC_0067.jpg .jpg
+ convert DCIM/DSC_0067.jpg -resize 100x DSC_0067.mini.jpg
() + for file in '$(find DCIM -name '\''*.jpg'\'''
++ basename DCIM/DSC_0189.jpg .jpg
+ convert DCIM/DSC_0189.jpg -resize 100x DSC_0189.mini.jpg
() + for file in '$(find DCIM -iname '\''*.jpg'\'''
++ basename DCIM/DSC_0062.jpg .jpg
+ convert DCIM/DSC_0062.jpg -resize 100x DSC_0062.mini.jpg

В этом примере для формирования результирующих имен файлов используется подстановка вывода команды basename(1) для отрезания «расширений» .jpg от имен файлов, к которым затем приклеиваются новые «расширения» .mini.jpg.

В примере из листинга 5.46 составной список for используется вместе с подстановкой команды seq(1), формирующей список чисел 1, ..., 254, очередные значения из которого принимает переменная node. На каждой итерации цикла () используется подстановка значения $node для формирования IP-адреса очередного узла локальной сети, доступность которого проверяется при помощи команды ping(1).

Листинг 5.46. Цикл с параметром: проверка доступности узлов локальной сети

bender@ubuntu:~$ for node in $(seq 1 254)
> do