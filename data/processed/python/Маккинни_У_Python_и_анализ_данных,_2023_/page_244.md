---
source_image: page_244.png
page_number: 244
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.40
tokens: 7960
characters: 2550
timestamp: 2025-12-24T02:47:03.527430
finish_reason: stop
---

<table>
  <tr>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>get</td>
    <td>Доступ по индексу ко всем элементам (выбрать i-й элемент)</td>
  </tr>
  <tr>
    <td>isalnum</td>
    <td>Эквивалентно встроенному методу str.isalnum</td>
  </tr>
  <tr>
    <td>isalpha</td>
    <td>Эквивалентно встроенному методу str.isalpha</td>
  </tr>
  <tr>
    <td>isdecimal</td>
    <td>Эквивалентно встроенному методу str.isdecimal</td>
  </tr>
  <tr>
    <td>isdigit</td>
    <td>Эквивалентно встроенному методу str.isdigit</td>
  </tr>
  <tr>
    <td>islower</td>
    <td>Эквивалентно встроенному методу str.islower</td>
  </tr>
  <tr>
    <td>isnumeric</td>
    <td>Эквивалентно встроенному методу str.isnumeric</td>
  </tr>
  <tr>
    <td>isupper</td>
    <td>Эквивалентно встроенному методу str.isupper</td>
  </tr>
  <tr>
    <td>join</td>
    <td>Объединяет строки в каждом элементе Series, вставляя между ними указанный разделитель</td>
  </tr>
  <tr>
    <td>len</td>
    <td>Вычисляет длину каждой строки</td>
  </tr>
  <tr>
    <td>lower, upper</td>
    <td>Преобразование регистра; эквивалентно x.lower() или x.upper() для каждого элемента</td>
  </tr>
  <tr>
    <td>match</td>
    <td>Вызывает re.match с указанным регулярным выражением для каждого элемента, возвращает список выделенных групп</td>
  </tr>
  <tr>
    <td>pad</td>
    <td>Дополняет строки пробелами слева, справа или с обеих сторон</td>
  </tr>
  <tr>
    <td>center</td>
    <td>Эквивалентно pad(side='both')</td>
  </tr>
  <tr>
    <td>repeat</td>
    <td>Дублирует значения; например, s.str.repeat(3) эквивалентно x * 3 для каждой строки</td>
  </tr>
  <tr>
    <td>replace</td>
    <td>Заменяет вхождения образца указанной строкой</td>
  </tr>
  <tr>
    <td>slice</td>
    <td>Вырезает каждую строку в объекте Series</td>
  </tr>
  <tr>
    <td>split</td>
    <td>Разбивает строки по разделителю или по регулярному выражению</td>
  </tr>
  <tr>
    <td>strip</td>
    <td>Убирает пробельные символы, в т. ч. знак новой строки, с обеих сторон строки</td>
  </tr>
  <tr>
    <td>rstrip</td>
    <td>Убирает пробельные символы справа</td>
  </tr>
  <tr>
    <td>lstrip</td>
    <td>Убирает пробельные символы слева</td>
  </tr>
</table>

7.5. Категориальные данные

В этом разделе мы познакомимся с типом pandas Categorical. Я покажу, как с его помощью повысить производительность и снизить потребление памяти при выполнении некоторых операций. Кроме того, я представлю инструменты, помогающие использовать категориальные данные в статистике и машинном обучении.