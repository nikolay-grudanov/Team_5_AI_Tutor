---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.45
tokens: 7406
characters: 1622
timestamp: 2025-12-24T04:50:46.440917
finish_reason: stop
---

иначе изменится только первое вхождение Mac в каждой строке. Затем выходные данные отправляются в файл fixed_file.txt. Выходные данные из sed поступают в stdout, поэтому команда перенаправляет их в файл для сохранности:

$ sed 's/Mac/Linux/g' somefile.txt > fixed_file.txt

Можно получить тот же результат, используя конвейер:

$ cat somefile.txt | sed 's/Mac/Linux/g' > fixed_file.txt

При поиске шаблона и замене его пустым шаблоном исходный удаляется. В примере выполняется поиск содержимого файла somefile.txt и лишние пробелы в конце каждой строки (s/ *$) заменяются на «ничего» (//). Выходные данные отправляются в файл fixed_file.txt:

$ cat somefile.txt | sed 's/ *$//' > fixed_file.txt

Простые скрипты оболочки

Иногда самые простые скрипты оказываются самыми полезными. Если приходится вводить одну и ту же последовательность команд повторно, имеет смысл сохранить эти команды (один раз!) в файле. В следующих разделах мы рассмотрим несколько простых, но полезных скриптов оболочки.

Телефонный список

Эта идея передавалась из поколения в поколение еще со времен хакеров UNIX. Скрипт действительно довольно простой, но в нем используются некоторые из концепций, описанных ранее:

#!/bin/bash
# (@)/ph
# A very simple telephone list
# Type "ph new name number" to add to the list, or
# just type "ph name" to get a phone number

PHONELIST=~/.phonelist.txt

# If no command line parameters ($#), there
# is a problem, so ask what they're talking about.
if [ $# -lt 1 ] ; then
    echo "Whose phone number did you want? "
    exit 1
fi

# Did you want to add a new phone number?
if [ $1 = "new" ] ; then
    shift