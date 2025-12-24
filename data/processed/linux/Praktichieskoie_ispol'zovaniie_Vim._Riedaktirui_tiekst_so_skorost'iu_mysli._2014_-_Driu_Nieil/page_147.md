---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.12
tokens: 5502
characters: 1271
timestamp: 2025-12-24T04:12:31.505572
finish_reason: stop
---

Подготовка

Функциональность, описываемая в этом рецепте, не входит в базовый набор функций Vim, но поддерживается расширением netrw. Это расширение распространяется в составе стандартного дистрибутива Vim, поэтому вам не придется заниматься его установкой — только настроить загрузку расширений в Vim. Ниже приводятся строки, которые следует добавить в файл vimrc:

essential.vim
http://media.pragprog.com/titles/dnvim/code/essential.vim

set nocompatible
filetype plugin on

Встречайте: netrw — встроенный обозреватель файлов Vim

Если запустить Vim, передав ему путь к каталогу, а не к файлу, он откроет окно обозревателя файлов:

⇒ $ cd code/file/mvc
⇒ $ ls
    app        app.js   index.html   lib
⇒ $ vim .

На рис. 7.1 показано, как выглядит этот обозреватель. Это обычный буфер Vim, но вместо содержимого файла он представляет содержимое каталога.

" =====================================================================
" Netrw Directory Listing
"   /Users/drew/code/mvc
"   Sorted by name
"   Sort sequence: [\/]$,\<core\%(\.\d\+\/)\=\>,\.h$,\.c$,\.c
"   Quick Help: <F1>:help -:go up dir  D:delete  R:rename
" =====================================================================
./
app/
lib/
app.js
index.html

Рис. 7.1. netrw — встроенный обозреватель файлов