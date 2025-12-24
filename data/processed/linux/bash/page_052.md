---
source_image: page_052.png
page_number: 52
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.10
tokens: 7656
characters: 2091
timestamp: 2025-12-23T23:03:38.779363
finish_reason: stop
---

сокращения. Например, чтобы найти любые числа в файле frost.txt, вы напишете следующее:

$ grep -P '\d' frost.txt

1    Two roads diverged in a yellow wood,
2    And sorry I could not travel both
3    And be one traveler, long I stood
4    And looked down one as far as I could
5    To where it bent in the undergrowth;
6
7 Excerpt from The Road Not Taken by Robert Frost

Другие символьные классы (с более подробным синтаксисом) действительно только внутри скобок, как показано в табл. 3.3. Они соответствуют одному символу, поэтому, если вам нужно сопоставить несколько строк подряд, чтобы получить необходимое повторение, используйте символы * или +.

Таблица 3.3. Символьные классы регулярных выражений в скобках

<table>
  <tr>
    <th>Символьный класс</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>[:alnum:]</td>
    <td>Любой буквенно-цифровой символ</td>
  </tr>
  <tr>
    <td>[:alpha:]</td>
    <td>Любой алфавитный символ</td>
  </tr>
  <tr>
    <td>[:cntrl:]</td>
    <td>Любой управляющий символ</td>
  </tr>
  <tr>
    <td>[:digit:]</td>
    <td>Любая цифра</td>
  </tr>
  <tr>
    <td>[:graph:]</td>
    <td>Любой графический символ</td>
  </tr>
  <tr>
    <td>[:lower:]</td>
    <td>Любой символ нижнего регистра</td>
  </tr>
  <tr>
    <td>[:print:]</td>
    <td>Любой печатаемый символ</td>
  </tr>
  <tr>
    <td>[:punct:]</td>
    <td>Любой знак препинания</td>
  </tr>
  <tr>
    <td>[:space:]</td>
    <td>Любой пробельный символ</td>
  </tr>
  <tr>
    <td>[:upper:]</td>
    <td>Любой символ верхнего регистра</td>
  </tr>
  <tr>
    <td>[:xdigit:]</td>
    <td>Любая шестнадцатеричная цифра</td>
  </tr>
</table>

Чтобы можно было использовать один из этих классов, он должен быть внутри скобок. Таким образом, вы получите два набора скобок. Например, grep '[[[:cntrl:]]]' large.data будет искать строки, содержащие управляющие символы (ASCII 0–25). Вот еще один пример:

grep 'X[[:upper:]][:digit:]' idlist.txt

Согласно этой команде будет выполнен поиск содержимого в файле idlist.txt и в результате будет выведена любая строка, содержащая символ X, за которым