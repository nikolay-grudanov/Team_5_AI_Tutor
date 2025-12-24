---
source_image: page_084.png
page_number: 84
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.88
tokens: 5063
characters: 1588
timestamp: 2025-12-23T23:29:25.414248
finish_reason: stop
---

стных дополнений, которые дают возможность проверить САС всем желающим.

В зависимости от типа САС определены дополнения списка CRL Extensions, к ним относятся CRL Number, Authority Key Identifier, Issuer Alternative Name, Issuing Distribution Point и Delta CRL Indicator.

Таблица 4.2. Формат списка аннулированных сертификатов

<table>
  <tr>
    <th>Версия</th>
    <th>Элемент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td rowspan="4">v1</td>
    <td><b>signature.algorithmIdentifier</b></td>
    <td>Тип подписи</td>
  </tr>
  <tr>
    <td><b>issuer</b></td>
    <td>Уникальное имя УЦ-издателя САС</td>
  </tr>
  <tr>
    <td><b>thisUpdate</b></td>
    <td>Дата выпуска данного САС</td>
  </tr>
  <tr>
    <td><b>nextUpdate</b></td>
    <td>Планируемая дата следующего САС</td>
  </tr>
  <tr>
    <td rowspan="7">v2</td>
    <td><b>version</b></td>
    <td>Версия (без номера означает v1, 1 означает v2)</td>
  </tr>
  <tr>
    <td>AuthorityKeyIdentifier<br>KeyIdentifier<br>AuthorityCertIssuer<br>authorityCertSerialNumber</td>
    <td>Идентификатор ключа, используемого для подтверждения САС</td>
  </tr>
  <tr>
    <td><b>cRLNumber</b></td>
    <td>Серийный номер списка аннулированных сертификатов</td>
  </tr>
  <tr>
    <td>issuingDistributionPoint<br>distributionPoint<br>onlyContainsUserCerts<br>onlyContainsCACerts<br>onlySomeResons<br>indirectCRL</td>
    <td>Атрибуты выпускающего пункта распространения САС</td>
  </tr>
  <tr>
    <td><b>deltaCRLIndicator</b></td>
    <td>Индикатор разностного списка аннулированных сертификатов (дельта-списка)</td>
  </tr>
</table>