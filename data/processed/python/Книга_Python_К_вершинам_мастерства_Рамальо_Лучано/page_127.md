---
source_image: page_127.png
page_number: 127
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 102.98
tokens: 12846
characters: 3779
timestamp: 2025-12-24T01:41:30.129496
finish_reason: stop
---

Базовые кодировщики и декодировщики

cp1252
Надмножество latin1, разработанное Майкрософт. Добавлены некоторые полезные символы, например фигурные кавычки и знак евро €. В некоторых приложениях для Windows эта кодировка называется «ANSI», хотя никакой стандарт ANSI по этому поводу не принимался.

cp437
Оригинальный набор символов для IBM PC, содержащий символы псевдографики. Несовместим с кодировкой latin1, которая появилась позже.

gb2312
Унаследованный стандарт кодирования упрощенных китайских иероглифов, используемый в континентальном Китае; одна из нескольких широко распространенных многобайтовых кодировок для азиатских языков.

utf-8
Самая употребительная 8-разрядная кодировка в веб3, обратно совместима с ASCII (текст, содержащий только символы ASCII, является допустимым и в кодировке UTF-8).

utf-16le
Одна из форм 16-разрядной схемы кодирования UTF-16; все кодировки семейства UTF-16 поддерживают кодовые позиции с номерами, большими U+FFFF, с помощью управляющих последовательностей, называемых «суррогатными парами».

<table>
  <tr>
    <th>char.</th>
    <th>code point</th>
    <th>ascii</th>
    <th>latin1</th>
    <th>cp1252</th>
    <th>cp437</th>
    <th>gb2312</th>
    <th>utf-8</th>
    <th>utf-16le</th>
  </tr>
  <tr>
    <td>A</td>
    <td>U+0041</td>
    <td>41</td>
    <td>41</td>
    <td>41</td>
    <td>41</td>
    <td>41</td>
    <td>41</td>
    <td>41 00</td>
  </tr>
  <tr>
    <td>¿</td>
    <td>U+00BF</td>
    <td>*</td>
    <td>BF</td>
    <td>BF</td>
    <td>A8</td>
    <td>*</td>
    <td>C2 BF</td>
    <td>BF 00</td>
  </tr>
  <tr>
    <td>Ã</td>
    <td>U+00C3</td>
    <td>*</td>
    <td>C3</td>
    <td>C3</td>
    <td>*</td>
    <td>*</td>
    <td>C3 83</td>
    <td>C3 00</td>
  </tr>
  <tr>
    <td>á</td>
    <td>U+00E1</td>
    <td>*</td>
    <td>E1</td>
    <td>E1</td>
    <td>A0</td>
    <td>A8 A2</td>
    <td>C3 A1</td>
    <td>E1 00</td>
  </tr>
  <tr>
    <td>Ω</td>
    <td>U+03A9</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>EA</td>
    <td>A6 B8</td>
    <td>CE A9</td>
    <td>A9 03</td>
  </tr>
  <tr>
    <td>çi</td>
    <td>U+06BF</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>DA BF</td>
    <td>BF 06</td>
  </tr>
  <tr>
    <td>"</td>
    <td>U+201C</td>
    <td>*</td>
    <td>*</td>
    <td>93</td>
    <td>*</td>
    <td>A1 B0</td>
    <td>E2 80 9C</td>
    <td>1C 20</td>
  </tr>
  <tr>
    <td>€</td>
    <td>U+20AC</td>
    <td>*</td>
    <td>*</td>
    <td>80</td>
    <td>*</td>
    <td>*</td>
    <td>E2 82 AC</td>
    <td>AC 20</td>
  </tr>
  <tr>
    <td>Γ</td>
    <td>U+250C</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>DA</td>
    <td>A9 B0</td>
    <td>E2 94 8C</td>
    <td>0C 25</td>
  </tr>
  <tr>
    <td>气</td>
    <td>U+6C14</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>C6 F8</td>
    <td>E6 B0 94</td>
    <td>14 6C</td>
  </tr>
  <tr>
    <td>氣</td>
    <td>U+6C23</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>E6 B0 A3</td>
    <td>23 6C</td>
  </tr>
  <tr>
    <td>§</td>
    <td>U+1D11E</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>*</td>
    <td>F0 9D 84 9E</td>
    <td>34 D8 1E DD</td>
  </tr>
</table>

Рис. 4.1. Двенадцать символов, их кодовые позиции и байтовые представления (в 16-ричном виде) в семи разных кодировках (звездочка означает, что в данной кодировке этот символ непредставим)

3 По состоянию на сентябрь 2014 года в исследовании W3Techs «Usage of Character Encodings for Websites» (http://bit.ly/w3techs-en) утверждается, что на 81.4 % сайтов используется кодировка UTF-8, тогда как сайт Built With в отчете «Encoding Usage Statistics» (http://trends.builtwith.com/encoding) дает оценку 79.4 %.