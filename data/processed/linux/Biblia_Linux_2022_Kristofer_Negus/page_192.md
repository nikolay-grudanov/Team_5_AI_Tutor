---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.76
tokens: 7563
characters: 2229
timestamp: 2025-12-24T04:50:23.971284
finish_reason: stop
---

Позиционные параметры оболочки

Существуют специальные переменные, которые назначает оболочка. Набор часто используемых символов называется позиционными параметрами аргументов командной строки. Они указываются в виде значений $0, $1, $2, $3... $n. $0 — особенный, ему присваивается имя, используемое для вызова скрипта, остальным присваиваются значения параметров, передаваемых в командной строке, в том порядке, в котором они появились.

Предположим, что скрипт оболочки с именем myscript содержит:

#!/bin/bash
# Script to echo out command-line arguments
echo "The first argument is $1, the second is $2."
echo "The command itself is called $0."
echo "There are $# parameters on your command line"
echo "Here are all the arguments: $@"

Допустим, что скрипт является исполняемым и находится в каталоге $PATH, тогда вот что произойдет, если запустить эту команду с аргументами foo и bar:

$ chmod 755 /home/chris/bin/myscript
$ myscript foo bar
The first argument is foo, the second is bar.
The command itself is called /home/chris/bin/myscript.
There are 2 parameters on your command line
Here are all the arguments: foo bar

Как видно в примере, позиционный параметр $0 — это полный или относительный путь к myscript, $1 — к foo, а $2 — к bar.

Другая переменная, #$, сообщает, сколько параметров было задано в скрипте. В этом примере переменная #$ будет равна 2. Переменная $@ содержит все аргументы, введенные в командной строке. Другой специальной переменной оболочки является $?, которая получает статус выхода последней выполненной команды. Как правило, нулевое значение означает, что команда завершилась успешно, а все, что не равно нулю, указывает на ошибку. Полный список позиционных параметров оболочки см. в руководстве bash.

Чтение параметров

С помощью команды read можно запросить у пользователя информацию и сохранить ее для последующего использования в скрипте. Пример скрипта с командой read:

#!/bin/bash
read -p "Type in an adjective, noun and verb (past tense): " adj1 noun1 verb1
echo "He sighed and $verb1 to the elixir. Then he ate the $adj1 $noun1."

В примере после того, как скрипт запросил прилагательное (adjective), существительное (noun) и глагол (verb), пользователь должен ввести слова, которые