---
source_image: page_272.png
page_number: 272
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.21
tokens: 5309
characters: 582
timestamp: 2025-12-24T04:15:06.997627
finish_reason: stop
---

Рецепт 86. Поиск текущего визуального выделения

Этот фрагмент можно вставить в файл vimrc непосредственно или установить расширение, реализующее данную функциональность¹.

Помимо команды *, мы также переопределили команду #, кото-
рая теперь будет выполнять поиск текущего выделения в обратном направлении. Ключевое слово xnoremap указывает, что данная при-
вязка должна действовать в визуальном режиме, но не должна дей-
ствовать в режиме выделения (см. :h mapmode-x http://vimdoc.
sourceforge.net/htmldoc/map.html#mapmode-x).

¹ https://github.com/nelstrom/vim-visual-star-search