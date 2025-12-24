---
source_image: page_277.png
page_number: 277
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.65
tokens: 6149
characters: 561
timestamp: 2025-12-24T04:02:00.975219
finish_reason: stop
---

15.8. Защита сервера Apache

По окончании настройки сервера запретим изменение и удаление файла конфигурации apache2.conf:

sudo chattr +i /etc/apache2/apache2.conf

После этого вы (и никто другой) не сможете изменить этот файл, даже с помощью конфигуратора. Если изменить файл все же нужно, снимите атрибут:

sudo chattr -i /etc/apache2/apache2.conf

Не нужно, чтобы посторонние глаза смогли посмотреть, а руки — изменить (и выполнить) файлы, находящиеся в каталогах /etc/apache2 и /var/log/apache2:

sudo chmod 700 /etc/apache2
sudo chmod 700 /var/log/apache2