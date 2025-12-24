---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.31
tokens: 5926
characters: 1155
timestamp: 2025-12-24T04:08:10.195463
finish_reason: stop
---

MX, NS, PTR, SIG, SOA и тому подобные.
$ host -t MX redhat.com
redhat.com mail is handled by 20 mx2.redhat.com.
redhat.com mail is handled by 10 mx1.redhat.com.

Если команда host не делает того, что вы хотите, то попробуйте использовать команду dig, еще одну мощную утилиту DNS-поиска. Также вы можете встретить команду nslookup, которая устарела в наши дни, но ее все еще можно найти в некоторых Linux- и Unix-системах.

whois [опции] имя_домена    jwhois
/usr/bin    stdin stdout -file -opt -help --version

Команда whois осуществляет поиск регистрационной информации Интернет-домена:

$ whois redhat.com
Registrant:
Red Hat, Inc. (REDHAT-DOM)

P.O. Box 13588
Research Triangle Park, NC 27709

Возможно, вы увидите несколько страниц текста отказа регистратора от обязательств до или после того, как появится нужная информация.

Полезные опции
-h регистратор    Выполнить поиск на сервере заданного регистратора. Например,
                  whois -h whois.networksolutions. com yahoo.com.
-р порт           Запросить заданный TCP-порт вместо стандартного порта43 (служба whois)

ping [опции\ хост iputils
/bin    stdin stdout -file -opt --help --version