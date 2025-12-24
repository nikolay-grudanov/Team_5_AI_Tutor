---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.51
tokens: 6103
characters: 1467
timestamp: 2025-12-24T04:07:14.029759
finish_reason: stop
---

bunzip2 –c file.bz2    Разжать данные в стандартный поток вывода
cat file.bz2| bunzip2 Разжать данные в стандартный поток вывода
bzcat file.bz2        Разжать данные в стандартный поток вывода

tar-файлы, сжатые с помощью bzip2: примеры команд
tar cjf myf ile. tar .bz2  dirname      Упаковать
tar tjf -myf ile. tar .bz2           Вывести список содержимого
tar xjf myf ile. tar .bz2            Распаковать
Добавьте опцию v для команды tar, чтобы выводить имена файлов по мере их обработки.

zip [опции] [файлы]
/usr/bin    stdin stdout -file --opt --help --version
Команды zip и unzip сжимают и разжимают файлы согласно формату Windows Zip. Сжатые файлы имеют суффикс .zip. В отличие от программ gzip, compress и bzip2, программа zip не удаляет исходный файл (файлы).

zipmyfile.zip file1 file2 file3. ...
zip -r myfile.zip dirname
unzip -l myfile.zip
unzip myfile.zip
Упаковать
Упаковать рекурсивно
Вывести список содержимого
Распаковать

uuencode [опции] новый файл входной файл shamb\s
/usr/bin    stdin stdout -file -opt --help --version
До того как появились функции прикрепления файлов к письмам и MIME, приходилось повозиться с бинарными файлами для того, чтобы отправить их по электронной почте. Сначала нужно было преобразовать файл с помощью программы uuencode в ASCII-формат, который выглядит примерно так.

begin 644 myfile
M(R4N8F%S:%]P<F]F:6QE"B,@4G5N<R!F:7)S="!W:&5N(&QO9V=I;F<@:6X6
- M=6YD97(@1TY/344*"G1R874@)
PH@('1E<WO@+6X@(B134TA?04=%3E1?4$E$
end