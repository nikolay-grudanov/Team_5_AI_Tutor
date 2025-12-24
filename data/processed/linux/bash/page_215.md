---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.11
tokens: 7537
characters: 1538
timestamp: 2025-12-23T23:09:56.514983
finish_reason: stop
---

Должны быть закодированы Base64 — стандартом кодирования данных с помощью только 64 символов ASCII. Кодировка Base64 важна из-за способа, с помощью которого зашифрованный текст позже будет расшифрован. Наконец, опция -pass используется для указания ключа шифрования.

Вывод из OpenSSL, который является зашифрованной версией сценария innerscript.sh, выглядит следующим образом:

U2FsdGVkX18WvDOyPFcvyvAozJHS3tjrZIPlZM9xRhz0tuwzDrKhKBBuugLxzp7T MoJoqx02tX7KLhATS0Vqgze1C+kzFxtKyDAh9Nm2N0HXfSNuo9YfYD+15DoXEGPd

Создание оболочки

Теперь, когда внутренний сценарий зашифрован и представлен в формате Base64, вы можете написать для него оболочку. Основная задача оболочки в том, чтобы сначала расшифровать внутренний сценарий (при наличии соответствующего ключа), а затем выполнить.

В идеале расшифровка и выполнение сценария должны происходить в оперативной памяти. Следует избегать записи незашифрованного сценария на жесткий диск, так как позже его могут найти и проанализировать посторонние. Такой сценарий оболочки показан в примере 14.6.

Пример 14.6. wrapper.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# wrapper.sh
#
# Описание:
# Пример выполнения зашифрованного «обернутого» скрипта
#
# Использование:
# wrapper.sh
#   Ввести пароль при появлении запроса
#
encrypted='U2FsdGVkX18WvDOyPFcvyvAozJHS3tjrZIPlZM9xRhz0tuwzDrKhKBBuugLxzp7T MoJoqx02tX7KLhATS0Vqgze1C+kzFxtKyDAh9Nm2N0HXfSNuo9YfYD+15DoXEGPd' ①

read -s word ②

innerScript=$(echo "$encrypted" | openssl aes-256-cbc -base64 -d -pass pass:"$word") ③

eval "$innerScript" ④