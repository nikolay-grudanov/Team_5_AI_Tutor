---
source_image: page_258.png
page_number: 258
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.58
tokens: 6714
characters: 1938
timestamp: 2025-12-24T04:02:07.940690
finish_reason: stop
---

https://devdocs.magento.com/guides/v2.3/install-gde/system-requirements-tech.html
https://devdocs.magento.com/guides/v2.2/install-gde/system-requirements-tech.html

Таблица 15.1. Magento и выбор версии PHP

<table>
  <tr>
    <th>Версия Magento</th>
    <th>7.0.0 – 7.0.12</th>
    <th>7.0.13 – 7.0.x</th>
    <th>7.1.x</th>
    <th>7.2.x</th>
    <th>7.3.x</th>
  </tr>
  <tr>
    <td>2.2</td>
    <td>-</td>
    <td>+</td>
    <td>+</td>
    <td>патч 2.2.10</td>
    <td>-</td>
  </tr>
  <tr>
    <td>2.3</td>
    <td>-</td>
    <td>-</td>
    <td>7.1.3+</td>
    <td>+</td>
    <td>+</td>
  </tr>
</table>

Казалось бы, что тут такого — нужно установить Magento 2.3 и PHP 7.2 или 7.3 (смотря какая версия есть в дистрибутиве), ведь мы устанавливаем все с нуля. Но это неправильное решение.

Может оказаться так, что нужное вам расширение или тема оформления не поддерживает версию 2.3. Когда я установил Magento 2.3 и подключил MarketPlace (https://marketplace.magento.com), то обнаружил, что в списке расширений не было необходимого мне расширения для моей CRM.

Именно поэтому сначала нужно выбрать шаблон для вашего сайта и составить список расширений, которые вам будут нужны. Возможно, это будут расширения, добавляющие необходимые вам способы оплаты/доставки (интеграция с платежной системой и службой доставки товаров), производящие интеграцию с CRM и т.д.

Составьте табличку совместимости (табл. 15.2). Например, в моем случае она выглядела так

Таблица 15.2. Таблица совместимости

<table>
  <tr>
    <th>Расширение/шаблон</th>
    <th>Magento 2.1</th>
    <th>Magento 2.2</th>
    <th>Magento 2.3</th>
  </tr>
  <tr>
    <td>SM Destino</td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td>retailCRM</td>
    <td>x</td>
    <td>x</td>
    <td>-</td>
  </tr>
</table>

Поставьте крестик в поле, если шаблон/расширение поддерживает версию Magento. Как правило, вся необходимая информация есть в документации