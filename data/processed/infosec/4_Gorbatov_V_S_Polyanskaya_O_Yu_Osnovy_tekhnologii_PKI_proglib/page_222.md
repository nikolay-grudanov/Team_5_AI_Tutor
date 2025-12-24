---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.21
tokens: 5411
characters: 2156
timestamp: 2025-12-23T23:32:10.518563
finish_reason: stop
---

Вот таблица, представленная в тексте:

<table>
  <tr>
    <th>Программный продукт</th>
    <th>Baltimore UniCERT 5.0</th>
    <th>BT TRUST ONSITE 4.5</th>
    <th>ENTRUST / PKI 5.0</th>
    <th>IBM Trust Authority 3.1.</th>
    <th>RSA Keon Certification Authority 6.5.</th>
  </tr>
  <tr>
    <th colspan="6">Безопасность</th>
  </tr>
  <tr>
    <th>Коммуникации с клиентом</th>
    <td>PKCS#10/7 PKCS#12</td>
    <td>Через считывание PIN-кода или по эл. Почте</td>
    <td>PKIX-CMP PKIX#7/10</td>
    <td>SSL</td>
    <td>SSL</td>
  </tr>
  <tr>
    <th>Коммуникации между УЦ/РЦ</th>
    <td>Подписанные сообщения PKIX CMP</td>
    <td>Защищенные транзакции</td>
    <td>Защищенный SPKM/GS S-API сеанс связи</td>
    <td>Подписанные сообщения PKIX CMP</td>
    <td>PKIX CMP</td>
  </tr>
  <tr>
    <th>Защита УЦ/РЦ</th>
    <td>Программные или аппаратные модули безопасности с контролем доступа</td>
    <td>Смарт-карты</td>
    <td>Цифровые удостоверения личности администраторов, токены</td>
    <td>Пароли или смарт-карты, списки управления доступом, аппаратные устройства</td>
    <td>Смарт-карты /токены</td>
  </tr>
  <tr>
    <th>Аппаратная защита корневых ключей УЦ</th>
    <td>Да</td>
    <td>Да</td>
    <td>Устройства Chrysalis, Zaxus (Racal) и Atalla</td>
    <td>Криптографический сопроцессор IBM 4758, смарт-карты</td>
    <td>Нет</td>
  </tr>
  <tr>
    <th colspan="6">Топология PKI</th>
  </tr>
  <tr>
    <th>Способы сертификации</th>
    <td>Сетевая, иерархическая</td>
    <td>Только иерархические PKI</td>
    <td>Сетевая, иерархическая и гибридная PKIX CMP PKCS#10/7</td>
    <td>Двусторонняя PKIX CMP</td>
    <td>Сетевая и иерархическая</td>
  </tr>
  <tr>
    <th>Глубина иерархии</th>
    <td>Любая</td>
    <td>Любая</td>
    <td>Любая</td>
    <td>Любая</td>
    <td>Любая</td>
  </tr>
  <tr>
    <th>Множественные УЦ/РЦ</th>
    <td>Да, максимальное число РЦ для одного УЦ – 255</td>
    <td>Да, без ограничений</td>
    <td>Да, без ограничений.</td>
    <td>Нет</td>
    <td>Да, без ограничений</td>
  </tr>
</table>

Эта таблица сравнивает различные программные продукты по различным аспектам безопасности и топологии PKI.