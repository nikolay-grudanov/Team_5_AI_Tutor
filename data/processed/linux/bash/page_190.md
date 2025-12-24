---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.49
tokens: 8243
characters: 2501
timestamp: 2025-12-23T23:09:12.160865
finish_reason: stop
---

Для визуализации вывода из weblogfmt.sh можно использовать таблицу, представленную на рисунке 12.2. В этой таблице приведены данные из access.log, где указаны IP-адрес, дата и время запроса, URL, статус кода ответа, размер файла и User Agent.

Таблица:

<table>
  <tr>
    <th>IP Address</th>
    <th>Date</th>
    <th>URL Requested</th>
    <th>Status Code</th>
    <th>Size</th>
    <th>Referer</th>
    <th>User Agent</th>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /"</td>
    <td>200</td>
    <td>2377</td>
    <td>"-"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /backblue.gif"</td>
    <td>200</td>
    <td>4529</td>
    <td>"http://192.168.0.35/"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /fade.gif"</td>
    <td>200</td>
    <td>1112</td>
    <td>"http://192.168.0.35/"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /favicon.ico"</td>
    <td>404</td>
    <td>503</td>
    <td>"-"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /index.html"</td>
    <td>200</td>
    <td>6933</td>
    <td>"-"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /favicon.ico"</td>
    <td>404</td>
    <td>504</td>
    <td>"-"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /files/main_styleleaf0e.css?1509483497"</td>
    <td>200</td>
    <td>5022</td>
    <td>"http://192.168.0.35/index.html"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
  <tr>
    <td>192.168.0.37 [12/Nov 2017:15:52:59 -0500]</td>
    <td>"GET /files/theme/mobile49c2.js?1490908488"</td>
    <td>200</td>
    <td>3413</td>
    <td>"http://192.168.0.35/index.html"</td>
    <td>"Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0"</td>
  </tr>
</table>

Рис. 12.2. Визуализация вывода из weblogfmt.sh