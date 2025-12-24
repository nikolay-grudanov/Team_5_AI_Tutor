---
source_image: page_028.png
page_number: 28
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.87
tokens: 7180
characters: 817
timestamp: 2025-12-24T04:32:33.542641
finish_reason: stop
---

Виртуальный терминал tty1
Виртуальный терминал tty2
Виртуальный терминал ttyN
клавиатура
дисплей →
Консоль
← команды
результаты →
Пользователь
Рис. 2.3. Виртуальные терминалы

Узнать имя текущего терминала (а точнее — имя специального файла устройства¹ терминального драйвера, см. листинг 2.1), на котором выполнен вход в систему, позволяет команда tty(1), а список всех терминальных входов пользователей — команды users(1), who(1) и w(1).

Листинг 2.1. Утилиты tty, users, who и w

finn@ubuntu:~$ tty
/dev/tty1
finn@ubuntu:~$ users
bubblegum finn iceking jake jake marceline
finn@ubuntu:~$ who
iceking pts/0      2019-11-16 10:46 (176.10.35.129)
bubblegum tty5     2019-11-16 10:46
marceline tty3     2019-11-16 10:47
finn   tty1        2019-11-16 10:46

¹ Подробнее о специальных файлах устройств см. в разд. 3.2.5.