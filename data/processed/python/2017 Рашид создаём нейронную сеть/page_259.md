---
source_image: page_259.png
page_number: 259
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.83
tokens: 6395
characters: 909
timestamp: 2025-12-24T02:15:12.323659
finish_reason: stop
---

Я буду использовать модель Raspberry Pi Zero, поскольку она еще дешевле и миниатюрнее, чем обычные устройства Raspberry Pi, и это делает задачу развертывания на ней нейронной сети еще более интересной. Стоит эта модель около 5 долларов. Это не опечатка!
Ниже представлена фотография моего устройства с двухпенсовой монетой для сравнения.

![Фотография Raspberry Pi Zero с двухпенсовым монетой](../images/raspberry_pi_zero_with_coin.jpg)

Установка IPython

Далее предполагается, что питание вашего Raspberry Pi включено, а клавиатура, мышь, дисплей и подключение к Интернету работают нормально.
Существует несколько дистрибутивов операционных систем для Raspberry Pi, но мы будем ориентироваться на Raspbian — версию популярного дистрибутива Debian Linux, оптимизированную для аппаратных возможностей Raspberry Pi и доступную для загрузки по следующему адресу:

https://www.raspberrypi.org/downloads/raspbian/