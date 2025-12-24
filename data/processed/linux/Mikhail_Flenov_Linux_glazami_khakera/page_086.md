---
source_image: page_086.png
page_number: 86
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.67
tokens: 7484
characters: 813
timestamp: 2025-12-24T04:20:55.710064
finish_reason: stop
---

Добро пожаловать в Linux

![Настройка автозагрузки](../images/ch3_2.png)

Рис. 3.2. Настройка автозагрузки

А для запуска делаем то же самое, только с параметром start:
sudo /etc/init.d/apache2 start

На рис. 3.3 показаны результаты выполнения этих команд.

Состояние сервисов можно просматривать и с помощью команды status:
sudo status cups

В данном случае я запрашиваю состояние сервиса cups, который отвечает за печать.
А для управления сервисом можно использовать команду service:
sudo service cups start
sudo service cups stop
sudo service cups restart

Думаю, что какие-то дополнительные комментарии тут излишни.
Чтобы просмотреть состояние всех установленных служб в данный момент, надо выполнить команду:
sudo service --status-all
или:
sudo initctl list

Команды немного разные, и вывод у них отличается.