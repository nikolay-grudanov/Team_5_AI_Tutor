---
source_image: page_049.png
page_number: 49
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.95
tokens: 6740
characters: 2441
timestamp: 2025-12-24T10:03:54.629431
finish_reason: stop
---

The "sys" module is now called "util". It should have a similar interface.

jscheckstyle results — firefox.js

<table>
  <tr>
    <th>Line</th>
    <th>Function</th>
    <th>Length</th>
    <th>Args</th>
    <th>Complex</th>
  </tr>
  <tr>
    <td>8</td>
    <td>doSeleniumStuff</td>
    <td>20</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>26</td>
    <td>Anonymous</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>31</td>
    <td>startCapture</td>
    <td>17</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>39</td>
    <td>Anonymous</td>
    <td>6</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>40</td>
    <td>Anonymous</td>
    <td>4</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>44</td>
    <td>Anonymous</td>
    <td>3</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>49</td>
    <td>doWS</td>
    <td>40</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>62</td>
    <td>ws.onerror</td>
    <td>4</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>67</td>
    <td>ws.onopen</td>
    <td>4</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>72</td>
    <td>ws.onmessage</td>
    <td>6</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>79</td>
    <td>ws.onclose</td>
    <td>9</td>
    <td>1</td>
    <td>1</td>
  </tr>
</table>

Утилита выводит список всех функций, присутствующих в файле, число строк в каждой из функций, число аргументов каждой функции и цикломатическую сложность каждой функции. Имейте в виду, что число строк подсчитывается с включением пустых строк и строк комментариев, поэтому данное значение как-то относительно в отличие от других показателей, значения которых являются абсолютными.

Обратите внимание, что в приведенном примере фактически есть только три высокоуровневых функции. Анонимная функция в строке 26 относится к функции doSeleniumStuff. Три анонимных функции также есть в функции startCapture, а функция doWS содержит четыре функции ws.*. Таким образом, этот инструмент, к сожалению, выявляет иерархию функций в файле довольно нечетко, поэтому будьте внимательны.

Напоследок отметим, что утилита jscheckstyle может также выводить информацию в форматах JSON и HTML, для чего при ее вызове нужно использовать параметры командной строки -json и -html соответственно.

2.4. Повторное использование кода

Лучший способ уменьшить размер кода заключается в уменьшении числа написанного вами кода.