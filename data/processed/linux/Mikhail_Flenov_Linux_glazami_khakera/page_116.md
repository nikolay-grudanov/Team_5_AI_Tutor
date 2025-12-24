---
source_image: page_116.png
page_number: 116
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.78
tokens: 7622
characters: 1316
timestamp: 2025-12-24T04:21:50.657598
finish_reason: stop
---

ция о нем. Например, следующая команда запрашивает у системы информацию о модуле ext3:

modinfo ext3

В ответ на это мы увидим примерно следующее:

filename: /lib/modules/2.4.18-5asp/kernel/fs/ext3/ext3.o
description: "Second Extended Filesystem with journaling extensions"
author: "Remy Card, Stephen Tweedie, Andrew Morton, Andreas Dilger, Theodore Ts'o and others"
license: "GPL"
parm: do_sync_supers int, description "Write superblocks synchronously"

Таким образом, нам становится известным имя и расположение файла, описание, автор, лицензия и т. д. Количество отображаемой информации сильно зависит от модуля, и, если честно, в некоторых случаях она настолько скудна, что предназначение модуля остается непонятным.

modprobe

Эта команда, в основном, используется системой для загрузки установленных модулей, но можно это делать и самостоятельно. В качестве единственного параметра нужно передать команде имя модуля, который надо загрузить.

Например, следующая команда загружает модуль iptable_nat (о нем мы будем говорить в разд. 4.12):

modprobe iptable_nat

rmmod

Эта команда выгружает модуль, имя которого указано в качестве параметра. Если вы воспользовались модулем для выполнения определенных действий, то не забудьте по окончании работы его выгрузить. Иначе как раз он и может стать причиной взлома.