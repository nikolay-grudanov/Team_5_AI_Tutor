---
source_image: page_270.png
page_number: 270
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.35
tokens: 7403
characters: 1615
timestamp: 2025-12-24T04:39:36.507561
finish_reason: stop
---

6.4.2. Почтовые службы SMTP, POP/IMAP

Электронная почта, пожалуй, является самым ранним приложением сетевой подсистемы операционных систем семейства UNIX. Изначально электронные письма пересылались непосредственно между конечными сетевыми узлами при помощи службы W:[sendmail] с использованием протокола W:[SMTP], а для отправки или чтения писем применялась утилита mail(1).

Вместо sendmail может быть использована абсолютно любая реализация агента пересылки почты (W:[mail transport agent], MTA¹), например W:[postfix] или W:[exim], но обычно его функцию делегируют почтовым серверам провайдера услуг Интернета или серверам публичных сервисов типа yandex.ru или gmail.com.

Листинг 6.21 иллюстрирует «классическую» схему электронной почты с «локальным» MTA, использующую команду mail(1) для составления исходящих ① и чтения входящих ③ писем и команду mailq(1) для просмотра очередей обработки почты ②.

Листинг 6.21. Обработка почты локальной почтовой системой

① lumpy@ubuntu:~$ mail -s Test dketov@gmail.com
Cc:
Это тест ;)
^D

② lumpy@ubuntu:~$ mailq
Mail queue is empty

③ lumpy@ubuntu:~$ mail
Mail version 8.1.2 01/15/2001. Type ? for help.
"/var/mail/lumpy" : 1 message 1 new
>N 1 MAILER-DAEMON@ubu Thu Jan 7 15:09 77/2653 Undelivered Mail Returned t
& 1
Message 1:
From MAILER-DAEMON Thu Jan 7 15:09:35 2016
X-Original-To: lumpy@ubuntu
Date: Thu, 7 Jan 2016 15:09:35 +0300 (MSK)
From: MAILER-DAEMON@ubuntu (Mail Delivery System)
Subject: Undelivered Mail Returned to Sender
To: lumpy@ubuntu
This is the mail system at host ubuntu.

¹ О всех этих MTA, MDA и MRA см. подробнее здесь: https://tiny.cc/n1yqqz.