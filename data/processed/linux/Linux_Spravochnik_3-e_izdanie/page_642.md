---
source_image: page_642.png
page_number: 642
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.19
tokens: 12301
characters: 2535
timestamp: 2025-12-24T03:44:32.407194
finish_reason: stop
---

Примеры поиска

<table>
  <tr>
    <th>Шаблон</th>
    <th>Результат поиска</th>
  </tr>
  <tr>
    <td>b.g</td>
    <td>Вторая буква является любым символом, кроме символа новой строки</td>
  </tr>
  <tr>
    <td>^...$</td>
    <td>Любая строка, содержащая ровно три буквы</td>
  </tr>
  <tr>
    <td>^\.</td>
    <td>Строка, которая начинается с точки</td>
  </tr>
  <tr>
    <td>^\.[a-z][a-z]</td>
    <td>То же, за точкой следуют две строчные буквы (так выглядят, например, запросы troff)</td>
  </tr>
  <tr>
    <td>^\.[a-z]\{2\}</td>
    <td>То же, что и в предыдущем случае, но только для grep или sed</td>
  </tr>
  <tr>
    <td>^[^.]</td>
    <td>Любая строка, которая не начинается с точки</td>
  </tr>
  <tr>
    <td>bugs*</td>
    <td>Слова «bug», «bugs», «bugss» и т. д.</td>
  </tr>
  <tr>
    <td>"word"</td>
    <td>Слово word в кавычках</td>
  </tr>
  <tr>
    <td>"*word"*</td>
    <td>Слово word в кавычках или без</td>
  </tr>
  <tr>
    <td>[A-Z][A-Z]*</td>
    <td>Одна или больше прописных букв</td>
  </tr>
  <tr>
    <td>[A-Z]+</td>
    <td>То же, но только для egrep или awk</td>
  </tr>
  <tr>
    <td>[A-Z].*</td>
    <td>Прописная буква, за которой следует произвольное количество (включая нулевое) любых символов</td>
  </tr>
  <tr>
    <td>[A-Z]*</td>
    <td>Произвольное количество (включая нулевое) прописных букв</td>
  </tr>
  <tr>
    <td>[a-zA-Z]</td>
    <td>Любая буква</td>
  </tr>
  <tr>
    <td>[0-9A-Za-z]+</td>
    <td>Любая буквенно-цифровая последовательность</td>
  </tr>
</table>

<table>
  <tr>
    <th>Шаблон egrep или awk</th>
    <th>Результат поиска</th>
  </tr>
  <tr>
    <td>[567]</td>
    <td>Одно из чисел 5, 6 или 7</td>
  </tr>
  <tr>
    <td>five|six|seven</td>
    <td>Одно из слов five, six или seven</td>
  </tr>
  <tr>
    <td>80[23]?86</td>
    <td>8086, 80286 или 80386</td>
  </tr>
  <tr>
    <td>Compan(y|ies)</td>
    <td>Слово company или companies</td>
  </tr>
</table>

<table>
  <tr>
    <th>Шаблон vi</th>
    <th>Результат поиска</th>
  </tr>
  <tr>
    <td>\<the</td>
    <td>Слова вроде theater или the</td>
  </tr>
  <tr>
    <td>the\></td>
    <td>Слова вроде breathe или the</td>
  </tr>
  <tr>
    <td>\<the\></td>
    <td>Слово the</td>
  </tr>
</table>

<table>
  <tr>
    <th>Шаблон sed или grep</th>
    <th>Результат поиска</th>
  </tr>
  <tr>
    <td>0\{5,\}</td>
    <td>Пять или более нулей подряд</td>
  </tr>
  <tr>
    <td>[0-9]\{3\}-[0-9]\{2\}-[0-9]\{4\}</td>
    <td>Номер социального страхования (<i>nnn-nn-nnnn</i>)</td>
  </tr>
</table>