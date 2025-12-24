---
source_image: page_701.png
page_number: 701
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 75.80
tokens: 12080
characters: 2388
timestamp: 2025-12-24T03:47:40.356365
finish_reason: stop
---

<table>
  <tr>
    <th>Параметр</th>
    <th>Умолчание</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>slowopen (slow)</td>
    <td></td>
    <td>Не обновлять изображение в процессе вставки. Значение по умолчанию зависит от скорости соединения и типа терминала.</td>
  </tr>
  <tr>
    <td>tabstop= (ts)</td>
    <td>8</td>
    <td>Определить количество пробелов, содержащихся в табуляции (для текущего сеанса). Печатающее устройство будет по-прежнему использовать системную установку табулятора в 8 пробелов.</td>
  </tr>
  <tr>
    <td>taglength= (tl)</td>
    <td>0</td>
    <td>Определить количество значимых символов в теге (tag). По умолчанию параметр равен 0, т. е. значимы все символы.</td>
  </tr>
  <tr>
    <td>tags=</td>
    <td>tags/usr/lib/tags</td>
    <td>Определить полные пути файлов, содержащих теги (см. команду ctags в главе 3). По умолчанию происходит поиск файлов tags (в текущем каталоге) и /usr/lib/tags.</td>
  </tr>
  <tr>
    <td>term=</td>
    <td></td>
    <td>Задание типа терминала.</td>
  </tr>
  <tr>
    <td>terse</td>
    <td>noterse</td>
    <td>Краткие сообщения об ошибках.</td>
  </tr>
  <tr>
    <td>timeout (to)</td>
    <td>timeout</td>
    <td>Клавиатурные связки прекращают ожидание через 1 секунду.</td>
  </tr>
  <tr>
    <td>ttytype=</td>
    <td></td>
    <td>Задание типа терминала. По умолчанию принимает значение переменной окружения TERM.</td>
  </tr>
  <tr>
    <td>warn</td>
    <td>warn</td>
    <td>Отображать сообщение «No write since last change» (последние изменения не сохранены).</td>
  </tr>
  <tr>
    <td>window= (w)</td>
    <td></td>
    <td>Отображать определенное количество строк файла на экране. Значение по умолчанию зависит от скорости соединения и типа терминала.</td>
  </tr>
  <tr>
    <td>wrapmargin= (wm)</td>
    <td>0</td>
    <td>Определить правое поле страницы. Если значение больше нуля, автоматически разрывать в этом месте строку посредством вставки символа возврата каретки.</td>
  </tr>
  <tr>
    <td>wrapscan (ws)</td>
    <td>ws</td>
    <td>Кольцевой поиск по файлу (не прекращается по достижении конца или начала файла).</td>
  </tr>
  <tr>
    <td>writeany (wa)</td>
    <td>nowa</td>
    <td>Разрешить сохранение в любой файл.</td>
  </tr>
</table>

Пример файла ~/.exrc

set nowrapscan wrapmargin=7
set sections=SeAhBhChDh nomesg
map q :w^M:n^M
map v dwElp
ab ORA O'Reilly & Associates, Inc.