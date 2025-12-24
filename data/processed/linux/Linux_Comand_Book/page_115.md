---
source_image: page_115.png
page_number: 115
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.44
tokens: 5944
characters: 1269
timestamp: 2025-12-24T04:07:04.363759
finish_reason: stop
---

diff [опции] файл1 файл2        diffutils
/usr/bin    stdin stdout -file —opt --help -version

Команда diff сравнивает два файла построчно, либо сравнивает директории. Сравнивая два текстовых файла, diff может создавать детальный отчет об их различиях. В случае бинарных файлов команда diff сообщает лишь о том, различны они или нет. Если различий нет, diff не создает выходных данных; это верно для любых типов файлов.

Традиционный формат выходных данных выглядит следующим образом.

Номера строк и тип изменения
< Соответствующий раздел файла file 1, если он есть
> Соответствующий раздел файла fde2, если он есть Например, сначала мы имеем файл/z/e_a.

Hello, this is a wonderful file.
The quick brown fox jumped over
the lazy dogs.
Goodbye for now.

Представьте себе, что мы удалили первую строку, заменили слово "brown" на "blue" во второй строке и добавили строку в конец, создав файл filejb.

The quick blue fox jumped over
the lazy dogs.
Goodbye for now.
Linux rOOlz!

Тогда выходные данные команды diff file_a file_b будут следующими.

1, 2cl строки 1-2 файла filea перейти в строку 1 файла file_b
<Hello, this is a wonderful file. Строки
1-2 файла file_a
<The quick brown fox jumped over
разделитель diff
>The quick blue fox jumped over Строка
1 файла filejb