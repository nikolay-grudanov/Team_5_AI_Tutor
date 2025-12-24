---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.67
tokens: 5737
characters: 1586
timestamp: 2025-12-24T04:14:15.632595
finish_reason: stop
---

Таблица 11.2. Воспроизведение макроса

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>
      1. one<br>
      2. two<br>
      // break up the monotony<br>
      3. three<br>
      4. four
    </td>
  </tr>
  <tr>
    <td>5@a</td>
    <td>
      1) One<br>
      2) Two<br>
      // break up the monotony<br>
      3. three<br>
      4. four
    </td>
  </tr>
</table>

Но задача фактически не была решена. Мы просили Vim выполнить макрос пять раз, а он сбежал на третьем повторении. Поэтому нам придется вызвать макрос еще раз, со следующей строки, чтобы выполнить работу до конца. Давайте посмотрим на альтернативное решение.

Параллельное выполнение макроса

В рецепте 30 (глава 5) демонстрировался способ применения команды «точка» к непрерывной последовательности строк. Этот же прием можно использовать и в данном случае:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>qa</td>
    <td>1. one</td>
  </tr>
  <tr>
    <td>0f.r)w~</td>
    <td>1) One</td>
  </tr>
  <tr>
    <td>q</td>
    <td>1) One</td>
  </tr>
  <tr>
    <td>jVG</td>
    <td>
      1) One<br>
      2. two<br>
      // break up the monotony<br>
      3. three<br>
      4. four
    </td>
  </tr>
  <tr>
    <td>:'<,'>normal @a</td>
    <td>
      1) One<br>
      2) Two<br>
      // break up the monotony<br>
      3) Three<br>
      4) Four
    </td>
  </tr>
</table>

Мы повторно записали макрос с самого начала. Он получился практически идентичным предыдущему, кроме того что мы опусти-