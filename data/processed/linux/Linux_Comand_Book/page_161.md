---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.51
tokens: 5931
characters: 1050
timestamp: 2025-12-24T04:08:05.197507
finish_reason: stop
---

/bin    stdin stdout -file --opt -help -version

Команда uname выводит основную информацию о вашем компьютере:

$ uname -a
Linux server.example.com 2.4.18-27.8.0 #1 Fri Mar 14 06:45:49 EST 2003 1686 i686 i386 GNU/Linux

Выходные данные включают в себя название ядра (Linux), имя хоста (server.example.com), версию ядра (2.4.18-27.8.0 #1 Fri Mar 14 06:45:49 EST 2003), название аппаратной платформы (1686), тип процессора (i686), аппаратную платформу (i386) и название операционной системы (GNU/Linux).

Полезные опции
-а    Вся информация
- s   Только название ядра (по умолчанию)
-п   Только имя хоста
- г   Только версию ядра
-т   Только название аппаратной платформы
-р   Только тип процессора
- i   Только аппаратную платформу
- о   Только название операционной системы

hostname [опции] [имя] net-tools
/bin    stdin stdout -file --opt --help --version

Команда hostname выводит имя вашего компьютера. В зависимости от ваших настроек это может быть полностью определенное имя хоста:

$ hostname
myhost.example.com

или короткое имя вашего хоста: