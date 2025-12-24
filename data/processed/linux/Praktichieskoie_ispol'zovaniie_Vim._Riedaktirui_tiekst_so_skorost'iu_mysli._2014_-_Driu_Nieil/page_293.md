---
source_image: page_293.png
page_number: 293
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.49
tokens: 5622
characters: 1734
timestamp: 2025-12-24T04:15:45.924425
finish_reason: stop
---

Рецепт 96. Поиск и замена в нескольких файлах

Команда подстановки действует в пределах текущего файла. А как быть, если нам потребуется применить ту же команду подстановки ко всему проекту? Подобная необходимость часто возникает на практике, однако редактор Vim не имеет отдельной команды поиска с заменой, которую можно было применить ко всему проекту. Впрочем, в этом нет необходимости, данную функциональность можно получить, объединив пару простых команд.

Начнем со знакомства с сырым, но эффективным решением, а затем посмотрим, как его улучшить. Для демонстрации мы будем использовать каталог refactor-project, который можно найти в пакете с загружаемыми примерами к книге. Ниже приводятся файлы, находящиеся в нем, и их содержимое:

refactor-project/
    about.txt
    Pragmatic Vim is a hands-on guide to working with Vim.

    credits.txt
    Pragmatic Vim is written by Drew Neil.

    license.txt
    The Pragmatic Bookshelf holds the copyright for this book.

    extra/
        praise.txt
        What people are saying about Pragmatic Vim...

        titles.txt
        Other titles from the Pragmatic Bookshelf...

Каждый из этих файлов содержит слово «Pragmatic» либо как часть фразы «Pragmatic Bookshelf», либо как часть фразы «Pragmatic Vim». Нам нужно найти каждое вхождение фразы «Pragmatic Vim» и заменить ее на «Practical Vim», оставив фразы «Pragmatic Bookshelf» нетронутыми.

Если вы желаете опробовать примеры ниже, загрузите пакет с исходными текстами со страницы книги на сайте Pragmatic Bookshelf. Прежде чем открыть Vim, перейдите в каталог refactor-project.

Команда подстановки

Начнем с создания команды подстановки. Нам нужно сконструировать шаблон, который совпадал бы со словом «Pragmatic» во фра-