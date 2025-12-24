---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.35
tokens: 5910
characters: 1139
timestamp: 2025-12-24T04:05:40.366102
finish_reason: stop
---

$ echo "The variable HOME has value $HOME' The variable HOME has value $HOME $ echo "The variable HOME has value $HOME" The variable HOME has value /home/smith

При использовании обратных кавычек их содержимое воспринимается как команда; в этом случае содержимое заменяется стандартным потоком вывода этой команды.

$ /usr/bin/whoami
smith
$ echo My name is "/usr/bin/whoami"
My name is smith

Маскировка

Если символ имеет специальный смысл для командного процессора, а вы хотите использовать его в строке (например, символ "*" - это знак сноски в обычном тексте, а не групповой символ), то поставьте перед этим символом левую косую черту "\". Это называется маскировкой специального символа.

$ echo a*    Здесь * является групповым символом для подбора файлов с именами начинающимися с буквы "a"

aardvark agnostic apple
$ echo a\*  Здесь *является простым символом a*
$ echo "I live in $HOME"  Символ доллара означает значение переменной
I live in /home/smith
$ echo "I live in \$HOME"  Обычный символ доллара
I live in $HOME

Также вы можете маскировать управляющие символы (табуляции, новой строки, ^D и т. д.), чтобы использовать их