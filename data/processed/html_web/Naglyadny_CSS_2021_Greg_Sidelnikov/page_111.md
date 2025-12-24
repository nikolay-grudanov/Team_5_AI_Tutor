---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.22
tokens: 7180
characters: 961
timestamp: 2025-12-24T09:23:14.073239
finish_reason: stop
---

16 Границы

Границы CSS — это гораздо больше, чем кажется на первый взгляд. В частности, вы хотите узнать, как радиус границы (только если указаны значения для осей X и Y) влияет на другие углы того же элемента. Но прежде, чем двигаться вперед, рассмотрим свойство border.

Вы можете легко получить доступ ко всем тем же свойствам CSS через JavaScript. Например, чтобы получить доступ ко всем свойствам CSS, просто возьмите объект с помощью кода document.getElementById("container"). Свойства привязаны к свойству объекта element.style:

<body style = "margin: 30px;">
    <div id = "container">
        <div style = "width: 100%; height: 100%; background: white;">CSS Is Awesome.</div>
    </div>
</body>

var x = document.getElementById("container");
x.style.fontSize = "25px";
x.style.lineHeight = "50px";
x.style.width = "500px";
x.style.height = "200px";
x.style.border = "30px solid silver";
x.style.background = "url(diag.png)";
x.style.padding = "30px";