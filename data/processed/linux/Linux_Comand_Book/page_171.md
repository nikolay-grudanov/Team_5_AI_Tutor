---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.00
tokens: 5859
characters: 918
timestamp: 2025-12-24T04:08:05.157280
finish_reason: stop
---

$ sftp remote.example.com
Password: **********
sftp> cd MyFiles
sftp> ls
README
file1
file2
file3
sftp> get file2
Fetching /home/smith/MyFiles/file2 to file2
sftp> quit

Если ваше имя пользователя в удаленной системе отлично от вашего имени пользователя в локальной системе, используйте аргумент имя_пользователя@хост:
$ sftp smith@remote.example.com

Команда    Функция

help        Вывести список всех доступных команд
ls          Вывести список файлов в текущей удаленной (ls) или локальной (lls) директории

pwd         вывести имя удаленной (pwd) или локальной (lpwd) рабочей директории
lpwd

cd dir      Сменить вашу удаленную (cd) или локальную (lcd) рабочую директорию на директорию dir
lcd dir

get файл1 [файл2]   Копировать удаленный файл/на локальной компьютер, опционально переименовав его в файл2

put файл1 [файл2]   Копировать локальный файл1 на удаленный компьютер опционально переименовав его в файл2