---
source_image: page_332.png
page_number: 332
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.61
tokens: 6125
characters: 473
timestamp: 2025-12-24T04:03:14.934893
finish_reason: stop
---

php bin/magento setup:static-content-deploy -f

Для дополнительной информации о режиме разработчика обратитесь к документации Magento.

18.5.7. Настройка MySQL

При настройке MySQL обратите внимание на параметры раздела Fine Tuning. Опять тут все зависит от размера вашей базы данных и от размера оперативной памяти. На рис. 18.10 приведена конфигурация рабочего сервера.

![Конфигурация MySQL для Magento](../images/ch18_10.png)

Рис. 18.10. Конфигурация MySQL для Magento