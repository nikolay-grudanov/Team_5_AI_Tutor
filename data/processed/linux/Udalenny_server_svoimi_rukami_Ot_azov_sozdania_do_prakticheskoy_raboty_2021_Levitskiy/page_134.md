---
source_image: page_134.png
page_number: 134
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.72
tokens: 6229
characters: 848
timestamp: 2025-12-24T03:59:06.344764
finish_reason: stop
---

7.1. Протокол SSH

Особенностью SSH-соединения является шифрование всех передаваемых по нему данных. Если злоумышленник перехватит SSH-трафик, он не узнает, ни логин, ни пароль, ни команды, которые вы передавали на сервер.

В Linux используется свободная реализация протокола SSH - OpenSSH. Данная реализация была определена рабочей группой IETF. Не беспокойтесь: OpenSSH так же безопасен, как и SSH. Далее мы будем говорить SSH, а подразумевать именно OpenSSH.

Для шифрования передаваемых данных SSH-соединение может использовать различные алгоритмы, например, BlowFish, 3DES (Data Encryption Standard), IDEA (International Data Encryption Algorithm) и RSA (Rivest-Shamir-Adelman algorithm). Алгоритм определяется настройками SSH-сервера.

![Приложение Bitvise SSH Client](https://i.imgur.com/3Q5z5QG.png)

Рис. 7.1. Приложение Bitvise SSH Client