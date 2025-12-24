---
source_image: page_208.png
page_number: 208
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.11
tokens: 6104
characters: 460
timestamp: 2025-12-24T04:00:30.223990
finish_reason: stop
---

После этого Winbind уже будет работать, но он все еще не интегрирован. Для интеграции Winbind в Linux. Откройте файл /etc/nsswitch.conf и найдите в нем строчки:

passwd: compat
group: compat

Эти строки нужно изменить так:

passwd: compat winbind
group: compat winbind

Раз мы уже настраиваем интеграцию с сетью Microsoft, то не грех и компьютер перезагрузить - по примеру Microsoft. После этого ваш сервер linux станет полноценным членом AD-домена MY.COMPANY.