---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.83
tokens: 5664
characters: 1709
timestamp: 2025-12-24T04:13:18.657062
finish_reason: stop
---

set nocompatible
filetype plugin on
runtime macros/matchit.vim

Возможности, поддерживаемые этим расширением, имеют большую практическую ценность, поэтому я рекомендую включить его у себя. За дополнительной информацией обращайтесь к разделу справки :h matchit-install http://vimdoc.sourceforge.net/htmldoc/usr_05.html#matchit-install.

Surround.vim

Расширение surround.vim, написанное Тимом Поупом (Tim Pope)1, является одним из моих любимых расширений. Оно позволяет легко заключить выделенный фрагмент в пару символов-ограничителей. Например, ниже показано, как с его помощью можно было бы заключить пару слов New York в кавычки:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>cities = ["London", "Berlin", <b>New York</b>]</td>
  </tr>
  <tr>
    <td>vee</td>
    <td>cities = ["London", "Berlin", <b>New York</b>]</td>
  </tr>
  <tr>
    <td>S"</td>
    <td>cities = ["London", "Berlin", <b>"New York"</b>]</td>
  </tr>
</table>

Расширение surround.vim предоставляет команду S", которую можно интерпретировать как «Surround the selection with a pair of double quote marks» (окружить выделение парой двойных кавычек). Точно также можно окружить выделение парой круглых или фигурных скобок, применив команду S) или S}.

С помощью surround.vim можно даже заменить имеющиеся символы-ограничители. Например, заменить {London} на [London] можно с помощью команды cs]], которую можно интерпретировать как «Change surrounding {} braces to [] brackets» (заменить окружающие скобки {} на []). Обратную замену можно выполнить командой cs]]. Это очень мощное расширение, обязательно установите его себе.

1 http://github.com/tpope/vim-surround