---
source_image: page_187.png
page_number: 187
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.91
tokens: 7603
characters: 1903
timestamp: 2025-12-24T03:06:01.049914
finish_reason: stop
---

В предыдущем разделе мы запустили сервис и с помощью утилиты curl выполнили несколько запросов к нему, так что можно посмотреть, что показывают журналы:

$ journalctl -u hello-world
-- Logs begin at Mon 2019-04-15 09:05:11 EDT, end at Tue 2019-04-23
Apr 23 13:44:20 srv1 systemd[1]: Started hello world pecan service.
Apr 23 13:44:44 srv1 pecan[23980] [INFO    ] [pecan.commands.serve] GET / 200
Apr 23 13:44:55 srv1 systemd[1]: Stopping hello world pecan service...
Apr 23 13:44:55 srv1 systemd[1]: hello-world.service: Main process exited
Apr 23 13:44:55 srv1 systemd[1]: hello-world.service: Succeeded.
Apr 23 13:44:55 srv1 systemd[1]: Stopped hello world pecan service.

Флаг -u задает юнит, в данном случае hello-world, но можно также использовать шаблон или даже указать несколько юнитов.

Зачастую, чтобы следить за записями в журнале, применяют команду tail. Ее вызов выглядит примерно так:

$ tail -f pecan-access.log

Команда, делающая то же самое с помощью journalctl, выглядит несколько иначе, но работает точно так же:

$ journalctl -fu hello-world
Apr 23 13:44:44 srv1 pecan[23980][INFO][pecan.commands.serve] GET / 200
Apr 23 13:44:44 srv1 pecan[23980][INFO][pecan.commands.serve] GET / 200
Apr 23 13:44:44 srv1 pecan[23980][INFO][pecan.commands.serve] GET / 200

Если доступен пакет systemd с движком pcre2, можно воспользоваться подкомандой --grep для дальнейшей фильтрации записей журнала в соответствии с шаблоном.

Флаг -f служит для того, чтобы следить за журналом, он начинает с самых недавних записей и продолжает отображать записи по мере их появления аналогично tail -f. В промышленной эксплуатации количество журналов может быть слишком велико, а ошибки могли появиться, например, сегодня. В подобных случаях можно применить сочетание флагов --since и --until. Оба флага принимают несколько видов параметров:

● today;
● yesterday;
● "3 hours ago";
● -1h;
● -15min;
● -1h35min.