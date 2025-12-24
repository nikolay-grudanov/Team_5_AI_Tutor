---
source_image: page_271.png
page_number: 271
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.11
tokens: 7450
characters: 1827
timestamp: 2025-12-24T04:39:41.081251
finish_reason: stop
---

I'm sorry to have to inform you that your message could not be delivered to one or more recipients. It's attached below.

★ <dketov@gmail.com>: host gmail-smtp-in.l.google.com[74.125.205.27] said:
| 550-5.7.1 [95.55.94.237] The IP you're using to send mail is not
| Authorized to 550-5.7.1 send email directly to our servers. Please use the
|   SMTP relay at your 550-5.7.1 service provider   instead. Learn more at 550
| 5.7.1 https://support.google.com/mail/answer/10336 tw4si41552991lbb.77 -
L gsmtp (in reply to end of DATA command)

& q ←
Saved 1 message in /home/lumpy/mbox

lumpy@ubuntu:~$ mail handy@happytreefriends.ru
Cc:
Subject: См. hands(4) ...
... про /dev/hands ;)
^D

lumpy@ubuntu:~$ mailq
-Queue ID- --Size-- ----Arrival Time---- -Sender/Recipient------
BB85027304*    341 Sun Nov 24 00:38:27 lumpy@ubuntu
                handy@happytreefriends.ru

-- 0 Kbytes in 1 Request.

Современные требования к условиям корректной пересылки почтовых сообщений (например, ★ в листинге 6.21) зачастую оказываются чересчур строгими, а содержание собственной локальной почтовой системы — небправданно сложным. В большинстве случаев конечные пользователи пользуются услугами «внешних» почтовых серверов, организующих полный цикл обработки почты — от приема исходящих сообщений до обслуживания почтовых ящиков. Исходящие сообщения отправляются таким серверам с помощью протокола W:[SMTP], а доступ к почтовым ящикам — при помощи протоколов W:[POP3] или W:[IMAP].

В примере из листинга 6.22 показан терминальный клиент современных почтовых систем mutt(1), поддерживающий «защищенные» протоколы электронной почты SMTPs, IMAPs и POPs, использующие протокол W:[SSL]1 для криптозащиты сетевых соединений.

1 Использующий весьма похожие на SSH способы обеспечения конфиденциальности данных и аутентичности взаимодействующих сторон.