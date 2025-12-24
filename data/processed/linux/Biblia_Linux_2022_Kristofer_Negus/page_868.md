---
source_image: page_868.png
page_number: 868
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.98
tokens: 7566
characters: 1893
timestamp: 2025-12-24T05:09:34.969890
finish_reason: stop
---

Глава 5. Работа с текстовыми файлами

1. Выполните следующие команды, чтобы создать файл /tmp/services, а затем отредактировать его так, чтобы название WorldWideWeb отображалось как World Wide Web:

$ cp /etc/services /tmp
$ vi /tmp/services
/WorldWideWeb <Enter>
cwWorld Wide Web <Esc>

Следующие две строки показывают исходный текст и результат:

http        80/tcp    www www-http    # WorldWideWeb HTTP
http        80/tcp    www www-http    # World Wide Web HTTP

2. Один из способов переместить абзац в файл /tmp/services — это найти первую строку абзаца, удалить пять строк (5dd), перейти к концу файла (G) и вставить текст (p):

$ vi /tmp/services
/Note that it is<Enter>
5dd
G
p

3. Чтобы использовать режим ex для поиска термина tcp (чувствительного к регистру) в файле /tmp/services и изменить его на WHATEVER, введите следующее:

$ vi /tmp/services
:g/tcp/s//WHATEVER/g<Enter>

4. Чтобы найти в каталоге /etc каждый файл с именем passwd и перенаправить ошибки из поиска в каталог /dev/null, введите следующее:

$ find /etc -name passwd 2> /dev/null

5. Создайте в своем домашнем каталоге каталог TEST. Создайте в нем файлы с именем one, two и three, которые имеют полные права на чтение/запись/выполнение для всех (пользователя, группы и др.). Введите команду find, которая найдет эти файлы и любые другие файлы, имеющие права на запись, открытые для «других» из вашего домашнего каталога и расположенные ниже:

$ mkdir $HOME/TEST
$ touch $HOME/TEST/{one,two,three}
$ chmod 777 $HOME/TEST/{one,two,three}
$ find $HOME -perm -002 -type f -ls
148120  0 -rwxrwxrwx   1 chris chris 0 Jan  1 08:56 /home/chris/TEST/two
148918  0 -rwxrwxrwx   1 chris chris 0 Jan  1 08:56 home/chris/TEST/three
147306  0 -rwxrwxrwx   1 chris chris 0 Jan  1 08:56 /home/chris/TEST/one

6. Найдите в каталоге /usr/share/doc файлы, которые не изменялись более чем 300 дней:

$ find /usr/share/doc -mtime +300