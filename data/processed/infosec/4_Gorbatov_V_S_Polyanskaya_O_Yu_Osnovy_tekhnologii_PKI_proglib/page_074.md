---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.63
tokens: 5192
characters: 1923
timestamp: 2025-12-23T23:29:13.615531
finish_reason: stop
---

<table>
  <tr>
    <th>Элемент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>keyUsage<br>keyAgreement</td>
    <td>Применение ключа (строки битов)<br>5. Формирование других ключей (например, по алгоритму Диффи-Хелмана)<br>6. Формирование ЭЦП сертификатов.<br>Может использоваться УЦ</td>
  </tr>
  <tr>
    <td>KeyCertSign</td>
    <td>7. Формирование ЭЦП САС. Может использоваться УЦ</td>
  </tr>
  <tr>
    <td>CRLSign</td>
    <td></td>
  </tr>
  <tr>
    <td>EncipherOnly<br>DecipherOnly</td>
    <td>8. Только для шифрования<br>9. Только для расшифрования</td>
  </tr>
  <tr>
    <td>privateKeyUsagePeriod</td>
    <td>Период действия секретного ключа подписи УЦ</td>
  </tr>
  <tr>
    <td>PolicyMappings<br>IssuerDomainPolicy<br>SubjectDomainPolicy</td>
    <td>Используется только для сертификата УЦ. Оговаривает, что политики применения сертификатов издателя и субъекта одинаковы</td>
  </tr>
  <tr>
    <td>SupportedAlgorithms<br>AlgorithmIdentifier<br>IntendedUsage<br>intendedCertificatePolicies</td>
    <td>Определяют атрибуты каталога. Используются, чтобы сделать атрибуты известными заранее в случаях, когда партнер по связи использует данные каталога</td>
  </tr>
  <tr>
    <td>SubjectAltName</td>
    <td>Альтернативное имя субъекта. Свободный выбор имени.<br>Произвольное имя<br>Адрес электронной почты<br>Имя домена<br>Адрес отправителя/получателя<br>Имя каталога<br>EDI-имя<br>Унифицированный указатель ресурсов<br>WWW URL</td>
  </tr>
  <tr>
    <td>OtherName<br>rfc822Name<br>dNSName<br>x400Address<br>directoryName<br>ediPartyName<br>uniformResourceIdentifier<br>iPAddress<br>registeredID</td>
    <td>IP-адрес<br>Зарегистриров. ID объекта</td>
  </tr>
  <tr>
    <td>issuerAltName</td>
    <td>Альтернативное имя издателя</td>
  </tr>
  <tr>
    <td>subjectDirectoryAttributes</td>
    <td>Необязательные атрибуты субъекта, например, почтовый адрес, номер телефона и т.п.</td>
  </tr>
</table>