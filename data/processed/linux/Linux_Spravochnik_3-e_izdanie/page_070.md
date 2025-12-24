---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 73.31
tokens: 12069
characters: 2256
timestamp: 2025-12-24T03:19:00.993280
finish_reason: stop
---

<table>
  <tr>
    <th>gw</th>
    <td>Список адресов шлюзов.</td>
    <th>bootpd</th>
  </tr>
  <tr>
    <th>ha</th>
    <td>Аппаратный адрес узла.</td>
    <th></th>
  </tr>
  <tr>
    <th>hd</th>
    <td>Домашний каталог файла загрузки.</td>
    <th></th>
  </tr>
  <tr>
    <th>hn</th>
    <td>Имя узла для посылки.</td>
    <th></th>
  </tr>
  <tr>
    <th>ht</th>
    <td>Тип аппаратного обеспечения узла (см. RFC Assigned Numbers — назначение номеров).</td>
    <th></th>
  </tr>
  <tr>
    <th>im</th>
    <td>Внедрить список адресов сервера.</td>
    <th></th>
  </tr>
  <tr>
    <th>ip</th>
    <td>IP-адрес узла.</td>
    <th></th>
  </tr>
  <tr>
    <th>lg</th>
    <td>Список адресов log-сервера.</td>
    <th></th>
  </tr>
  <tr>
    <th>lp</th>
    <td>Список адресов lpr-сервера.</td>
    <th></th>
  </tr>
  <tr>
    <th>ns</th>
    <td>Список адресов сервера имен IEN-116.</td>
    <th></th>
  </tr>
  <tr>
    <th>rl</th>
    <td>Список адресов сервера протокола обнаружения ресурсов.</td>
    <th></th>
  </tr>
  <tr>
    <th>sm</th>
    <td>Маска подсети узла.</td>
    <th></th>
  </tr>
  <tr>
    <th>tc</th>
    <td>Продолжение таблицы.</td>
    <th></th>
  </tr>
  <tr>
    <th>to</th>
    <td>Разница во времени с UTC (в секундах).</td>
    <th></th>
  </tr>
  <tr>
    <th>ts</th>
    <td>Список адресов сервера времени.</td>
    <th></th>
  </tr>
  <tr>
    <th>vm</th>
    <td>Волшебный селектор cookie производителей.</td>
    <th></th>
  </tr>
  <tr>
    <td colspan="3">Существует также общий тег Tn, в котором n является номером производителя (по записи производителя из RFC 1048). Общие данные могут представляться либо потоком шестнадцатеричных чисел, либо строками ASCII-символов, заключенными в кавычки.</td>
  </tr>
</table>

bootpgw [options] server

Шлюз протокола загрузки через Интернет (Internet Boot Protocol Gateway). Поддерживает шлюз, направляющий серверу server запросы от bootpd. Обрабатывает пакеты BOOTREPLY, а также пакеты BOOTREQUEST. bootpgw обычно запускается /etc/inetd при включении в /etc/inetd.conf следующей строки:

bootps dgram udp wait root /etc/bootpgw bootpgw

При этом bootpgw запускается только при поступлении запроса на загрузку. bootpgw опознает те же параметры, что и bootpd, кроме -c.