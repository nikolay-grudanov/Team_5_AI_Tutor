---
source_image: page_368.png
page_number: 368
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.54
tokens: 5599
characters: 1775
timestamp: 2025-12-24T04:17:12.357842
finish_reason: stop
---

A1.3. Применение настроек для определенных типов файлов

Наши предпочтения могут отличаться для файлов разных типов. Например, допустим, что мы следуем рекомендациям по оформлению исходных текстов, которые в языке Ruby советуют использовать отступы шириной два пробела, а в языке JavaScript — четыре. Мы можем воплотить эти рекомендации, добавив следующие строки в файл vimrc:

customizations/filetype-indentation.vim
http://media.pragprog.com/titles/dnvim/code/customizations/filetype-indentation.vim

if has("autocmd")
    filetype on
    autocmd FileType ruby setlocal ts=2 sts=2 sw=2 et
    autocmd FileType javascript setlocal ts=4 sts=4 sw=4 noet
endif

Объявление autocmd сообщает редактору организовать прием указанного события и выполнять указанную команду, как только оно появится (:h :autocmd http://vimdoc.sourceforge.net/htmldoc/autocmd.html#:autocmd). В данном случае настраивается реакция на событие FileType, которое генерируется, когда Vim определяет тип текущего файла.

Для одного и того же события можно предусмотреть выполнение нескольких команд autocmd. Допустим, что нам требуется использовать программу nodelint в качестве компилятора для файлов JavaScript. С этой целью мы могли бы добавить следующую строку в пример выше:

autocmd FileType javascript compiler nodelint

Обе команды будут выполняться всякий раз, когда событие FileType окажется сгенерировано для файла JavaScript.

Добавление подобных команд в файл vimrc отлично подходит для случая, когда вам необходимо изменить один-два параметра настройки для файлов некоторого типа. Но если требуется применить массу настроек, файл начинает разрастаться непомерно. Решением проблемы может стать расширение ftplugin — альтернативный механизм применения настроек, зависящих от типов файлов. Вместо