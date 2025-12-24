---
source_image: page_310.png
page_number: 310
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.10
tokens: 11537
characters: 1094
timestamp: 2025-12-24T09:39:59.806812
finish_reason: stop
---

<div>
</div>
</body>
</html>

Когда запрашивается эта страница, Web-сервер сканирует ее в поисках команд. Когда он находит команду include, то извлекает заданный файл и вставляет его содержимое в это место Web-страницы. Затем он отправляет окончательный обработанный файл вам. В данном примере это означает, что ваш Web-браузер получает Web-страницу, выглядящую следующим образом (рис. 10.2).

![Web-страница с многократно используемыми элементами](../images/ch10_02.png)

Рис. 10.2. Хоть эта страница и выглядит обычно, ее отображение не обошлось без магии. Перед тем как послать эту страницу вам, Web-сервер считывает из отдельного файла ссылки меню и вставляет их на страницу

<!DOCTYPE html>

<html>
<head>
    <title>Server-Side Include Test</title>
    <link rel="stylesheet" href="styles.css" />
</head>

<body>
    <div class="Header">
        <h1>Welcome to a Multipart Page</h1>
    </div>

    <div class="MenuPanel">
        <h1>Menu</h1>
        <a href="...">Page 1</a><br />
        <a href="...">Page 2</a><br />
        <a href="...">Page 3</a><br />
    </div>
</body>
</html>