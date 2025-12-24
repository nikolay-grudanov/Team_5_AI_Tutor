---
source_image: page_448.png
page_number: 448
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.38
tokens: 6180
characters: 3507
timestamp: 2025-12-24T07:16:30.782494
finish_reason: stop
---

В представлении подстановками можно положить:
e — единица, \( a = (1\ 2\ 3\ 4) \), \( b = (13)(24) \), \( c = (1432) \);
2) четверная группа с элементами \( e, a, b, c \) и таблицей

<table>
  <tr>
    <th></th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
  </tr>
  <tr>
    <td>e</td>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <td>a</td>
    <td>a</td>
    <td>e</td>
    <td>c</td>
    <td>b</td>
  </tr>
  <tr>
    <td>b</td>
    <td>b</td>
    <td>c</td>
    <td>e</td>
    <td>a</td>
  </tr>
  <tr>
    <td>c</td>
    <td>c</td>
    <td>b</td>
    <td>a</td>
    <td>e</td>
  </tr>
</table>

В представлении подстановками можно положить:
e — единица, \( a = (1\ 2)(3\ 4) \), \( b = (13)(24) \), \( c = (14)(23) \).

в) Две группы:
1) циклическая группа шестого порядка с элементами \( e, a, b, c, d, f \) и таблицей

<table>
  <tr>
    <th></th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
    <th>d</th>
    <th>f</th>
  </tr>
  <tr>
    <td>e</td>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
    <td>d</td>
    <td>f</td>
  </tr>
  <tr>
    <td>a</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
    <td>d</td>
    <td>f</td>
    <td>e</td>
  </tr>
  <tr>
    <td>b</td>
    <td>b</td>
    <td>c</td>
    <td>d</td>
    <td>f</td>
    <td>e</td>
    <td>a</td>
  </tr>
  <tr>
    <td>c</td>
    <td>c</td>
    <td>d</td>
    <td>f</td>
    <td>e</td>
    <td>a</td>
    <td>b</td>
  </tr>
  <tr>
    <td>d</td>
    <td>d</td>
    <td>f</td>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <td>f</td>
    <td>f</td>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
    <td>d</td>
  </tr>
</table>

В представлении подстановками можно положить:
e — единица, \( a = (1\ 2\ 3\ 4\ 5\ 6) \), \( b = (135)(246) \), \( c = (14)(25)(36) \), \( d = (153)(264) \), \( f = (165432) \);
2) симметрическая группа третьей степени с элементами \( e, a, b, c, d, f \) и таблицей

<table>
  <tr>
    <th></th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
    <th>d</th>
    <th>f</th>
  </tr>
  <tr>
    <td>e</td>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
    <td>d</td>
    <td>f</td>
  </tr>
  <tr>
    <td>a</td>
    <td>a</td>
    <td>b</td>
    <td>e</td>
    <td>d</td>
    <td>f</td>
    <td>c</td>
  </tr>
  <tr>
    <td>b</td>
    <td>b</td>
    <td>e</td>
    <td>a</td>
    <td>f</td>
    <td>c</td>
    <td>d</td>
  </tr>
  <tr>
    <td>c</td>
    <td>c</td>
    <td>f</td>
    <td>d</td>
    <td>e</td>
    <td>b</td>
    <td>a</td>
  </tr>
  <tr>
    <td>d</td>
    <td>d</td>
    <td>c</td>
    <td>f</td>
    <td>a</td>
    <td>e</td>
    <td>b</td>
  </tr>
  <tr>
    <td>f</td>
    <td>f</td>
    <td>d</td>
    <td>c</td>
    <td>b</td>
    <td>a</td>
    <td>e</td>
  </tr>
</table>

В представлении подстановками можно положить:
e — единица; \( a = (1\ 2\ 3) \), \( b = (1\ 3\ 2) \), \( c = (1\ 2) \), \( d = (2\ 3) \), \( f = (1\ 3) \).

Указание. Показать, что если в группе \( G \) порядка \( n \) имеется множество \( H \) из \( k \) элементов, \( k < n \), которое само является группой при операции умножения, заданной в \( G \), то, умножая все элементы из \( H \) на элемент \( x \), не лежащий в \( H \), мы получим \( k \) новых элементов группы \( G \). Поэтому \( k \geqslant \frac{n}{2} \). За \( H \) можно взять множество элементов \( e, a, a^2, \ldots, a^{k-1} \), где \( a^k = e \). Например, в случае в) 2), т. е. для