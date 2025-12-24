---
source_image: page_223.png
page_number: 223
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.81
tokens: 5491
characters: 1261
timestamp: 2025-12-24T04:14:05.222815
finish_reason: stop
---

буется добавить команду в начало или в середину макроса, мы не сможем воспользоваться этим способом. В рецепте 71 ниже описывается более мощный прием исправления макроса после его записи.

Рецепт 69. Выполнение операций над множеством файлов

До сих пор мы имели дело с операциями, повторно выполняемыми в пределах одного файла, однако макросы с тем же успехом можно применять к коллекциям файлов. В этом рецепте мы снова будем рассматривать приемы последовательного и параллельного выполнения макросов.
Допустим, что у нас имеется множество файлов, содержащих примерно такой текст:

macros/ruby_module/animal.rb
http://media.pragprog.com/titles/dnvim/code/macros/ruby_module/animal.rb

# ...[end of copyright notice]
class Animal
    # implementation
end

Нам нужно заключить определение класса в модуль, как показано ниже:

# ...[end of copyright notice]
module Rank
    class Animal
        # implementation...
    end
end

Подготовка

Для успешного воспроизведения примеров в этом рецепте добавьте следующие строки в свой конфигурационный файл:

macros/rc.vim
http://media.pragprog.com/titles/dnvim/code/macros/rc.vim

set nocompatible
filetype plugin indent on
set hidden
if has("autocmd")
    autocmd FileType ruby setlocal ts=2 sts=2 sw=2 expandtab
endif