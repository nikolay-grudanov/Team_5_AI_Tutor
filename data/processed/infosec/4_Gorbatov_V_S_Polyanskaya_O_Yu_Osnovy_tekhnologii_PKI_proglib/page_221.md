---
source_image: page_221.png
page_number: 221
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.97
tokens: 5414
characters: 2160
timestamp: 2025-12-23T23:32:07.819287
finish_reason: stop
---

ПРИЛОЖЕНИЕ 2. СРАВНИТЕЛЬНАЯ ХАРАКТЕРИСТИКА ПРОГРАММНЫХ ПРОДУКТОВ

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
    <th colspan="6">Поддержка сертификатов</th>
  </tr>
  <tr>
    <td>Формат сертификата</td>
    <td>X.509v3</td>
    <td>X.509v3</td>
    <td>X.509v3</td>
    <td>X.509v3</td>
    <td>X.509v3</td>
  </tr>
  <tr>
    <td>Дополнения сертификата стандартные/частные</td>
    <td>Почти все<br>Дополнения заказчика</td>
    <td>Да<br>Да/да</td>
    <td>X.509v3, PKIX, FPKI Enterprise, Web, SET, VPN, PKIX, FPKI</td>
    <td>Да<br>Да/да</td>
    <td>Да, в том числе дополнения, определяемые пользователем</td>
  </tr>
  <tr>
    <th colspan="6">Методы аннулирования</th>
  </tr>
  <tr>
    <td>СAC</td>
    <td>Да</td>
    <td>Через файлы LDIFv3</td>
    <td>Да</td>
    <td>Да</td>
    <td>Да</td>
  </tr>
  <tr>
    <td>Протокол OCSP</td>
    <td>Да</td>
    <td>Да (VeriSign)</td>
    <td>Да</td>
    <td>Да</td>
    <td>Да</td>
  </tr>
  <tr>
    <td>Пункты распространения САС</td>
    <td>Да</td>
    <td>Да</td>
    <td>Да</td>
    <td>Нет</td>
    <td>Нет</td>
  </tr>
  <tr>
    <th colspan="6">Расширяемость</th>
  </tr>
  <tr>
    <td>Модульность</td>
    <td>Отдельные модули, которые могут быть размещены вместе и на отдельных компьютерах</td>
    <td>Модули УЦ и РЦ размещаются на разных компьютерах</td>
    <td>Модуль УЦ работает на отдельной рабочей станции и одновременно взаимодействует со многими РЦ</td>
    <td>Модули CA/Audit Server, RA Server и Directory размещаются на разных компьютерах</td>
    <td>Модули УЦ и РЦ могут размещаться вместе, для других модулей требуются отдельные компьютеры</td>
  </tr>
  <tr>
    <td>Максимальное количество сертификатов</td>
    <td>Нет ограничений на количество сертификатов</td>
    <td>Нет ограничений на количество сертификатов</td>
    <td>Сертификаты для 1 млн пользователей</td>
    <td>Свыше 30 млн</td>
    <td>Нет ограничений на количество сертификатов</td>
  </tr>
</table>