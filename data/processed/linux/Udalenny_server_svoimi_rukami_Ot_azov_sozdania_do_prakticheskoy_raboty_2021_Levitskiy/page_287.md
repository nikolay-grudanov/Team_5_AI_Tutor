---
source_image: page_287.png
page_number: 287
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.63
tokens: 6221
characters: 847
timestamp: 2025-12-24T04:02:20.583096
finish_reason: stop
---

16.4.5. Автоматическое обновление сертификата

Наш сертификат будет действителен в течение 90 дней, после чего должен быть обновлен. Для обновления можно использовать следующий сценарий renew-letsencrypt.sh:

#!/bin/sh

cd /opt/letsencrypt/
./certbot-auto --config /etc/letsencrypt/configs/my-domain.conf certonly

if [ $? -ne 0 ]
then
    ERRORLOG=`tail /var/log/letsencrypt/letsencrypt.log`
    echo -e "The Let's Encrypt cert has not been renewed!\n\n"
    $ERRORLOG
else
    nginx -s reload
fi

exit 0

В расписание cron нужно добавить строку:

0 0 1 JAN,MAR,MAY,JUL,SEP,NOV * /path/to/renew-letsencrypt.sh

И не забудьте создать каталог /var/log/letsencrypt/ (если он еще не создан) и изменить соответствующим образом права доступа (пользователь, от имени которого выполняется обновление сертификата должен иметь право писать в этот каталог).