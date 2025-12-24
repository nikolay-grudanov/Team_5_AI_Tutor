---
source_image: page_014.png
page_number: 14
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.51
tokens: 7344
characters: 1297
timestamp: 2025-12-24T09:20:50.931273
finish_reason: stop
---

Здесь не описаны редко используемые свойства CSS (или те, которые на момент написания книги не имели полной поддержки основных браузеров). Они бы только все запутали.

Мы сосредоточимся только на свойствах, которые в настоящее время широко применяются веб-дизайнерами и разработчиками. Много усилий было уделено созданию схем grid- и flex-верстки. Помимо этого, я включил краткое руководство по SASS/SCSS, но выбрал только наиболее важные функции, о которых вы должны знать.

1.1. Внешнее размещение

Код CSS можно сохранить в отдельном внешнем файле (например, style.css) и включить с помощью HTML-элемента link.

Исходный код файла style.css:

001 body p
002 {
003     background: white;
004     color: black;
005     font-family: Arial, sans-serif;
006     font-size: 16px;
007     line-height: 1.58;
008     text-rendering: optimizeLegibility;
009     -webkit-font-smoothing: antialiased;
010 }

Пример ссылки на внешний CSS-файл:

001 <html>
002     <head>
003         <title>Добро пожаловать на сайт.</title>
004         <link rel = "stylesheet"
005             type = "text/css"
006             href = "style.css" />
007     </head>
008     <body>
009         <p>CSS-стили записаны в файле style.css
010             и применяются к содержимому этой страницы.</p>
011     </body>
012 </html>