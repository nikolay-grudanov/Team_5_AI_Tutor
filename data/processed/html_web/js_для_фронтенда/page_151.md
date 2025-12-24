---
source_image: page_151.png
page_number: 151
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.22
tokens: 6025
characters: 759
timestamp: 2025-12-24T10:05:26.950493
finish_reason: stop
---

У вас должна получиться структура каталогов, подобная изображенной на рис. 4.3.

Как видно из рис. 4.3, каталог test зеркально отображает дерево src. Для каждого файла из каталога src в каталоге test есть соответствующий ему тестовый файл. Файл связующего звена, test_user_view.html, выглядит примерно так:

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>User View Tests</title>
</head>
<body class="yui3-skin-sam">
    <h1>Test User View</h1>
    <div id="log" />
    <script src="http://yui.yahooapis.com/3.18.1/build/yui/yui-min.js">
    </script>
    <script src="../../src/frontend/user/userView.js"></script>
</body>
</html>