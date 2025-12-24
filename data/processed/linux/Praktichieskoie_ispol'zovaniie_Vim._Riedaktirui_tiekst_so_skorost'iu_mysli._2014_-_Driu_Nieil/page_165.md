---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.20
tokens: 5822
characters: 2073
timestamp: 2025-12-24T04:13:01.711870
finish_reason: stop
---

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Find the first occurrence of {char} and move to it.</td>
  </tr>
  <tr>
    <td>fo</td>
    <td>Find the first occurrence of {char} and move to it.</td>
  </tr>
  <tr>
    <td>;;</td>
    <td>Find the first occurrence of {char} and move to it.</td>
  </tr>
  <tr>
    <td>;</td>
    <td>Find the first occurrence of {char} and move to it.</td>
  </tr>
</table>

Случайно промахнувшись, мы можем вернуться назад командой ,. Она повторит последний поиск f{char}, но в обратном направлении (см. :h , http://vimdoc.sourceforge.net/htmldoc/motion.html#).

Вспомните мантру из рецепта 4 в главе 1: действие, повтор, возврат. Я думаю о , как о подушке безопасности, когда чересчур рьяно нажимаю клавишу ;.

Не забывайте команду повторения поиска символа в обратном направлении

Vim практически каждой клавише на клавиатуре присваивает какую-нибудь функцию. Если вы желаете создать собственный набор привязок к клавишам, как это реализовать? Vim предоставляет клавишу <Leader>, играющую роль пространства имен команд, определяемых пользователем. Ниже показано, как создать собственные привязки с использованием <Leader>:

noremap <Leader>n nzz
noremap <Leader>N Nzz

По умолчанию роль клавиши <Leader> играет клавиша \, поэтому определенные выше команды можно вызывать нажатием последовательностей \n и \N. Чтобы узнать, что делают эти новые команды, загляните в справку :h zz http://vimdoc.sourceforge.net/htmldoc/scroll.html#zz.

На некоторых клавиатурах клавиша \ расположена очень неудобно, поэтому Vim упрощает замену клавиши <Leader> (см. :h mapleader http://vimdoc.sourceforge.net/htmldoc/map.html#mapleader). Обычно эту клавишу привязывают к клавише «запятая». Если вы пойдете таким путем, надо привязать функцию повторения поиска символа в обратном направлении к какой-нибудь другой клавише. Например:

let mapleader=","
noremap \ ,

Команды ; и , дополняют друг друга. Если одну из них выбросить, все семейство команд поиска символа станет менее ценным.