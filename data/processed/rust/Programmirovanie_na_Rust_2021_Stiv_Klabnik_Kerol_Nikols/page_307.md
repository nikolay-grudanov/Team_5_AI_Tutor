---
source_image: page_307.png
page_number: 307
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.63
tokens: 7539
characters: 2246
timestamp: 2025-12-24T10:53:55.645586
finish_reason: stop
---

чувствительный к регистру. Нас интересует не само значение переменной среды, а только то, что оно задано, поэтому мы проверяем is_err, не используя методы unwrap, expect или любые другие, которые мы видели в типе Result.

Мы передаем значение переменной case_sensitive в экземпляр структуры Config, благодаря чему функция run может прочитать это значение и принять решение о том, какую функцию следует вызывать — search или search_case_insensitive, как это было реализовано в листинге 12.22.

Давайте попробуем это сделать! Сначала выполним программу без заданной переменной среды и с запросом to, который должен совпасть с любой строкой текста со словом to в нижнем регистре:

$ cargo run to poem.txt
    Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
    Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!

Похоже, пока что все работает! Теперь давайте выполним программу с использованием переменной среды CASE_INSENSITIVE, равной 1, но с тем же запросом to.

Если вы используете PowerShell, то нужно будет установить переменную среды и выполнить программу двумя командами, а не одной:

$ $env:CASE_INSENSITIVE=1
$ cargo run to poem.txt

Мы должны получить строки со словом to, которые могут иметь буквы в верхнем регистре:

$ CASE_INSENSITIVE=1 cargo run to poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
    Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
To tell your name the livelong day
To an admiring bog!

Отлично! У нас также есть строки текста, содержащие To! Программа minigrep теперь может выполнять нечувствительный к регистру поиск под управлением переменной среды. Таким образом, вы знаете, как управлять вариантами, заданными с аргументами командной строки и переменными среды.

Некоторые программы одновременно допускают и аргументы, и переменные среды для одной и той же конфигурации. В этих случаях принимается решение о приоритете одного либо другого. В качестве еще одного самостоятельного упражнения попробуйте поиграть с нечувствительностью к регистру посредством аргумента командной строки либо переменной среды. Примите решение о прио-