---
source_image: page_398.png
page_number: 398
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.40
tokens: 6161
characters: 637
timestamp: 2025-12-24T04:04:29.480143
finish_reason: stop
---

Запустим Greenlight:

docker-compose up -d

Осталось совсем немного. Нужно создать учетную запись администратора и перезагрузить систему. Создаем учетную запись администратора:

docker exec greenlight-v2 bundle exec rake user:create["me","me@ mail","Password","admin"]

Перезагружаем систему:

sudo shutdown -r now

На рис. 22.1 показана панель управления BBB (для получения доступа к ней перейдите по адресу, сконфигурированному для BBB, в нашем случае это bigbluebutton.example.com). По сути, BBB готова к использованию.

![Панель управления BigBlueButton](../images/ch22_01.png)

Рис. 22.1. bigbluebutton - бесплатные видеоконференции