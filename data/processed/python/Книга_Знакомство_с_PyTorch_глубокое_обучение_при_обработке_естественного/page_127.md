---
source_image: page_127.png
page_number: 127
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.36
tokens: 7664
characters: 2147
timestamp: 2025-12-24T02:24:38.458097
finish_reason: stop
---

<table>
  <tr>
    <th>Input[5]</th>
    <td># Связь 6: тропонимия (отличия в способе осуществления действия)<br>embeddings.compute_and_print_analogy('talk', 'communicate', 'read')</td>
  </tr>
  <tr>
    <th>Output[5]</th>
    <td>talk : communicate :: read : interpret</td>
  </tr>
  <tr>
    <th>Input[6]</th>
    <td># Связь 7: метонимия (соглашения/фигуры речи)<br>embeddings.compute_and_print_analogy('blue', 'democrat', 'red')</td>
  </tr>
  <tr>
    <th>Output[6]</th>
    <td>blue : democrat :: red : republican</td>
  </tr>
  <tr>
    <th>Input[7]</th>
    <td># Связь 8: степени прилагательных<br>embeddings.compute_and_print_analogy('fast', 'fastest', 'young')</td>
  </tr>
  <tr>
    <th>Output[7]</th>
    <td>fast : fastest :: young : youngest</td>
  </tr>
</table>

Хотя может показаться, что связи четко отражают функционирование языка, не все так просто. Как демонстрирует пример 5.4, связи могут неверно определяться, поскольку векторы слов определяются на основе их совместной встречаемости.

Пример 5.4. Пример, иллюстрирующий опасность кодирования смысла слов на основе совместной встречаемости, — иногда это не работает!

<table>
  <tr>
    <th>Input[0]</th>
    <td>embeddings.compute_and_print_analogy('fast', 'fastest', 'small')</td>
  </tr>
  <tr>
    <th>Output[0]</th>
    <td>fast : fastest :: small : largest</td>
  </tr>
</table>

Пример 5.5 иллюстрирует одно из самых распространенных сочетаний при кодировании гендерных ролей.

Пример 5.5. Осторожнее с защищаемыми атрибутами, например с гендером, кодируемыми вложениями слов. Они могут приводить к нежелательной предвзятости в дальнейших моделях

<table>
  <tr>
    <th>Input[0]</th>
    <td>embeddings.compute_and_print_analogy('man', 'king', 'woman')</td>
  </tr>
  <tr>
    <th>Output[0]</th>
    <td>man : king :: woman : queen</td>
  </tr>
</table>

Оказывается, довольно сложно различить закономерности языка и закоренелые культурные предубеждения. Например, доктора отнюдь не всегда мужчины, а медсестры не всегда женщины, но подобные предубеждения настолько устоялись, что отразились в языке, а в результате и в векторах слов, как показано в примере 5.6.