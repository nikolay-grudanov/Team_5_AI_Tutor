---
source_image: page_368.png
page_number: 368
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.14
tokens: 6229
characters: 3817
timestamp: 2025-12-24T07:25:26.051560
finish_reason: stop
---

несущественны: для определенности будем считать, что они во всех клетках различны.)

Случай 1: входные алфавиты исходных автоматов не пересекаются. Пусть \( A_1 = \{a, b, c\}, A_2 = \{d, f\}, A_3 = \{g, h, i\} \). Тогда схеме на рис. 8.9 соответствует табл. 8.9, а. В ней заключительные состояния отождествлены с начальными состояниями последующих автоматов (аналогичные преобразования производились при композиции машин Тьюринга в § 5.2). Полученную таблицу переходов можно минимизировать по правилам минимизации частичных автоматов; результат приведен в табл. 8.9, б. Разумеется, автомат, описываемый в табл. 8.9, б, будет работать в соответствии с блок-схемой рис. 8.9 только в том случае, если в нужные моменты времени будут происходить «переключения внешней среды», т. е. переходы от алфавита \( A_1 \) к алфавиту \( A_2 \) и т. д. Поскольку эти моменты соответствуют переходам от одного подавтомата к другому и, следовательно, автоматом с табл. 8.9, б распознаются, то переключения можно осуществлять с помощью выходных сигналов. В нашем примере переключающими сигналами будут \( \lambda(1, b), \lambda(2, a), \lambda(2, d), \lambda(1, h), \lambda(2, g), \lambda(2, h) \). Итак, в этом случае блок-схема из автоматов — это также автомат, алфавит которого является

<table>
  <tr>
    <th rowspan="2">q<sub>ij</sub></th>
    <th colspan="3">a</th>
    <th colspan="3">b</th>
    <th colspan="3">c</th>
    <th colspan="3">d</th>
    <th colspan="3">f</th>
    <th colspan="3">g</th>
    <th colspan="3">h</th>
    <th colspan="3">i</th>
  </tr>
  <tr>
    <th>a</th><th>b</th><th>c</th>
    <th>d</th><th>f</th><th>g</th>
    <th>h</th><th>i</th>
  </tr>
  <tr>
    <td>q<sub>11</sub></td>
    <td>q<sub>11</sub></td><td>q<sub>21</sub></td><td>q<sub>12</sub></td>
    <td></td><td></td><td></td>
    <td></td><td></td>
  </tr>
  <tr>
    <td>q<sub>12</sub></td>
    <td>q<sub>21</sub></td><td>q<sub>11</sub></td><td>q<sub>12</sub></td>
    <td></td><td></td><td></td>
    <td></td><td></td>
  </tr>
  <tr>
    <td>q<sub>21</sub></td>
    <td></td><td></td><td></td>
    <td>q<sub>23</sub></td><td>q<sub>22</sub></td>
    <td></td><td></td><td></td>
  </tr>
  <tr>
    <td>q<sub>22</sub></td>
    <td></td><td></td><td></td>
    <td>q<sub>31</sub></td><td>q<sub>22</sub></td>
    <td></td><td></td><td></td>
  </tr>
  <tr>
    <td>q<sub>23</sub></td>
    <td></td><td></td><td></td>
    <td>q<sub>21</sub></td><td>q<sub>23</sub></td>
    <td></td><td></td><td></td>
  </tr>
  <tr>
    <td>q<sub>31</sub></td>
    <td></td><td></td><td></td>
    <td></td><td></td>
    <td>q<sub>31</sub></td><td>q<sub>21</sub></td><td>q<sub>32</sub></td>
  </tr>
  <tr>
    <td>q<sub>32</sub></td>
    <td></td><td></td><td></td>
    <td></td><td></td>
    <td>q<sub>11</sub></td><td>q<sub>11</sub></td><td>q<sub>31</sub></td>
  </tr>
</table>

Таблица 8.9

<table>
  <tr>
    <th rowspan="2">q<sub>ij</sub></th>
    <th colspan="3">a</th>
    <th colspan="3">b</th>
    <th colspan="3">c</th>
    <th colspan="3">d</th>
    <th colspan="3">f</th>
    <th colspan="3">g</th>
    <th colspan="3">h</th>
    <th colspan="3">i</th>
  </tr>
  <tr>
    <th>1</th><th>2</th><th>3</th>
    <th>1</th><th>2</th><th>3</th>
    <th>1</th><th>2</th><th>3</th>
    <th>1</th><th>2</th><th>3</th>
    <th>1</th><th>2</th><th>3</th>
    <th>1</th><th>2</th><th>3</th>
    <th>1</th><th>2</th><th>3</th>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td><td>1</td><td>2</td>
    <td>3</td><td>2</td><td>1</td>
    <td>1</td><td>1</td><td>2</td>
  </tr>
  <tr>
    <td>2</td>
    <td>1</td><td>1</td><td>2</td>
    <td>1</td><td>2</td><td>1</td>
    <td>1</td><td>1</td><td>1</td>
  </tr>
  <tr>
    <td>3</td>
    <td>--</td><td>--</td><td>--</td>
    <td>1</td><td>3</td><td>--</td>
    <td>--</td><td>--</td><td>--</td>
  </tr>
</table>

Таблица 8.9