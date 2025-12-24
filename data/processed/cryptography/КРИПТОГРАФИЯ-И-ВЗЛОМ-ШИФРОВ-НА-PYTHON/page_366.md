---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.51
tokens: 7684
characters: 2064
timestamp: 2025-12-24T08:55:16.706687
finish_reason: stop
---

Применение частотного анализа для взлома каждого подключа

Если мы угадали длину ключа, то каждая из четырех строк, созданных нами в предыдущем разделе, должна быть зашифрована с помощью одного ключа. Это означает, что если строка, зашифрованная корректным ключом, подвергается частотному анализу, то дешифрованные буквы, вероятнее всего, будут иметь высокую оценку частотного соответствия. Рассмотрим, как это работает, используя в качестве примера первую строку: PAEBABANZIAHAKDXAAAKIU.

Прежде всего, дешифруем строку 26 раз (по одному разу для каждого из 26 возможных подключей), используя функцию vigenereCipher.decryptMessage() (см. главу 18). Затем протестируем каждую дешифрованную строку, используя функцию частотного анализа для английского языка freqAnalysis.englishFreqMatchScore() (см. главу 19). Введите в интерактивной оболочке следующий код.

>>> import freqAnalysis, vigenereCipher
>>> for subkey in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
...     decryptedMessage = vigenereCipher.decryptMessage(subkey,
...         'PAEBABANZIAHAKDXAAAKIU')
...     print(subkey, decryptedMessage,
...         freqAnalysis.englishFreqMatchScore(decryptedMessage) )
...
A PAEBABANZIAHAKDXAAAKIU 2
B OZDAZAZMYHZGZJCWZZZJHT 1
--опущено--

Результаты представлены в табл. 20.4.

Таблица 20.4. Оценки частотного соответствия для каждого варианта дешифрования

<table>
  <tr>
    <th>Подключ</th>
    <th>Дешифрование</th>
    <th>Оценка частотного соответствия</th>
  </tr>
  <tr>
    <td>'A'</td>
    <td>'PAEBABANZIAHAKDXAAAKIU'</td>
    <td>2</td>
  </tr>
  <tr>
    <td>'B'</td>
    <td>'OZDAZAZMYHZGZJCWZZZJHT'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'C'</td>
    <td>'NYCZYZYLXGYFYIBVYYYIGS'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'D'</td>
    <td>'MXBYXYXKWFEXHAUXXXHFR'</td>
    <td>0</td>
  </tr>
  <tr>
    <td>'E'</td>
    <td>'LWAXWXWJVEWDWGZTWWWGEQ'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'F'</td>
    <td>'KVZWVVWVIUDVCVFYSVVVFDP'</td>
    <td>0</td>
  </tr>
  <tr>
    <td>'G'</td>
    <td>'JUYVUVUHTCUBUEXRUUUECO'</td>
    <td>1</td>
  </tr>
</table>