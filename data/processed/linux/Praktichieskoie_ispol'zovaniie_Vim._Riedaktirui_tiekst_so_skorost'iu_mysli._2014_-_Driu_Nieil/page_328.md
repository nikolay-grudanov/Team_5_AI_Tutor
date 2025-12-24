---
source_image: page_328.png
page_number: 328
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.39
tokens: 5578
characters: 1396
timestamp: 2025-12-24T04:16:25.691836
finish_reason: stop
---

Рецепт 107. Настройка внешнего компилятора

⇒ $ npm install nodelint -g

Для демонстрации мы будем использовать следующий файл JavaScript:

quickfix/fizzbuzz.js
http://media.pragprog.com/titles/dnvim/code/quickfix/fizzbuzz.js

var i;
for (i=1; i <= 100; i++) {
    if(i % 15 == 0) {
        console.log('Fizzbuzz');
    } else if(i % 5 == 0) {
        console.log('Buzz');
    } else if(i % 3 == 0) {
        console.log('Fizz');
    } else {
        console.log(i);
    }
};

Настройка вызова программы Nodelint командой :make

Определить программу, которую должна вызывать команда :make, можно с помощью параметра настройки makeprg (см. :h 'makeprg' http://vimdoc.sourceforge.net/htmldoc/options.html#'makeprg'), как показано ниже:

⇒ :setlocal makeprg=NODE_DISABLE_COLORS=1\ nodelint\ %

На место символа % будет поставлен путь к текущему файлу. То есть, если редактируется файл ~/quickfix/fizzbuzz.js, вызов команды :make в редакторе Vim будет эквивалентен вызову следующей команды в оболочке:

⇒ $ export NODE_DISABLE_COLORS=1
⇒ $ nodelint ~/quickfix/fizzbuzz.js
~/quickfix/fizzbuzz.js, line 2, character 22: Unexpected '++'.
~/quickfix/fizzbuzz.js, line 3, character 15: Expected '===' ...
~/quickfix/fizzbuzz.js, line 5, character 21: Expected '===' ...
~/quickfix/fizzbuzz.js, line 7, character 21: Expected '===' ...
~/quickfix/fizzbuzz.js, line 12, character 2: Unexpected ';'.
5 errors