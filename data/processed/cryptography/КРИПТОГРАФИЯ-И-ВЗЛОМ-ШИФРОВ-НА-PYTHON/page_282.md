---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 81.39
tokens: 8476
characters: 3685
timestamp: 2025-12-24T08:53:53.725975
finish_reason: stop
---

Вместо переменных LETTERS и key в функции используются переменные charsA и charsB, что позволяет заменять буквы в строке charsA буквами из строки charsB с тем же индексом. Возможность перестановки букв в переменных charsA и charsB упрощает переключение между режимами шифрования и дешифрования. В строке 47 в переменную charsA записывается содержимое строки LETTERS, а в строке 48 в переменную charsB записывается строка key.

Процесс шифрования проиллюстрирован на рис. 16.2. В верхнем ряду показаны символы строки charsA (содержит строку LETTERS), в среднем — символы строки charsB (содержит строку key), в нижнем — целочисленные индексы, соответствующие символам. Функция translateMessage() ищет индекс символа в строке charsA и заменяет его символом из строки charsB, имеющим тот же индекс.

<table>
  <tr>
    <th>charsA</th>
    <th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th><th>K</th><th>L</th><th>M</th><th>N</th><th>O</th><th>P</th><th>Q</th><th>R</th><th>S</th><th>T</th><th>U</th><th>V</th><th>W</th><th>X</th><th>Y</th><th>Z</th>
  </tr>
  <tr>
    <th>charsB</th>
    <td>V</td><td>J</td><td>Z</td><td>B</td><td>G</td><td>N</td><td>F</td><td>E</td><td>P</td><td>L</td><td>I</td><td>T</td><td>M</td><td>X</td><td>D</td><td>W</td><td>K</td><td>Q</td><td>U</td><td>C</td><td>R</td><td>Y</td><td>A</td><td>H</td><td>S</td><td>O</td>
  </tr>
  <tr>
    <th>Индекс</th>
    <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td>
  </tr>
</table>

Рис. 16.2. Использование индексов для шифрования сообщения

Когда нужно дешифровать сообщение, мы меняем переменные charsA и charsB местами с помощью инструкции charsA, charsB = charsB, charsA в строке 52. Процесс дешифрования проиллюстрирован на рис. 16.3.

<table>
  <tr>
    <th>charsA</th>
    <th>V</th><th>J</th><th>Z</th><th>B</th><th>G</th><th>N</th><th>F</th><th>E</th><th>P</th><th>L</th><th>I</th><th>T</th><th>M</th><th>X</th><th>D</th><th>W</th><th>K</th><th>Q</th><th>U</th><th>C</th><th>R</th><th>Y</th><th>A</th><th>H</th><th>S</th><th>O</th>
  </tr>
  <tr>
    <th>charsB</th>
    <td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
  </tr>
  <tr>
    <th>Индекс</th>
    <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td>
  </tr>
</table>

Рис. 16.3. Использование индексов для дешифрования шифротекста

Не забывайте о том, что функция всегда заменяет символы из строки charsA символами из строки charsB, имеющими тот же индекс. Поэтому после перестановки переменных в строке 52 функция выполняет не шифрование, а дешифрование.

В следующем фрагменте кода осуществляется поиск требуемого индекса.

54. # Цикл по всем символам сообщения
55. for symbol in message:
56.     if symbol.upper() in charsA:
57.         # Шифрование/дешифрование символа
58.         symIndex = charsA.find(symbol.upper())

На каждой итерации цикла for в строке 55 переменной symbol присваивается очередной символ строки сообщения. Если этот символ, преобразованный в верхний регистр, встречается в строке charsA (вспомните, что