---
source_image: page_152.png
page_number: 152
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 80.51
tokens: 12419
characters: 3138
timestamp: 2025-12-24T01:42:24.638714
finish_reason: stop
---

3 Вывести re_dig, если символ соответствует регулярному выражению r'\d'.
4 Вывести isdig, если char.isdigit() равно True.
5 Вывести isnum, если char.isnumeric() равно True.
6 Числовое значение в поле шириной 5 с двумя десятичными знаками после запятой.
7 Имя символа Unicode.

В результате выполнения этой программы получается распечатка, показанная на рис. 4.3.

<table>
  <tr>
    <th>U+0031</th>
    <th>1</th>
    <th>re_dig</th>
    <th>isdig</th>
    <th>isnum</th>
    <th>1.00</th>
    <th>DIGIT ONE</th>
  </tr>
  <tr>
    <th>U+00bc</th>
    <th>\u2152</th>
    <th>-</th>
    <th>-</th>
    <th>isnum</th>
    <th>0.25</th>
    <th>VULGAR FRACTION ONE QUARTER</th>
  </tr>
  <tr>
    <th>U+00b2</th>
    <th>2</th>
    <th>-</th>
    <th>isdig</th>
    <th>isnum</th>
    <th>2.00</th>
    <th>SUPERSCRIPT TWO</th>
  </tr>
  <tr>
    <th>U+0969</th>
    <th>३</th>
    <th>re_dig</th>
    <th>isdig</th>
    <th>isnum</th>
    <th>3.00</th>
    <th>DEVANAGARI DIGIT THREE</th>
  </tr>
  <tr>
    <th>U+136b</th>
    <th>ג</th>
    <th>-</th>
    <th>isdig</th>
    <th>isnum</th>
    <th>3.00</th>
    <th>ETHIOPIC DIGIT THREE</th>
  </tr>
  <tr>
    <th>U+216b</th>
    <th>XII</th>
    <th>-</th>
    <th>-</th>
    <th>isnum</th>
    <th>12.00</th>
    <th>ROMAN NUMERAL TWELVE</th>
  </tr>
  <tr>
    <th>U+2466</th>
    <th>⑦</th>
    <th>-</th>
    <th>isdig</th>
    <th>isnum</th>
    <th>7.00</th>
    <th>CIRCLED DIGIT SEVEN</th>
  </tr>
  <tr>
    <th>U+2480</th>
    <th>(3)</th>
    <th>-</th>
    <th>-</th>
    <th>isnum</th>
    <th>13.00</th>
    <th>PARENTHESIZED NUMBER THIRTEEN</th>
  </tr>
  <tr>
    <th>U+3285</th>
    <th>๖</th>
    <th>-</th>
    <th>-</th>
    <th>isnum</th>
    <th>6.00</th>
    <th>CIRCLED IDEOGRAPH SIX</th>
  </tr>
</table>

Рис. 4.3. Девять числовых символов и их метаданные; re_dig означает, что символ соответствует регулярному выражению r'\d'

Шестая колонка на рис. 4.3 содержит результат вызова unicodedata.numeric(char) для символа. Эта функция говорит о том, что Unicode знает числовые значения символов, представляющих числа. Так что если вы собираетесь написать программу для электронной таблицы, поддерживающей тамильские или римские цифры, вперед и с песней!

Из рис. 4.3 видно, что регулярному выражению r'\d' соответствует цифра «1» и цифра 3 письменности Деванагари, но не некоторые другие символы, которые функция isdigit считает цифрами. Модуль re знает о Unicode меньше, чем должен бы. Новый модуль regex, включенный в библиотеку PyPI, имеет целью полностью заменить re и поддерживает Unicode лучше12. Мы вернемся к модулю re в следующем разделе.

В этой главе мы пользовались несколькими функциями из модуля unicodedata, но на самом деле их гораздо больше. См. описание модуля unicodedata в документации по стандартной библиотеке (https://docs.python.org/3/library/unicodedata.html).

Мы завершим сравнение типов str и bytes беглым знакомством с новой тенденцией: двухрежимным API, предоставляющим функции, которые принимают в качестве аргументов str и bytes и работают по-разному в зависимости от типа.

12 Хотя цифры он распознавал ничуть не лучше модуля re.