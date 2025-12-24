---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.26
tokens: 6093
characters: 1061
timestamp: 2025-12-24T10:06:57.902754
finish_reason: stop
---

Глава 6. Интеграционное, нагрузочное и тестирование производительности

![Водопадный график для примера Yahoo.com](https://i.imgur.com/3Q5z5QG.png)

Рис. 6.4. Водопадный график для примера Yahoo.com

Чтобы просмотреть графическое представление вывода YSlow, вам нужна другая программа — YSlow visualizer (визуализатор YSlow), скачать которую можно по адресу: http://www.showslow.com/beacon/yslow/. Данную программу можно также установить локально (http://www.showslow.org/Installation_and_configuration), если вы не хотите отправить ваши YSlow-данные третьей стороне.

Давайте посмотрим, как это все работает вместе. После установки YSlow передайте ему HAR-файл для просмотра результатов на Showslow.com:

% yslow -i all -b http://www.showslow.com/beacon/yslow/yahoo.com.har

Данная команда отправит ваш HAR-вывод из Yahoo.com на ShowSlow.com для визуализации. Затем нам нужно перейти на http://www.showslow.com/ и найти ваш URL в списке последних адресов, чтобы просмотреть полный графический вывод (http://www.showslow.com/details/6005/http://www.yahoo.com/).