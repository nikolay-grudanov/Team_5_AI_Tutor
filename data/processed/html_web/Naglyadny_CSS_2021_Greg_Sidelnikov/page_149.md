---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.84
tokens: 7243
characters: 914
timestamp: 2025-12-24T09:23:58.812867
finish_reason: stop
---

ку промежуток, занимаемый элементом 1 в grid-макете, вытолкнул элемент 3 из исходного grid-шаблона. В таблице это было бы невозможно.

<table id = "tab">
  <tr>
    <td colspan = "2" rowspan = "2">1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>3</td>
  </tr>
  <tr>
    <td>4</td>
    <td>5</td>
    <td>6</td>
  </tr>
  <tr>
    <td>7</td>
    <td>8</td>
    <td>9</td>
  </tr>
</table>

#item1{
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 2;
}

21.4. Свойство grid-auto-rows

Свойство grid-auto-row в grid-макетах позволяет настраивать высоту автоматических (неявно созданных) строк. Да, им можно присвоить другое значение!

Вместо того чтобы наследовать значения от свойств grid-template-rows, можно указать конкретную высоту всех неявных строк, которые выходят за пределы ваших стандартных определений.

Неявно указанная высота строки определяется свойством grid-auto-rows: