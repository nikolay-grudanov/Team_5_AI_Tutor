---
source_image: page_330.png
page_number: 330
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.97
tokens: 5619
characters: 1602
timestamp: 2025-12-24T04:16:29.503903
finish_reason: stop
---

Рецепт 107. Настройка внешнего компилятора

Настройка makeprg и errorformat единственной командой

Строка для параметра настройки errorformat достаточно сложна, чтобы удерживать ее в памяти. Однако ее можно сохранить в файл и затем активировать командой :compiler, которая является более краткой формой настройки параметров makeprg и errorformat (см. :h :compiler http://vimdoc.sourceforge.net/htmldoc/quickfix.html#:compiler):

⇒ :compiler nodelint

Команда :compiler активирует расширение компилятора (compiler plugin), которое настраивает параметры makeprg и errorformat на работу с программой nodelint. Она является примерным эквивалентом встраивания следующих строк в файл с настройками:

quickfix/ftplugin.javascript.vim
http://media.pragprog.com/titles/dnvim/code/quickfix/ftplugin.javascript.vim

setlocal makeprg=NODE_DISABLE_COLORS=1\ nodelint\ %
let &l:efm='%A'
let &l:efm='%f\, '
let &l:efm='line %l\, '
let &l:efm='character %c:'
let &l:efm='%m' . ' ,'
let &l:efm='%Z%.%#' . ' ,'
let &l:efm='%-G%.%#'

Внутреннее устройство расширения компилятора намного сложнее, но данная аппроксимация достаточно близко описывает его. Ознакомиться со списком имеющихся расширений компиляторов можно с помощью команды

⇒ :args $VIMRUNTIME/compiler/*.vim

Обратите внимание, что Vim-расширение компилятора для поддержки nodelint не входит в состав стандартного дистрибутива Vim, но его легко можно установить¹. Если предполагается постоянное использование программы nodelint в качестве «компилятора» для файлов JavaScript, можно воспользоваться расширением авто-

¹ https://github.com/bigfish/vim-nodelint