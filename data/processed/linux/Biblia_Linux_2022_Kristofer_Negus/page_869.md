---
source_image: page_869.png
page_number: 869
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.03
tokens: 7546
characters: 1921
timestamp: 2025-12-24T05:09:38.790055
finish_reason: stop
---

7. Создайте каталог /tmp/FILES. Найдите в каталоге /usr/share все файлы размером более 5 и менее 10 Мбайт и скопируйте их в каталог /tmp/FILES:

$ mkdir /tmp/FILES
$ find /usr/share -size +5M -size -10M -exec cp {} /tmp/FILES \;
$ du -sh /tmp/FILES/*
6.6M   /tmp/FILES/BidiCharacterTest.txt
7.6M   /tmp/FILES/BidiTest.txt
5.2M   /tmp/FILES/day.jpg

8. Найдите в каталоге /tmp/FILES все файлы и сделайте резервную копию каждого здесь же. Используйте существующее имя каждого файла и добавьте файл .mybackup для создания резервных копий:

find /tmp/FILES/ -type f -exec cp {} {}.mybackup \;

9. Установите пакет kernel-doc в Fedora или Red Hat Enterprise Linux. Используя команду grep, найдите в файлах, содержащихся в каталоге /usr/share/doc/kernel-doc*, термин e1000 (без учета регистра) и перечислите имена файлов, содержащих его:

# yum install kernel-doc
$ cd /usr/share/doc/kernel-doc*
$ grep -rli e1000 .
./Documentation/powerpc/booting-without-of.txt
./Documentation/networking/e100.txt
...

10. Снова найдите термин e1000 в том же месте. Однако на этот раз перечислите каждую строку, содержащую термин, и выделите его цветом:

$ cd /usr/share/doc/kernel-doc-*
$ grep -ri --color e1000 .

Глава 6. Управление активными процессами

1. Чтобы перечислить все процессы, запущенные в вашей системе, с полным набором столбцов и передать выходные данные в команду less, введите следующее:

$ ps -ef | less

2. Чтобы перечислить все процессы, запущенные в системе, и отсортировать их по имени пользователя, выполняющего каждый процесс, введите следующее:

$ ps -ef --sort=user | less

3. Чтобы вывести список всех процессов, запущенных в системе, со столбцами имени, идентификатора процесса, имени пользователя, названия группы, приоритета, размера виртуальной памяти, размера оперативной памяти и команды, введите следующее:

$ ps -eo 'pid,user,group,nice,vsz,rss,comm' | less
PID USER    GROUP    NI    VSZ    RSS COMMAND