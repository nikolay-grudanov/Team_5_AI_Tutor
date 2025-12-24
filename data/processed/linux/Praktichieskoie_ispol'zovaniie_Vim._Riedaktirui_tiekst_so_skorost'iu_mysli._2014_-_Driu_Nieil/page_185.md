---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.79
tokens: 5545
characters: 1410
timestamp: 2025-12-24T04:13:21.392450
finish_reason: stop
---

Для каждого буфера поддерживается свой список изменений, в отличие от списка переходов, который поддерживается для каждого окна.

Рецепт 57. Переход к файлу с именем под курсором

Имена файлов в документе могут интерпретироваться редактором Vim как своеобразные гиперссылки. При правильных настройках можно использовать команду gf для перехода к файлам с именами под курсором.

Для демонстрации воспользуемся каталогом jumps, который находится в пакете с загружаемыми примерами к книге. Он содержит следующее дерево подкаталогов:

practical_vim.rb
practical_vim/
    core.rb
    jumps.rb
    more.rb
    motions.rb

Сначала перейдите в каталог jumps в командной оболочке, а затем запустите редактор Vim. Для данной демонстрации я рекомендую использовать флаги -u NONE -N, обеспечивающие запуск Vim без загрузки дополнительных расширений:

⇒ $ cd code/jumps
⇒ $ vim -u NONE -N practical_vim.rb

Файл practical_vim.rb содержит только инструкции загрузки файлов core.rb и more.rb:

jumps/practical_vim.rb
http://media.pragprog.com/titles/dnvim/code/jumps/practical_vim.rb

require 'practical_vim/core'
require 'practical_vim/more'

Разве не было бы полезно иметь возможность быстро взглянуть на содержимое файла, указанного в директиве require? Именно для этих целей существует команда gf. Ее имя можно расшифровать как «go to file» (перейти к файлу) (:h gf http://vimdoc.sourceforge.net/htmldoc/editing.html#gf).