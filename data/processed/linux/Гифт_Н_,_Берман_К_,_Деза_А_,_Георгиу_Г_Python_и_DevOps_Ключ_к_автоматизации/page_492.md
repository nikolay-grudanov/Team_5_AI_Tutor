---
source_image: page_492.png
page_number: 492
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.47
tokens: 7081
characters: 440
timestamp: 2025-12-24T03:13:30.312180
finish_reason: stop
---

Подключение срабатывающего по событию триггера CloudWatch

Последний шаг для активации триггера CloudWatch состоит в задании срабатывания генератора сообщений по времени и проверке того, что сообщения поступают в SQS, как показано на рис. 15.13.

![Настройка таймера](../images/ch15_13.png)

Рис. 15.13. Настройка таймера

Теперь в очереди SQS появятся сообщения (рис. 15.14).

![Очередь SQS](../images/ch15_14.png)

Рис. 15.14. Очередь SQS