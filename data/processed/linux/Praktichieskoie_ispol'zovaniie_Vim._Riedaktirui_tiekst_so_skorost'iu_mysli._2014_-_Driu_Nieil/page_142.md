---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.19
tokens: 5445
characters: 1172
timestamp: 2025-12-24T04:12:27.670651
finish_reason: stop
---

app.js
index.html
app/
    controllers/
        Mailer.js
        Main.js
        Navigation.js
    models/
        User.js
    views/
        Home.js
        Main.js
        Settings.js
    lib/
        framework.js
        theme.css

В командной оболочке выполните переход в каталог files/mvc и затем запустите Vim:

⇒ $ cd code/files/mvc
⇒ $ vim index.html

Как открыть файл, указав путь относительно текущего рабочего каталога

В редакторе Vim, так же как в bash и других командных оболочках, существует понятие текущего рабочего каталога. Когда Vim запускается, его текущим рабочим каталогом становится текущий рабочий каталог оболочки. Проверить это можно с помощью команды Ex :pwd, название которой (как и в bash) происходит от англ. «print working directory» (вывести текущий рабочий каталог):

⇒ :pwd
/Users/drew/practical-vim/code/files/mvc

Команда :edit {file} может принимать пути к файлам, откладываемые относительно текущего рабочего каталога. Например, чтобы открыть файл lib/framework.js, достаточно выполнить следующую команду:

⇒ :edit lib/framework.js

А открыть файл app/controllers/Navigation.js можно командой:

⇒ :edit app/controllers/Navigation.js