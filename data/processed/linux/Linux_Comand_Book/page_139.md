---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.41
tokens: 5864
characters: 845
timestamp: 2025-12-24T04:07:40.271502
finish_reason: stop
---

$ ps –ux

всех процессов пользователя smith:

$ ps -U smith

всех работающих экземпляров программы program_ пате:

$ ps -C ргодгат_name

процессов в терминале N:

$ ps -tW

конкретных процессов 1, 2 и 3505:
$ ps -pl,2,3505
всех процессов с командными строками, урезанными шириной экрана:
$ ps -ef всех процессов с полными командными строками:
$ ps -efww
и всех процессов в виде дерева, когда дочерние процессы располагаются ниже родительских с отступом:
$ ps -efH
Помните, что вы можете извлекать более лаконичную информацию из выходных данных команды ps, используя команду grep или другие фильтрующие программы.

uptime procps
/usr/bin    stdin stdout -file --opt --help --version

Команда uptime сообщает о том, как долго работает система с момента последней загрузки.

$ uptime
10:54pm up 8 days, 3:44, 3 users,
load average: 0.89, 1.00, 2.15