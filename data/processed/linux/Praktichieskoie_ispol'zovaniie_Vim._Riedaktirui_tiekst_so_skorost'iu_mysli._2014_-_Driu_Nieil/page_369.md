---
source_image: page_369.png
page_number: 369
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.76
tokens: 5410
characters: 1013
timestamp: 2025-12-24T04:17:05.015932
finish_reason: stop
---

объявления наших предпочтений в отношении файлов JavaScript в файле vimrc с помощью autocmd мы можем поместить их в файл с именем ~/.vim/after/ftplugin/javascript.vim:

customizations/ftplugin/javascript.vim
http://media.pragprog.com/titles/dnvim/code/customizations/ftplugin/javascript.vim

setlocal ts=4 sts=4 sw=4 noet
compiler nodelint

Этот файл имеет точно такую же организацию, как и файл vimrc, за исключением того, что настройки из него применяются только к файлам JavaScript. Точно так же мы могли бы создать файл ftplugin/ruby.vim с целью хранения настроек для языка Ruby, как и для каждого типа файлов, с которыми приходится работать регулярно. Дополнительные подробности можно найти в разделе справки :h ftplugin-name http://vimdoc.sourceforge.net/htmldoc/usr_05.html#ftplugin-name.

Для работы механизма ftplugin необходимо гарантировать включение обоих механизмов: определения типа файлов и поддержку расширений. Убедитесь, что в вашем файле vimrc присутствует следующая строка:

filetype plugin on