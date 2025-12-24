---
source_image: page_351.png
page_number: 351
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.46
tokens: 5635
characters: 1569
timestamp: 2025-12-24T04:16:52.745016
finish_reason: stop
---

auto_complete/webapp/public/index.html
http://media.pragprog.com/titles/dnvim/code/auto_complete/webapp/public/index.html

<!DOCTYPE html>
<html>
<head>
    <title>Practical Vim - the app</title>
    <script src="" type="text/javascript"></script>
</head>
<body></body>
</html>

Нам нужно подставить в атрибут src="" ссылку на файл application.js. Но если воспользоваться функцией автодополнения имен файлов, у нас возникнут сложности:

⇒ :pwd
webapp

Если вызвать автодополнение имен файлов прямо сейчас, она добавит относительный путь к файлу, начинающийся в каталоге webapp, дав нам в результате: src="public/js/application.js". А нам в действительности требуется такая ссылка: src="js/application.js". Чтобы воспользоваться функцией автодополнения имен файлов в данной ситуации, необходимо сначала перейти в каталог public:

⇒ :cd public

Теперь можно вызвать функцию автодополнения имен файлов, и на этот раз она будет подставлять пути относительно каталога webapp/public:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>i</td>
    <td>&lt;script src=""/&gt;</td>
  </tr>
  <tr>
    <td>js/ap</td>
    <td>&lt;script src="js/ap"/&gt;</td>
  </tr>
  <tr>
    <td>&lt;C-x&gt;&lt;C-f&gt;</td>
    <td>&lt;script src="js/application.js"/&gt;</td>
  </tr>
</table>

После вставки пути к файлу можно вернуться обратно, в первоначальный рабочий каталог:

⇒ :cd -

Как и в командной оболочке, команда :cd- выполнит переход в предыдущий рабочий каталог (см. :h :cd- http://vimdoc.sourceforge.net/htmldoc/editing.html#:cd-).