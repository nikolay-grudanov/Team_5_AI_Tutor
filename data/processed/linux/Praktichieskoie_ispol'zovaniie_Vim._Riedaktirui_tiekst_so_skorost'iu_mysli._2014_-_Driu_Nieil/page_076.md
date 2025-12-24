---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.26
tokens: 5777
characters: 2081
timestamp: 2025-12-24T04:11:12.712557
finish_reason: stop
---

Допустим, что у нас имеется такой фрагмент текста:

insert_mode/replace.txt
http://media.pragprog.com/titles/dnvim/code/insert_mode/replace.txt

Typing in Insert mode extends the line. But in Replace mode the line length doesn’t change.

Нам необходимо объединить два предложения в одно, заменив точку запятой. Кроме того, требуется символ «В» в слове «But» заменить символом «b». Следующий пример демонстрирует, как можно выполнить эту правку в режиме замены.

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Typing in Insert mode extends the line. But in Replace mode the line length doesn’t change.</td>
  </tr>
  <tr>
    <td>f.</td>
    <td>Typing in Insert mode extends the line. But in Replace mode the line length doesn’t change.</td>
  </tr>
  <tr>
    <td>R, b<Esc></td>
    <td>Typing in Insert mode extends the line, but in Replace mode the line length doesn’t change.</td>
  </tr>
</table>

Переход в режим замены из командного режима выполняется командой R. Как видно в примере выше, вводимые символы «, b» затирают имеющиеся «. В». Закончив правку в режиме замены, можно нажать клавишу <Esc> и вернуться в командный режим. Не на всех клавиатурах имеется клавиша <Insert>, но если у вас она есть, вы можете использовать ее для переключения между режимами вставки и замены.

Затирайте символы табуляции в виртуальном режиме замены

Некоторые символы могут осложнять работу в режиме замены. Примером таких символов могут служить символы табуляции. В файле символ табуляции представлен единственным символом, но на экране он может занимать несколько знакомест, согласно настройке tabstop (см. :h ‘tabstop’ http://vimdoc.sourceforge.net/html/doc/options.html#’tabstop’). Если поместить курсор в позицию символа табуляции и инициировать режим замены, следующий введенный символ затрет символ табуляции. Допустим, что параметр настройки tabstop имеет значение 8 (по умолчанию), тогда может создаться ощущение, что один символ заменил восемь пробелов, вызвав значительное сокращение длины текущей строки.