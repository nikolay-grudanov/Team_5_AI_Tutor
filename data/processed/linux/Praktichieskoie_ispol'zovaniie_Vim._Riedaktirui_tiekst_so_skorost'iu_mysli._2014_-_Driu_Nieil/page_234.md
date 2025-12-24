---
source_image: page_234.png
page_number: 234
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.49
tokens: 5261
characters: 434
timestamp: 2025-12-24T04:14:18.863864
finish_reason: stop
---

Рецепт 71. Правка содержимого макроса

функцию substitute() (которая не имеет ничего общего с командой :substitute! См. :h substitute() i http://vimdoc.sourceforge.net/htmldoc/eval.html#substitute()):

⇒ :let @a=substitute(@a, '\~', 'vU', 'g')

Если вас заинтересовала такая возможность, загляните в справку :h function-list i http://vimdoc.sourceforge.net/htmldoc/usr_41.html#function-list, где можно найти дополнительную информацию.