---
source_image: page_268.png
page_number: 268
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.55
tokens: 6451
characters: 1571
timestamp: 2025-12-24T04:02:04.895576
finish_reason: stop
---

<table>
  <tr>
    <th>AddIconByType</th>
    <td>Сопоставляет значок типу файла. Значок будет использоваться при выводе каталога, если включена директива FancyIndexing. Директива AddIconByType имеет следующий формат:

AddIconByType (TEXT, URL) mime-type

Параметр TEXT определяет текстовое описание типа, которое увидят пользователи, использующие текстовый браузер или пользователи, у которых отключено отображение рисунков. Параметр URL определяет адрес значка, а параметр mime-type -- это тип файла, с которым нужно сопоставить значок. Полный перечень MIME-типов приведен в файле apache-mime.types. В качестве имени файла можно задать не только MIME-тип, но и символы, которыми заканчивается имя файла, но для этого нужно использовать директиву AddIcon вместо AddIconByType.

AddIconByType (VID,/icons/movie.gif) video/*
AddIcon /icons/binary.gif .bin .exe

Первая директива сопоставляет типу video значок /icons/movie.gif. Вторая директива сопоставляет бинарным файлам *.bin и *.exe значок /icons/binary.gif. Значок по умолчанию задается директивой DefaultIcon.</td>
  </tr>
  <tr>
    <th>DefaultType</th>
    <td>Если запрашиваемый клиентом тип не соответствует ни одному из MIME-типов, используется MIME-тип, указанный в директиве DefaultType.</td>
  </tr>
  <tr>
    <th>AddEncoding</th>
    <td>Для сокращения времени передачи файла клиентам используется сжатие данных. Браузеры имеют встроенные программы для распаковки, запускаемые при получении архивов определенных MIME-типов. Именно эти MIME-типы и указываются в директиве AddEncoding.</td>
  </tr>
</table>