---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.08
tokens: 7530
characters: 1023
timestamp: 2025-12-24T04:23:33.689314
finish_reason: stop
---

Управление доступом

Local IP address and netmask pairs:
    192.168.77.1 / 0xfffffff00
Default table of environment variables to clear
    BASH_ENV
    ENV
    TERMCAP
    ...
    ...
Default table of environment variables to sanity check
    LANGUAGE
    LANG
    LC_*

Я не стал приводить результат выполнения команды полностью, но основную информацию можно увидеть. Вначале нам сообщается версия программы sudo, в данном случае это 1.6.5.p2. Наиболее интересными в этом листинге являются следующие три строки:

Authentication timestamp timeout: 5 minutes
Password prompt timeout: 5 minutes
Number of tries to enter a password: 3

В первой строке указывается время сохранения пароля в кэше. В данном случае это 5 минут. Если пользователь в течение этого времени снова выполнит команду sudo, то повторно аутентификация проводиться не будет.

Следующая строка указывает время ожидания ввода пароля, а последняя — количество попыток его задать. Если за этот период верный пароль не будет указан, работа программы прервется.