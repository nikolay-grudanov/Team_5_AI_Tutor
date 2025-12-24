---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.17
tokens: 6002
characters: 1323
timestamp: 2025-12-24T04:07:04.473981
finish_reason: stop
---

gzip [опции] [файл\` stdin stdout -file --opt -help --version

Команды gzip и gunzip сжимают и разжимают файлы в формате GNU Zip. Сжатые файлы имеют суффикс .gz.

Примеры команд
gzip file        Сжать файл file в файл file.gz. Исходный файл удаляется
gzip -c file     Вывести сжатые данные в стандартный поток вывода
cat file | gzip  Сжать данные из конвейера
gunzip file.gz   Разжать файл file.gz в файл. Исходный файл file.gz удаляется
gunzip -c file.gz Разжать данные в стандартный поток вывода
cat file.gz | gunzip Разжать данные из конвейера
zcat file.z      Разжать данные в стандартный поток вывода

tar-файлы, сжатые с помощью gzip: примеры команд
tar czf myf ile. tar .gz dirname    Упаковать директорию dimame
tar tzf myf ile. tar .gz            Вывести список содержимого
tar xzf myf ile. tar .gz            Распаковать
Добавьте опцию v для команды tar, чтобы выводить имена файлов по мере их обработки.

compress [опции] [файлы] /usr/bin stdin stdout -file -opt -help -version
ncompress
Команды compress и uncompress сжимают и разжимают файлы согласно стандартному формату сжатия Unix (Lempel Ziv). Сжатые файлы имеют суффикс .Z.

Примеры команд
compress file        Сжать файл fi1e в файл fi1e.Z.
compress -c file     Исходный файл удаляется
                    Вывести сжатые данные в стандартный поток вывода