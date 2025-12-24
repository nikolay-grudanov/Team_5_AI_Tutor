---
source_image: page_262.png
page_number: 262
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.27
tokens: 5865
characters: 2399
timestamp: 2025-12-24T04:15:13.017505
finish_reason: stop
---

повторить нашу неидеальную «формулу точки», она создаст жуткое слово «langsusage». Очевидно, что это один из примеров, когда предпочтительнее было иметь возможность устанавливать курсор в конец совпадения, а не в конец слова.
В табл. 13.2 демонстрируется улучшенное решение.
Здесь выполняется поиск командой /lang/e<CR>, которая помещает курсор в конец совпадения, именно так, как нам нужно. Теперь каждый раз, когда будет выполняться команда n, курсор будет устанавливаться в конец найденного совпадения, подготавливая почву для команды «точка». Итак, использование смещения в совпадении помогло нам получить идеальную «формулу точки».

Таблица 13.2. Улучшенное решение с использованием «формулы точки»

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Aim to learn a new programming lang each year.<br>Which lang did you pick up last year?<br>Which langs would you like to learn?</td>
  </tr>
  <tr>
    <td>/lang/e<CR></td>
    <td>Aim to learn a new programming lang each year.<br>Which lang did you pick up last year?<br>Which langs would you like to learn?</td>
  </tr>
  <tr>
    <td>auage<Esc></td>
    <td>Aim to learn a new programming language each year.<br>Which lang did you pick up last year?<br>Which langs would you like to learn?</td>
  </tr>
  <tr>
    <td>n</td>
    <td>Aim to learn a new programming language each year.<br>Which lang did you pick up last year?<br>Which langs would you like to learn?</td>
  </tr>
  <tr>
    <td>.</td>
    <td>Aim to learn a new programming language each year.<br>Which language did you pick up last year?<br>Which langs would you like to learn?</td>
  </tr>
  <tr>
    <td>n.</td>
    <td>Aim to learn a new programming language each year.<br>Which language did you pick up last year?<br>Which languages would you like to learn?</td>
  </tr>
</table>

На практике не всегда очевидно, когда применение смещений в совпадениях может принести выгоду. Представьте, что мы начали выполнять команду поиска без смещения, но, выполнив команду n пару раз, поняли, что было бы удобно, если бы курсор устанавливался в конец совпадения. Эта проблема легко решается, достаточно выполнить команду //e<CR>. Когда поле шаблона остается пустым, как в данном случае, Vim будет повторно использовать предыдущий шаблон. То есть данная команда повторит предыдущую команду поиска, но со смещением.