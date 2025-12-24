---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.07
tokens: 8389
characters: 1219
timestamp: 2025-12-24T02:17:58.153413
finish_reason: stop
---

4. В home.html, мы начнем с объявления типа документа:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Packt Todo Application</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZSjTc5UWRPEfHIAqiwoqQfNgAcHJzUm4WjB5+OQ6L异nEeQmH+g==crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.10/css/all.css" integrity="sha384-+d0P83n9kaQMCwj8F4RJB66tzIwOKmrdb46+porD/OvrJ+37WqIM7UoBtwHO6Nlg" crossorigin="anonymous">
    </head>
```

5. Следующим шагом является написание содержимого для тела шаблона. В тело шаблона мы включим имя приложения под тегом <header></header> и ссылку на todo_container дочернего шаблона, заключенную в тег блока. Дочерний шаблон будет написан на шаге 8.

Включите следующий код сразу после тега </head> в файл шаблона home.html:

```html
<body>
    <header>
        <nav class="navar">
            <div class="container-fluid">
                <center>
```