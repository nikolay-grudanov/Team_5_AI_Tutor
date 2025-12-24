---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.51
tokens: 8143
characters: 2804
timestamp: 2025-12-24T08:54:27.385287
finish_reason: stop
---

Рис. 18.2. Соответствие ключей и букв в шифре Цезаря

Обратимся к примеру. Ниже приведено сообщение "COMMON SENSE IS NOT SO COMMON" вместе с ключом Виженера "PIZZA". Под каждой буквой исходного текста записан подключ, который ее шифрует.

COMMONSENSEISNOTSOCOMMON
PIZZAPIZZAPIZZAPIZZAPIZZ

Чтобы зашифровать первую букву исходного текста, 'C', используя подключ 'P', зашифруйте ее с помощью числового ключа шифра Цезаря, соответствующего данному подключу, в результате чего вы получите шифробукву 'R'. Повторяйте этот процесс для каждой буквы исходного текста, циклически перебирая подключи (табл. 18.1). Целые числа, указанные в скобках рядом с буквами исходного текста и подключей, суммируются попарно, и полученные целые числа соответствуют буквам шифротекста.

Таблица 18.1. Шифрование букв с помощью шифра Виженера

<table>
  <tr>
    <th>Буква открытого текста</th>
    <th>Подключ</th>
    <th>Буква шифротекста</th>
    <th>Буква открытого текста</th>
    <th>Подключ</th>
    <th>Буква шифротекста</th>
  </tr>
  <tr>
    <td>C (2)</td>
    <td>P (15)</td>
    <td>R (17)</td>
    <td>S (18)</td>
    <td>Z (25)</td>
    <td>R (17)</td>
  </tr>
  <tr>
    <td>O (14)</td>
    <td>I (8)</td>
    <td>W (22)</td>
    <td>N (13)</td>
    <td>Z (25)</td>
    <td>M (12)</td>
  </tr>
  <tr>
    <td>M (12)</td>
    <td>Z (25)</td>
    <td>L (11)</td>
    <td>O (14)</td>
    <td>A (0)</td>
    <td>O (14)</td>
  </tr>
  <tr>
    <td>M (12)</td>
    <td>Z (25)</td>
    <td>L (11)</td>
    <td>T (19)</td>
    <td>P (15)</td>
    <td>I (8)</td>
  </tr>
  <tr>
    <td>O (14)</td>
    <td>A (0)</td>
    <td>O (14)</td>
    <td>S (18)</td>
    <td>I (8)</td>
    <td>A (0)</td>
  </tr>
  <tr>
    <td>N (13)</td>
    <td>P (15)</td>
    <td>C (2)</td>
    <td>O (14)</td>
    <td>Z (25)</td>
    <td>N (13)</td>
  </tr>
  <tr>
    <td>S (18)</td>
    <td>I (8)</td>
    <td>A (0)</td>
    <td>C (2)</td>
    <td>Z (25)</td>
    <td>B (1)</td>
  </tr>
  <tr>
    <td>E (4)</td>
    <td>Z (25)</td>
    <td>D (3)</td>
    <td>O (14)</td>
    <td>A (0)</td>
    <td>O (14)</td>
  </tr>
  <tr>
    <td>N (13)</td>
    <td>Z (25)</td>
    <td>M (12)</td>
    <td>M (12)</td>
    <td>P (15)</td>
    <td>B (1)</td>
  </tr>
  <tr>
    <td>S (18)</td>
    <td>A (0)</td>
    <td>S (18)</td>
    <td>M (12)</td>
    <td>I (8)</td>
    <td>U (20)</td>
  </tr>
  <tr>
    <td>E (4)</td>
    <td>P (15)</td>
    <td>T (19)</td>
    <td>O (14)</td>
    <td>Z (25)</td>
    <td>N (13)</td>
  </tr>
  <tr>
    <td>I (8)</td>
    <td>I (8)</td>
    <td>Q (16)</td>
    <td>N (13)</td>
    <td>Z (25)</td>
    <td>M (12)</td>
  </tr>
</table>

Шифр Виженера с ключом "PIZZA" (состоящим из подключей 15, 8, 25, 25, 0) превращает открытый текст "COMMON SENSE IS NOT SO COMMON" в шифротекст "RWLLOC ADMST QR MOI ANBOBUNM".