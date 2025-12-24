---
source_image: page_287.png
page_number: 287
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.17
tokens: 11915
characters: 1984
timestamp: 2025-12-24T03:28:16.973996
finish_reason: stop
---

<table>
  <tr>
    <th>make</th>
    <th>ignore</th>
    <td>Игнорировать сигналы прерывания, поступающие с терминала. Выводить их как символ @.</td>
  </tr>
  <tr>
    <th></th>
    <th>ignoreeof</th>
    <td>Не считать символ ^D символом EOF.</td>
  </tr>
  <tr>
    <th></th>
    <th>metoo</th>
    <td>Не удалять отправителя из списка рассылки.</td>
  </tr>
  <tr>
    <th></th>
    <th>noheader</th>
    <td>Идентично параметру командной строки -N.</td>
  </tr>
  <tr>
    <th></th>
    <th>nokerberos</th>
    <td>Получение почты POP по протоколу POP3, а не KPOP.</td>
  </tr>
  <tr>
    <th></th>
    <th>nosave</th>
    <td>Не сохранять незавершенные сообщения в файле dead.letter.</td>
  </tr>
  <tr>
    <th></th>
    <th>pop-mail</th>
    <td>Получение почты по протоколу POP3 и сохранение ее в файле mbox.pop.</td>
  </tr>
  <tr>
    <th></th>
    <th>prompt</th>
    <td>Сменить строку приглашения.</td>
  </tr>
  <tr>
    <th></th>
    <th>Replyall</th>
    <td>Обмен функций Reply и reply.</td>
  </tr>
  <tr>
    <th></th>
    <th>quiet</th>
    <td>Не выводить информацию о версии в начале работы.</td>
  </tr>
  <tr>
    <th></th>
    <th>searchheaders</th>
    <td>При задании спецификатора вида /x:y отображать все сообщения, содержащие строку y в поле заголовка x.</td>
  </tr>
  <tr>
    <th></th>
    <th>verbose</th>
    <td>Идентично параметру командной строки -v.</td>
  </tr>
  <tr>
    <th></th>
    <th>verbose-pop</th>
    <td>Отображать состояние при получении почты POP.</td>
  </tr>
</table>

Специальные файлы

calendar
Содержит даты, уведомление о которых отправляется пользователю системой.

.maildelivery
Файл настройки доставки почтовых сообщений.

.mailrc
Файл настроек работы с почтой.

triplog
Список адресатов, получающих автоматические уведомления.

tripnote
Содержание сообщения автоуведомления.

mailq
mailq [option]
Команда системного администрирования. Перечисление всех сообщений из почтовой очереди sendmail. Эквивалентно sendmail –bp.