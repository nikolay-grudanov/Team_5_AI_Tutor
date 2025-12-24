---
source_image: page_309.png
page_number: 309
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 57.59
tokens: 11761
characters: 1885
timestamp: 2025-12-24T09:40:23.994983
finish_reason: stop
---

серверными включениями (Server-Side Includes, SSI), упрощенная версия методики HTML-сборки, применяемой на таких сайтах, как Amazon и Expedia.

По существу серверное включение — это команда, заставляющая Web-сервер вставить содержимое одного HTML-файла в другой. Предположим, что вы хотите использовать одно и то же меню на нескольких страницах. Можно было бы начать с сохранения меню в виде отдельного файла с именем menu.htm. Далее приведено его содержимое.

<h1>Menu</h1>
<a href="...">Page 1</a><br />
<a href="...">Page 2</a><br />
<a href="...">Page 3</a><br />
<a href="...">The End</a>

Обратите внимание на то, что menu.htm — не полный HTML-документ. В нем отсутствуют такие элементы, как <html>, <head> и <body>. Это всего лишь строительный блок, который вы поместите на другие полноценные HTML-страницы.

Теперь вы готовы к использованию меню на Web-странице. Для этого вставьте специальную команду include в то место страницы, где должно появиться меню. Далее показано, как это выглядит.

<!--#include file="menu.htm" -->

Команда include с помощью символов <!-- в начале и символов --> в конце маскируется под HTML-комментарий (см. врезку "Секреты ремесла" в разд. "Структурирование текста" главы 2). Но ее середина содержит реальную историю. Знак решетки (#) означает, что это команда Web-серверу, а атрибут file указывает на файл, который вы хотите использовать.

Далее приведена команда include в действии на готовой Web-странице.

<!DOCTYPE html>

<html>
<head>
    <title>Server-Side Include Test</title>
    <link rel="stylesheet" href="styles.css" />
</head>

<body>
    <div class="Header">
        <h1>Templates Rule!</h1>
    </div>

    <div class="MenuPanel">
        <!--#include file="menu.htm" -->
    </div>

    <div class="Content">
        <p>This is the welcome page. Just above this text is the handy menu for this site.</p>
    </div>
</body>
</html>