---
source_image: page_367.png
page_number: 367
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.62
tokens: 5605
characters: 1554
timestamp: 2025-12-24T04:17:12.398927
finish_reason: stop
---

customizations/two-space-indent.vim
http://media.pragprog.com/titles/dnvim/code/customizations/two-space-indent.vim

""" Оформлять отступы двумя пробелами
set tabstop=2
set softtabstop=2
set shiftwidth=2
set expandtab

Всякий раз, когда понадобится применить эти настройки к текущему буферу, достаточно будет выполнить следующую команду:

⇒ :source two-space-indent.vim

При изменении настроек на лету мы начинаем ввод с символа двоеточия, чтобы переключиться в режим командной строки. Однако, когда настройки сохраняются в файле, они необязательно должны начинаться с двоеточия, потому что команда :source предполагает, что каждая строка в указанном файле должна выполняться как команда Ex.

В момент запуска редактор Vim проверяет наличие файла с именем vimrc. Если файл найден, Vim автоматически загружает его содержимое. Благодаря этому избранные настройки можно хранить в файле vimrc, и они автоматически будут применяться при каждом запуске Vim.

Vim пытается найти файл vimrc в нескольких местах (см. :h vimrc http://vimdoc.sourceforge.net/htmldoc/starting.html#vimrc). В системах Unix пытается найти файл с именем ~/.vimrc. В Windows — файл $HOME/_vimrc. Не важно, какой системой вы пользуетесь, вы можете открыть этот файл прямо из редактора Vim следующей командой:

⇒ :edit $MYVIMRC

$MYVIMRC — это переменная окружения в Vim, хранящая путь к файлу vimrc. После сохранения изменений в файле vimrc мы можем загрузить новую конфигурацию командой

⇒ :source $MYVIMRC

Если файл vimrc открыт в активном буфере, эту команду можно сократить до :so %.