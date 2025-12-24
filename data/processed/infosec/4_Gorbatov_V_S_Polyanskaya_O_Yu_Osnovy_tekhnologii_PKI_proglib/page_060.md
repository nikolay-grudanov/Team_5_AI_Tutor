---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.49
tokens: 5440
characters: 2376
timestamp: 2025-12-23T23:29:01.476579
finish_reason: stop
---

3.2. Стандарты Internet X.509 PKI (PKIX)

3.2.1. Терминология и концепции PKIX

Стандарты PKIX для описания инфраструктур используют сходные понятия инфраструктура открытых ключей PKI и инфраструктура управления привилегиями PMI. Главное отличие между ними заключается в том, что PKI управляет сертификатами открытых ключей, а PMI — атрибутными сертификатами. Сертификат открытого ключа можно сравнить с паспортом субъекта, а атрибутный сертификат — с визой, первый обеспечивает идентификацию личности, а второй дает определенное разрешение.

Основные термины и аббревиатуры, используемые в стандартах PKIX, а также их аналоги на русском языке приведены в табл. 3.5.

Таблица 3.5. Термины PKIX

<table>
  <tr>
    <th>Термин на английском языке</th>
    <th>Аббревиатура</th>
    <th>Термин на русском языке</th>
  </tr>
  <tr>
    <td>Attribute Authority</td>
    <td>AA</td>
    <td>Атрибутный центр</td>
  </tr>
  <tr>
    <td>Attribute Certificate</td>
    <td>AC</td>
    <td>Атрибутный сертификат</td>
  </tr>
  <tr>
    <td>Certificate</td>
    <td></td>
    <td>Сертификат</td>
  </tr>
  <tr>
    <td>Certification Authority</td>
    <td>CA</td>
    <td>Удостоверяющий центр (УЦ)</td>
  </tr>
  <tr>
    <td>Certificate Policy</td>
    <td>CP</td>
    <td>Политика применения сертификатов (ППС)</td>
  </tr>
  <tr>
    <td>Certification Practice Statement</td>
    <td>CPS</td>
    <td>Регламент УЦ</td>
  </tr>
  <tr>
    <td>End–Entity</td>
    <td>EE</td>
    <td>Конечный субъект</td>
  </tr>
  <tr>
    <td>Public Key Certificate</td>
    <td>PKC</td>
    <td>Сертификат открытого ключа</td>
  </tr>
  <tr>
    <td>Public Key Infrastructure</td>
    <td>PKI</td>
    <td>Инфраструктура открытых ключей</td>
  </tr>
  <tr>
    <td>Privilege Management Infrastructure</td>
    <td>PMI</td>
    <td>Инфраструктура управления привилегиями</td>
  </tr>
  <tr>
    <td>Registration Authority</td>
    <td>RA</td>
    <td>Регистрационный центр (РЦ)</td>
  </tr>
  <tr>
    <td>Relying Party</td>
    <td></td>
    <td>Доверяющая сторона</td>
  </tr>
  <tr>
    <td>Root CA</td>
    <td></td>
    <td>Корневой УЦ</td>
  </tr>
  <tr>
    <td>Subordinate CA</td>
    <td></td>
    <td>Подчиненный УЦ</td>
  </tr>
  <tr>
    <td>Subject</td>
    <td></td>
    <td>Субъект</td>
  </tr>
  <tr>
    <td>Top CA</td>
    <td></td>
    <td>УЦ верхнего уровня</td>
  </tr>
</table>