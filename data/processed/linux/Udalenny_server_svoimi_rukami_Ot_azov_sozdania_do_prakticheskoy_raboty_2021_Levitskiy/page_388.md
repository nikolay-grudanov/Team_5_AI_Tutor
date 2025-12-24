---
source_image: page_388.png
page_number: 388
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.73
tokens: 6341
characters: 1122
timestamp: 2025-12-24T04:04:24.071587
finish_reason: stop
---

6. Локаль en_US.UTF-8

Подобная конфигурация — не самая дорогая. По сути, любой современный компьютер подойдет под эти требования. Можно даже арендовать VPS, но виртуальный сервер нужной конфигурации обойдется довольно дорого от 3600 р. в месяц, учитывая большой объем накопителя. В этом случае особо нет смысла, поскольку бизнес-тариф для Zoom обойдется дешевле.

Если локаль отличается от en_US.UTF-8 (скорее всего, так оно и есть), перенастроить ее можно с помощью следующих команд:

sudo sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
sudo sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen
sudo dpkg-reconfigure --frontend=noninteractive locales
sudo update-locale LANG=en_US.UTF-8

Убедитесь, что локаль указана в переменных окружения:

sudo systemctl show-environment

Вывод должен быть таким:
LANG=en_US.UTF-8
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

22.4. Установка и настройка системы веб-конференций

Будем считать, что сеть уже настроена и у нас есть доступ к Интернету. Проверим, так ли это, пропинговав сервер Google DNS:

$ ping -c 3 8.8.8.8