---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.08
tokens: 5941
characters: 1046
timestamp: 2025-12-24T04:07:14.389528
finish_reason: stop
---

же завершать работу и возвращать код ошибки; 0, если файлы одинаковые, 1 - если отличаются (или другое значение, если сравнение не было выполнено по какой-либо причине)

md5sum файлы | --check файл coreutils
/usr/bin    stdin stdout -file —opt -help —version
Команда md5sum выводит 32-байтную контрольную сумму для заданных файлов, используя алгоритм MD5 (более подробная информация на http://www.faqs.org/rfcs/rfc 1321 .html).

$ md5sum myfile
dd63 602dflcceb57 96 6d085524c3 980f
myfile

Два разных файла весьма маловероятно будут иметь одинаковую контрольную сумму MD5, поэтому сравнение контрольных сумм - это достаточно надежный способ определить различие файлов:

$ md5sum myfile1 > suml
$ md5sum myfile2 > sum2
$ diff -q suml sum2
Files suml and sum2 differ
Файлы suml и sum2 различаются
или что набор файлов изменился, с помощью опции --check:
$ md5sum file1 file2 file3 > mysum
$ md5sum --check mysum
file1: OK   :
file2: OK
file3 : OK  ',...-
$ echo "новые данные" > file2
$ md5sum --check mysum
file1: OK
file2: FAILED
file3 : OK   ...