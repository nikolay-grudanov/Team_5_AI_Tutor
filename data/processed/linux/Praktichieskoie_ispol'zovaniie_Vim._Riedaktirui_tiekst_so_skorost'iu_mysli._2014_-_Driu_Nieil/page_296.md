---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.45
tokens: 5688
characters: 1922
timestamp: 2025-12-24T04:15:49.212786
finish_reason: stop
---

Рецепт 96. Поиск и замена в нескольких файлах

⇒ /Pragmatic\ze Vim
⇒ :vimgrep /<C-r>// **/*.txt

Последовательность нажатий <C-r>/ вставит последний использовавшийся шаблон. Мы снова используем последовательность групповых символов **/*.txt, чтобы вынудить команду vimgrep просмотреть все файлы, находящиеся в текущем каталоге и во вложенных подкаталогах.

Каждое совпадение, возвращаемое командой vimgrep, записывается в список результатов (quickfix list) (см. главу 17 «Компиляция кода и обзор ошибок с помощью Quickfix List»). Ознакомиться с результатами поиска можно с помощью команды :copen, которая открывает окно со списком результатов. Но нам не нужны результаты как таковые, нам нужно применить команду подстановки ко всем файлам, оказавшимся в этом списке.

Было бы очень удобно, если бы Vim поддерживал команду :quickfixdo, но такой команды нет. Поэтому мы будем использовать следующий небольшой сценарий на языке Vim:

substitution/qargs.vim
http://media.pragprog.com/titles/dnvim/code/substitution/qargs.vim

command! -nargs=0 -bar Qargs execute 'args' QuickfixFilenames()
function! QuickfixFilenames()
    let buffer_numbers = {}
    for quickfix_item in getqflist()
        let buffer_numbers[quickfix_item['bufnr']] = bufname(quickfix_item['bufnr'])
    endfor
    return join(map(values(buffer_numbers), 'fnameescape(v:val)'))
endfunction

Вы можете добавить этот код в свой файл vimrc или установить его как расширение¹.

Теперь можно вызвать команду :Qargs, которая заполнит список аргументов именами файлов из списка результатов (quickfix list). Если теперь применить команду подстановки к каждому из файлов в списке аргументов, можно быть уверенными, что подстановка будет выполнена только в файлах, содержащих совпадения с искомым шаблоном. Можно также отбросить флаг e, так как в данном случае команда подстановки не должна генерировать сообщения об ошибках:

¹ https://github.com/nelstrom/vim-qargs