---
source_image: page_357.png
page_number: 357
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.79
tokens: 5604
characters: 1512
timestamp: 2025-12-24T04:16:57.712171
finish_reason: stop
---

⇒ :set spell
⇒ :set spelllang=en_us

После этого слово «moustache» будет помечаться как ошибочное, а «mustache» будет рассматриваться как правильное. В число других поддерживаемых диалектов входят: en_au, en_ca, en_gb и en_nz. Подробности смотрите в разделе справки :h spell-remarks http://vimdoc.sourceforge.net/htmldoc/spell.html#spell-remarks.

Получение словарей для других языков

В состав дистрибутива Vim входит только орфографический словарь английского языка, однако вы можете найти десятки словарей для других языков по адресу http://ftp.vim.org/vim/runtime/spell/.

Если попытаться настроить проверку орфографии языка, для которого отсутствует файл словаря, Vim предложит загрузить и установить его:

⇒ :set spell
⇒ :set spelllang=ru
Cannot find spell file for “ru” in utf-8
Do you want me to try downloading it?
(Y)es, [N]o:
⇒ Y
Downloading ru.utf-8.spl
In which directory do you want to write the file:
1. /Users/drew/.vim/spell
2. /Applications/MacVim.app/Contents/Resources/vim/runtime/spell
[C]ancel, (1), (2):

Эта возможность поддерживается посредством расширения с именем spellfile.vim, который входит в состав дистрибутива Vim (см. :h spellfile.vim http://vimdoc.sourceforge.net/htmldoc/spell.html#spellfile.vim). Чтобы он заработал, добавьте следующие две строки в файл vimrc (в самый конец):

set nocompatible
plugin on

Рецепт 120. Добавление слов в орфографический словарь

Орфографические словари не претендуют на абсолютную полноту, и у нас есть возможность добавлять в них новые слова.