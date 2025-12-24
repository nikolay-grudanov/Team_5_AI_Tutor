---
source_image: page_375.png
page_number: 375
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.60
tokens: 7376
characters: 1713
timestamp: 2025-12-24T04:42:56.991728
finish_reason: stop
---

тельский» экземпляр' systemd ①, запускаемый «системным» systemd каждому пользователю при его входе в систему.

Несмотря на то что рассмотрение задач администрирования systemd выходит за рамки данной книги, листинги 10.9—10.13 прекрасно иллюстрируют его возможности и назначение. На практике чрезвычайно часто возникает задача мгновенно «поделиться» файлами в «случайной» сети, например с участниками конференции, с партнерами на встрече или заказчиками на воркшопе и в прочих подобных ситуациях. Никогда не известно, какую операционную систему и на каких устройствах они (заказчики) используют — ноутбуки, планшеты, смартфоны, iOS, Android, Windows. Безотказно работает HTTP и MDNS (см. главу 6) в публичной Wi-Fi-сети, однако использование в этой ситуации полнофункционального HTTP-сервера, например W:[Apache HTTP Server] или W:[nginx], абсолютно лишено всякого смысла. В целом задача не нова, и даже существует определенное количество решений, например woof² (web offer one file), но systemd позволяет решить эту задачу в два счета и на языке командного интерпретатора.

Листинг 10.9. Пользовательский Web-сервер на основе bash

morty@ubuntu:~$ cat ~/bin/peerweb
#!/bin/bash
documentroot=$1

read method uri ver
if [ -f $documentroot/$uri ]
then
    echo "HTTP/1.0 200 Ok"
    echo "Content-Type: `file -bi $documentroot/$uri`"
    echo "Content-Size: `stat -c %s $documentroot/$uri`"
    echo
    cat $documentroot/$uri
else
    echo "HTTP/1.0 404 Not found"
    echo
fi

1 Звучит запутанно, но в понятиях systemd все так и есть. Пользовательский экземпляр systemd, управляющий пользовательскими службами, сам является системной службой с названием user@.service.
2 См. http://www.home.unix-ag.org/simon/woof.