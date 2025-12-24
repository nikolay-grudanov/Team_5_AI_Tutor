---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.41
tokens: 5078
characters: 1700
timestamp: 2025-12-23T23:29:10.498485
finish_reason: stop
---

<table>
  <tr>
    <th>Элемент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td><b>BasicConstraints</b></td>
    <td>Отличает ключ УЦ от ключей конечных пользователей (используется только для сертификата УЦ)<br>Для ключа УЦ сA истинно.<br>Ограничение длины цепочки</td>
  </tr>
  <tr>
    <td>cA<br>pathLenConstraint</td>
    <td></td>
  </tr>
  <tr>
    <td><b>NameConstraints</b></td>
    <td>Используется только при сертификации УЦ<br>Определяет сертификацию домена по имени по отношению к подчиненному УЦ в пределах пути, устанавливаемого параметром BasicConstraints<br>Подчиненный УЦ и домен его поддерева<br>Имя подчиненного УЦ<br>Верхний предел домена<br>Нижний предел домена<br>Подчиненный УЦ, исключенный из домена</td>
  </tr>
  <tr>
    <td>PermittedSubtrees<br>Base<br>minimum<br>maximum<br>excludedSubtree</td>
    <td></td>
  </tr>
  <tr>
    <td><b>PolicyConstraints</b><br><b>PolicySet</b><br><b>InhibitPolicyMapping</b></td>
    <td>Ограничения политики (используется только для requireExplicitPolicy УЦ)</td>
  </tr>
  <tr>
    <td><b>cRLDistributionPoints</b><br>distributionPoint<br>reasons</td>
    <td>Пункты распространения САС<br>Имя пункта распространения<br>Вид списка, распространяемого данным пунктом<br>1. Скомпрометированный ключ конечного пользователя<br>2. Скомпрометированный ключ УЦ<br>3. Измененная информация в сертификате (не повреждение)<br>4. Приостановленный ключ<br>5. Завершение использования<br>6. Приостановление использования<br>Имя издателя САС</td>
  </tr>
  <tr>
    <td>keyCompromise<br>cACompromise<br>affiliationChanged<br>superseded<br>cessationOfOperation<br>certificateHold<br>cRLIssuer</td>
    <td></td>
  </tr>
</table>

Окончание таблицы 4.1