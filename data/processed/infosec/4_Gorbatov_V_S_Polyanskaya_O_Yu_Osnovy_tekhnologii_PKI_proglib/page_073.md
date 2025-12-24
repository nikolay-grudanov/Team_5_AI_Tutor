---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.31
tokens: 5234
characters: 1981
timestamp: 2025-12-23T23:29:13.574491
finish_reason: stop
---

Таблица 4.1. Формат сертификата X.509

<table>
  <tr>
    <th>Элемент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>version</td>
    <td>Версия (0 означает v1, 2 означает v3)</td>
  </tr>
  <tr>
    <td>serialNumber</td>
    <td>Серийный номер сертификата</td>
  </tr>
  <tr>
    <td>signature.algorithm<br>Identifier<br>algorithm parameters</td>
    <td>Тип алгоритма подписи<br>Алгоритм<br>Параметры</td>
  </tr>
  <tr>
    <td>issuer</td>
    <td>Уникальное название УЦ, выпустившего сертификат</td>
  </tr>
  <tr>
    <td>Validity<br>NotBefore<br>notAfter</td>
    <td>Период действия<br>Дата и время начала действия<br>Дата и время окончания действия</td>
  </tr>
  <tr>
    <td>subject</td>
    <td>Уникальное имя субъекта</td>
  </tr>
  <tr>
    <td>SubjectPublicKeyInfo<br>Algorithm<br>subjectPublicKey</td>
    <td>Информация об открытом ключе субъекта<br>Криптографический алгоритм<br>Ключ (строка битов)</td>
  </tr>
  <tr>
    <td rowspan="2">Версия v2</td>
    <td>issuerUniqueID</td>
    <td>Уникальный идентификатор центра, выпускающего сертификат</td>
  </tr>
  <tr>
    <td>subjectUniqueID</td>
    <td>Уникальный идентификатор субъекта</td>
  </tr>
  <tr>
    <td rowspan="3">Версия v3</td>
    <td>AuthorityKeyIdentifier<br>keyIdentifier<br>authorityCertIssuer<br>authorityCertSerialNumber</td>
    <td>Идентификатор ключа УЦ<br>Идентификатор ключа<br>Общее название УЦ<br>Серийный номер сертификата УЦ</td>
  </tr>
  <tr>
    <td>subjectKeyIdentifier</td>
    <td>Идентификатор, используемый тогда, когда субъект имеет более одного ключа (например, во время возобновления сертификата)</td>
  </tr>
  <tr>
    <td>keyUsage<br>digitalSignature<br>nonRepudiation<br>keyEncipherment<br>dataEncipherment</td>
    <td>Применение ключа (строки битов)<br>1. Формирование и проверка цифровой подписи<br>2. Неотказуемость<br>3. Шифрование других ключей<br>4. Шифрование и расшифрование данных и контроль целостности с использованием имитозащиты.</td>
  </tr>
</table>