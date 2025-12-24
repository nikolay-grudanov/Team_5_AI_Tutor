---
source_image: page_368.png
page_number: 368
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.11
tokens: 7576
characters: 1632
timestamp: 2025-12-24T08:55:16.263352
finish_reason: stop
---

ми, нам нужно перебрать 50 возможных ключей. Это намного лучше, чем полный перебор 26 · 26 · 26 · 26 (или 456 976) возможных ключей, к которому пришлось бы прибегнуть, если бы мы не сузили список кандидатов. Разница становится еще более существенной в случае ключей Виженера большей длины.

Таблица 20.5. Наиболее вероятные подключи для тестируемых строк

<table>
  <tr>
    <th>Строка шифротекста</th>
    <th>Наиболее вероятные подключи</th>
  </tr>
  <tr>
    <td>PAEBABANZIAHAKDXAAAKIU</td>
    <td>A, I, N, W, X</td>
  </tr>
  <tr>
    <td>PXKNZNLLIMMGTUSWIZVZBW</td>
    <td>I, Z</td>
  </tr>
  <tr>
    <td>QQGKUGJTJVVVCUGUTUVCQP</td>
    <td>C</td>
  </tr>
  <tr>
    <td>CVYMYBOSYRORTDOLVRVPO</td>
    <td>K, N, R, V, Y</td>
  </tr>
</table>

Перебор возможных подключей методом грубой силы

Метод грубой силы предполагает полный перебор всех возможных комбинаций подключей. Все 50 возможных комбинаций приведены ниже.

AICK   IICK   NICK   WICK   XICK
AICN   IICN   NICN   WICN   XICN
AICR   IICR   NICR   WICR   XICR
AICV   IICV   NICV   WICV   XICV
AICY   IICY   NICY   WICY   XICY
AZCK   IZCK   NZCK   WZCK   XZCK
AZCN   IZCN   NZCN   WZCN   XZCN
AZCR   IZCR   NZCR   WZCR   XZCR
AZCV   IZCV   NZCV   WZCV   XZCV
AZCY   IZCY   NZCY   WZCY   XZCY

Завершающим этапом алгоритма, реализуемого нашей программой взлома шифра Виженера, будет тестирование всех 50 возможных вариантов дешифрования на полном шифротексте, чтобы увидеть, какие из них приводят к получению осмысленного текста на английском языке. В ходе этого процесса мы должны обнаружить, что ключом для дешифрования шифротекста "PPQCA XQVEKG..." является WICK.