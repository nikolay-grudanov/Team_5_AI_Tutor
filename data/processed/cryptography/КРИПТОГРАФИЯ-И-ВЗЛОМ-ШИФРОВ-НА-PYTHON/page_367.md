---
source_image: page_367.png
page_number: 367
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.69
tokens: 8035
characters: 2599
timestamp: 2025-12-24T08:55:39.380273
finish_reason: stop
---

<table>
  <tr>
    <th>Подключ</th>
    <th>Дешифрование</th>
    <th>Оценка частотного соответствия</th>
  </tr>
  <tr>
    <td>'H'</td>
    <td>'ITXUTUTGSBTATDWQTTTDBN'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'I'</td>
    <td>'HSWTSTSFRASZSCVPSSSCAM'</td>
    <td>2</td>
  </tr>
  <tr>
    <td>'J'</td>
    <td>'GRVSRSRSEQZRYRBUORRRBZL'</td>
    <td>0</td>
  </tr>
  <tr>
    <td>'K'</td>
    <td>'FQUQRQRDPYQXQATNQQQAYK'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'L'</td>
    <td>'EPTQPQPCOXPWPZSMPPPZXJ'</td>
    <td>0</td>
  </tr>
  <tr>
    <td>'M'</td>
    <td>'DOSPOPOBNWOVOYRL000YWI'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'N'</td>
    <td>'CNRONONAMVNUNXQKNNNXVH'</td>
    <td>2</td>
  </tr>
  <tr>
    <td>'O'</td>
    <td>'BMQNMNZLUMTMWPJMMMWWUG'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'P'</td>
    <td>'ALPMLMLYKTLSLVOILLLVTF'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'Q'</td>
    <td>'ZKOLKLKXJSKRKUNHKKKUSE'</td>
    <td>0</td>
  </tr>
  <tr>
    <td>'R'</td>
    <td>'YJNKJKJWIRJQJTMGJJJTRD'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'S'</td>
    <td>'XIMJIJIVHQIPISLFIIISQC'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'T'</td>
    <td>'WHLIHIHUGPHOHHRKEHHHRPB'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'U'</td>
    <td>'VGKHGHGTFOGNGQJDGGGQOA'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'V'</td>
    <td>'UFJGFGESENFMFPICFFFPNZ'</td>
    <td>1</td>
  </tr>
  <tr>
    <td>'W'</td>
    <td>'TEIFEFERDMELEOHBEEEOMY'</td>
    <td>2</td>
  </tr>
  <tr>
    <td>'X'</td>
    <td>'SDHEDEDQCLDKDNGADDDNLX'</td>
    <td>2</td>
  </tr>
  <tr>
    <td>'Y'</td>
    <td>'RCGDCDCPBKCJCMFZCCCMKW'</td>
    <td>0</td>
  </tr>
  <tr>
    <td>'Z'</td>
    <td>'QBFCBCBOAJBIBLEYBBBLJV'</td>
    <td>0</td>
  </tr>
</table>

Подключи, которые приводят к получению вариантов дешифрования с наибольшей оценкой, являются самыми вероятными кандидатами на роль реального ключа. В табл. 20.4 подключи 'A', 'I', 'N', 'W' и 'X' дают наивысшую оценку частотного соответствия для первой строки. Обратите внимание на то, что оценки в целом имеют низкие значения, поскольку объем шифротекста не позволяет получить достаточно длинную тестовую строку, но для данного примера этого вполне достаточно.

Следующий шаг заключается в повторении этого процесса для остальных трех строк с целью выявления наиболее вероятных вариантов подключей. Окончательные результаты приведены в табл. 20.5.

Поскольку для первой строки существуют пять возможных подключей, для второй — два, для третьей — один и для четвертой — пять, общее количество возможных комбинаций составляет 50 (5 · 2 · 1 · 5). Другими слова-