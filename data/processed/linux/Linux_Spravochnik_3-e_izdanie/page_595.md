---
source_image: page_595.png
page_number: 595
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.19
tokens: 11672
characters: 1330
timestamp: 2025-12-24T03:41:57.790404
finish_reason: stop
---

%у   Текущий год (99, 00 и т. д.).
%В   Начало полужирного выделения.
%C   Аналогично %c, но с использованием абсолютных имен, а не записи через ~.
%D   Число месяца (09, 10 и т. д.).
%M   Полное имя узла.
%P   Текущее время с точностью до секунды (в 24-часовом формате).
%S   Начало инверсного выделения (reverse video).
%T   Текущее время (в 24-часовом формате).
%U   Начало подчеркивания.
%W   Текущий месяц (09, 10 и т. д.).
%Y   Текущий год (1999, 2000 и т. д.).

Пример файла .cshrc

# Предопределенные переменные

set path=(~ ~/bin /usr/ucb /bin /usr/bin .)
set mail=(/usr/mail/tom)

if ($?prompt) then      # настройки для диалогового режима
    set echo
    set noclobber ignoreeof

    set cdpah=(/usr/lib /usr/spool/uucp)
    # Теперь можно вводить команду cd macros вместо cd /usr/lib/macros

    set history=100
    set prompt='tom \!% '      # содержит номер команды
    set time=3

# Мои переменные

    set man1="/usr/man/man1"     # теперь можно использовать cd $man1, ls $man1
    set a="[a-z]*"               # а также vi $a
    set A="[A-Z]*"               # или grep string $A

# Псевдонимы

alias c "clear; dirs"        # кавычки экранируют ; или |
alias h "history|more"
alias j jobs -l
alias ls ls -sFC             # переопределяем команду ls
alias del 'mv \!* ~/tmp_dir' # безопасная альтернатива rm
endif