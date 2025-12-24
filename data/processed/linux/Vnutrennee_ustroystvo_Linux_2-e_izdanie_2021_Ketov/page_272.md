---
source_image: page_272.png
page_number: 272
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.24
tokens: 7603
characters: 2011
timestamp: 2025-12-24T04:39:44.598430
finish_reason: stop
---

Для отправки сообщений используются учетная запись пользователя lumpy.moose и сервер «исходящих» сообщений smtp.yandex.ru, принимающий почту по протоколу SMTPS (1), а для чтения писем из почтового ящика пользователя lumpy.moose могут быть использованы протоколы IMAPs (2) или POPs (3) и серверы «входящих» сообщений imap.yandex.ru и pop.yandex.ru, соответственно.

Листинг 6.22. Обработка почты публичной почтовой службой

1 lumpy@ubuntu:~$ mutt -s Тест dketov@gmail.com
lumpy@ubuntu:~$ cat ~/.muttrc
set from=lumpy.moose@yandex.ru
set smtp_url=smtpls://lumpy.moose@smtp.yandex.ru

2 lumpy@ubuntu:~$ mutt -f imaps://lumpy.moose@imap.yandex.ru

Определяется адрес сервера imap.yandex.ru...
Устанавливается соединение с imap.yandex.ru...
SSL/TLS-соединение с использованием TLS1.3 (ECDHE-RSA/AES-256-GCM/AEAD)
Пароль для lumpy.moose@imap.yandex.ru: ...

<table>
  <tr>
    <th>q:Выход</th>
    <th>d:Удалить</th>
    <th>u:Восстановить</th>
    <th>s:Сохранить</th>
    <th>m:Создать</th>
    <th>r:Ответить</th>
    <th>g:Всем</th>
  </tr>
  <tr>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Jan 07 Яндекс (9,9К) Соберите всю почту в этот ящик</td>
  </tr>
  <tr>
    <td>2</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Jan 07 Команда Яндекс. (15К) Как читать почту с мобильного</td>
  </tr>
  <tr>
    <td>3</td>
    <td>N + Маг 30 Яндекс.Паспорт (8,4К)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Доступ к аккаунту восстановлен</td>
  </tr>
</table>

3 lumpy@ubuntu:~$ mutt -f pops://lumpy.moose@pop.yandex.ru

6.4.3. Служба WWW

Служба W:[WWW] знакома каждому современному пользователю и в комментариях особо не нуждается. Одной ее заметной особенностью в Linux, пожалуй, является существование терминальных Web-браузеров links(1), lynx(1), elinks(1) и w3m(1), позволяющих работать с «текстовой» частью гипертекстовых Web-ресурсов, что проиллюстрировано с помощью lynx(1) в примере из листинга 6.23.