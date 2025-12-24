---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.63
tokens: 7759
characters: 2177
timestamp: 2025-12-24T10:48:57.114186
finish_reason: stop
---

Строковые срезы

Строковый срез — это ссылка на часть значения типа String. Он выглядит следующим образом:

let s = String::from("hello world");

let hello = &s[0..5];
① let world = &s[6..11];

Он похож на взятие ссылки на все значение типа String, но с дополнительным фрагментом [0..5]. Вместо ссылки на все значение типа String срез является ссылкой на часть значения типа String.

Мы можем создавать срезы, используя интервал внутри скобок, указав [starting_index..ending_index], где starting_index — это первая позиция в срезе, а ending_index — на одну позицию больше, чем последняя позиция в срезе. Внутренне срезовая структура данных хранит начальную позицию и длину среза, которая соответствует ending_index минус starting_index. Таким образом, в ① переменная world будет срезом, который содержит указатель на 7-й байт переменной s со значением длины, равным 5.

Рисунок 4.6 показывает это на схеме.

<table>
  <tr>
    <th>имя</th>
    <th>значение</th>
    <th>указатель</th>
    <th>значение</th>
  </tr>
  <tr>
    <td>ptr</td>
    <td></td>
    <td>0</td>
    <td>h</td>
  </tr>
  <tr>
    <td>длина</td>
    <td>5</td>
    <td>1</td>
    <td>e</td>
  </tr>
  <tr>
    <td>емкость</td>
    <td>5</td>
    <td>2</td>
    <td>l</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>3</td>
    <td>l</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>4</td>
    <td>o</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>5</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>6</td>
    <td>w</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>7</td>
    <td>o</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>8</td>
    <td>r</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>9</td>
    <td>l</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>10</td>
    <td>d</td>
  </tr>
</table>

Рис. 4.6. Срез значения типа String, ссылающийся на часть значения

С помощью интервального синтаксиса .. языка Rust, если вы хотите начать с первого индекса (нуля), то вы можете отбросить значение перед двумя точками. Другими словами, варианты ниже равны:

let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];