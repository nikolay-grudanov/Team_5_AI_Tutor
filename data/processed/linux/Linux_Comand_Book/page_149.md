---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.07
tokens: 5974
characters: 1285
timestamp: 2025-12-24T04:07:48.777202
finish_reason: stop
---

означает "да", "минус" - "нет", а вопросительный знак означает "неизвестно"
-m    Вывести информацию только о себе, то есть, о пользователе связанном с текущим терминалом
-q    Вывод только имен пользователей и количества пользователей. Выводит почти ту же информацию, что и команда users, но добавляет количество пользователей.

* Если ваша система сконфигурирована для журналирования этих завершенных сессий и неудачных попыток входа в систему.

users [имя файла] coreutils
/usr/bin    stdin stdout -file -opt --help -version

Команда users выводит сжатый список пользователей, имеющих открытые рабочие сессии. Если пользователь работает в нескольких командных процессорах (терминалах), то его имя в списке появится несколько раз.

$ users
barrett jones smith smith smith

Аналогично команде who, команда users по умолчанию получает входные данные из файла /var/ log/utmp, но может читать их и из другого указанного файла.

finger [опции\ [пользователь[@хост\]] finger
/usr/bin    stdin stdout -file —opt -help -version

Команда finger выводит информацию о пользователях в сжатом формате:
$ finger
Login   Name   Tty   Idle Login Time
smith   Sandy Smith :0   Sep 6 17:09
barrett Daniel Barrett :pts/l 24 Sep 6 17:10
jones   Jill Jones :pts/2 Sep 8 20:58
или подробно:
$ finger smith