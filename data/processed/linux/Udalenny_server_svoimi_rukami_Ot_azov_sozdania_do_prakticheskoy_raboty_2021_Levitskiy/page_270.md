---
source_image: page_270.png
page_number: 270
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.51
tokens: 6457
characters: 1619
timestamp: 2025-12-24T04:02:09.926232
finish_reason: stop
---

<table>
  <tr>
    <th>ScriptAlias</th>
    <td>Аналогична директиве Alias, но позволяет задать месторасположение каталога для CGI-сценариев.</td>
  </tr>
  <tr>
    <th>AddType</th>
    <td>С помощью этой директивы можно добавить новый MIME-тип, который не указан в файле apache-mime.types.</td>
  </tr>
  <tr>
    <th>AddHandler и Action</th>
    <td>Директива AddHandler позволяет сопоставить определенному MIME-типу какой-нибудь обработчик. А с помощью директивы Action можно определить какое-нибудь действие для обработчика. Например, вы можете запустить какую-нибудь программу для обработки файла данного типа. Пример:<br>AddHandler text/dhtml dhtml<br>Action text/dhtml /cgi-bin/dhtml-parse</td>
  </tr>
  <tr>
    <th>ErrorDocument</th>
    <td>Директива, сопоставляющая коды ошибок сервера URL-адресам на этом же сервере.</td>
  </tr>
  <tr>
    <th>Redirect</th>
    <td>Используется для перенаправления с одного адреса на другой</td>
  </tr>
</table>

В таблице 15.3 не рассмотрены директивы Location и Directory, которые заслуживают отдельного разговора. Директива Directory определяет свойства каталога, например:

<Directory />
Options Indexes Includes FollowSymLinks
AllowOverride None
</Directory>

Свойства каталога можно указывать в директиве Directory или в файле .htaccess, который находится в том каталоге, для которого необходимо установить нужные параметры.

В блоке Directory могут находиться директивы управления доступом. К ним относятся директивы AllowOverride, Options, Limit. Рассмотрим по порядку все эти директивы. Директива AllowOverride может принимать значения, указанные в табл. 15.4.