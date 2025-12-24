---
source_image: page_874.png
page_number: 874
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.96
tokens: 7478
characters: 1838
timestamp: 2025-12-24T05:09:45.379411
finish_reason: stop
---

3. Чтобы найти в каталоге /var/spool все файлы, принадлежащие пользователям, отличным от суперпользователя, и вывести их длинный список, введите следующее (я рекомендую войти от имени суперпользователя, чтобы найти недоступные для других пользователей файлы):

$ su -
Password: **********
# find /var/spool -not -user root -ls | less

4. Чтобы стать суперпользователем и создать пустой или обычный текстовый файл с именем /mnt/test.txt, введите следующее:

$ su -
Password: **********
# touch /mnt/test.txt
# ls -l /mnt/test.txt
-rw-r--r--. 1 root root 0 Jan 9 21:51 /mnt/test.txt

5. Чтобы стать суперпользователем и отредактировать файл /etc/sudoers так, чтобы ваша обычная учетная запись пользователя (например, bill) получала полные привилегии суперпользователя с помощью команды sudo, введите:

$ su -
Password: **********
# visudo
o
bill    ALL=(ALL)      ALL
Esc ZZ

Поскольку команда visudo открывает файл /etc/sudoers в редакторе vi, в примере вводится параметр o, который открывает строку, а затем пишет в ней, чтобы дать пользователю bill полные привилегии суперпользователя.

После ввода строки нажмите клавишу Esc, чтобы вернуться в командный режим, и введите ZZ, чтобы записать и выйти.

6. Чтобы с помощью команды sudo создать файл /mnt/test2.txt и убедиться, что он находится там и принадлежит суперпользователю, введите следующее:

[bill]$ sudo touch /mnt/test2.txt
We trust you have received the usual lecture from the local System Administrator. It usually boils down to these three things:
    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.
[sudo] password for bill: **********
[bill]$ ls -l /mnt/text2.txt
-rw-r--r--. 1 root root 0 Jan 9 23:37 /mnt/text2.txt

7. Чтобы смонтировать и размонтировать USB-накопитель и просмотреть системный журнал: