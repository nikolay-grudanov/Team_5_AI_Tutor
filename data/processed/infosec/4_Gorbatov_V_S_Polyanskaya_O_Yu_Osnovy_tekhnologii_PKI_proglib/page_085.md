---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.80
tokens: 5149
characters: 1892
timestamp: 2025-12-23T23:29:27.631464
finish_reason: stop
---

<table>
  <tr>
    <th>Версия</th>
    <th>Элемент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td colspan="3">[Следующие элементы повторяются для каждого аннулированного сертификата]</td>
  </tr>
  <tr>
    <td rowspan="2">v1</td>
    <td><b>certificateSerialNumber</b></td>
    <td>Серийный номер сертификата</td>
  </tr>
  <tr>
    <td><b>revocationDate</b></td>
    <td>Дата получения запроса об аннулировании</td>
  </tr>
  <tr>
    <td rowspan="8">v2</td>
    <td><b>reasonCode</b></td>
    <td>Код причины аннулирования (задается перечисленными ниже значениями)<br>
      1. Причина не определена<br>
      2. Повреждение ключа конечного пользователя<br>
      3. Повреждение ключа УЦ<br>
      4. Изменение информации в сертификате (не повреждение)<br>
      5. Приостановление действия ключа<br>
      6. Завершение использования<br>
      7. Приостановление использования<br>
      8. Отмена временного приостановления
    </td>
  </tr>
  <tr>
    <td>unspecified<br>keyCompromise<br>cACompromise<br>affiliationChanged</td>
    <td></td>
  </tr>
  <tr>
    <td>superseded<br>cessationOfOperation<br>certificateHold<br>removeFromCRL</td>
    <td></td>
  </tr>
  <tr>
    <td><b>holdInstructionCode</b></td>
    <td>Код временного приостановления сертификата (OID)</td>
  </tr>
  <tr>
    <td><b>invalidityDate</b></td>
    <td>Дата признания сертификата недействительным</td>
  </tr>
  <tr>
    <td><b>certificateIssuer</b></td>
    <td>Имя издателя сертификата, ассоциированного с косвенным САС</td>
  </tr>
</table>

Дополнение CRL Number выполняет функцию счетчика и информирует пользователей о выпуске очередного САС. Дополнение Authority Key Identifier помогает пользователям выбрать правильный открытый ключ для верификации подписи на данном САС в том случае, когда удостоверяющий центр владеет многими парами ключей подписи САС. Дополнение Issuer Alternative Name служит для