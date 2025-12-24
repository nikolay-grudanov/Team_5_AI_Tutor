---
source_image: page_223.png
page_number: 223
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.18
tokens: 7610
characters: 2031
timestamp: 2025-12-24T00:57:10.790742
finish_reason: stop
---

Таблица 3.4. Соответствие между методами библиотеки Pandas и функциями модуля re языка Python

<table>
  <tr>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>match()</td>
    <td>Вызывает функцию re.match() для каждого элемента, возвращая булево значение</td>
  </tr>
  <tr>
    <td>extract()</td>
    <td>Вызывает функцию re.match() для каждого элемента, возвращая подходящие группы в виде строк</td>
  </tr>
  <tr>
    <td>findall()</td>
    <td>Вызывает функцию re.findall() для каждого элемента</td>
  </tr>
  <tr>
    <td>replace()</td>
    <td>Заменяет вхождения шаблона какой-либо другой строкой</td>
  </tr>
  <tr>
    <td>contains()</td>
    <td>Вызывает функцию re.search() для каждого элемента, возвращая булево значение</td>
  </tr>
  <tr>
    <td>count()</td>
    <td>Подсчитывает вхождения шаблона</td>
  </tr>
  <tr>
    <td>split()</td>
    <td>Эквивалент функции str.split(), но принимающий на входе регулярные выражения</td>
  </tr>
  <tr>
    <td>rsplit()</td>
    <td>Эквивалент функции str.rsplit(), но принимающий на входе регулярные выражения</td>
  </tr>
</table>

С помощью этих функций можно выполнять массу интересных операций. Например, можно извлечь имя из каждого элемента, выполнив поиск непрерывной группы символов в начале каждого из них:

In[11]: monte.str.extract('([A-Za-z]+)')

Out[11]:  0    Graham
          1    John
          2    Terry
          3    Eric
          4    Terry
          5    Michael
         dtype: object

Или, например, найти все имена, начинающиеся и заканчивающиеся согласным звуком, воспользовавшись символами регулярных выражений «начало строки» (^) и «конец строки» ($):

In[12]: monte.str.findall(r'^[^AEIOU].*[^aeiou]$')

Out[12]:  0    [Graham Chapman]
          1    []
          2    [Terry Gilliam]
          3    []
          4    [Terry Jones]
          5    [Michael Palin]
         dtype: object

Такой сжатый синтаксис регулярных выражений для записей объектов Series и DataFrame открывает массу возможностей для анализа и очистки данных.