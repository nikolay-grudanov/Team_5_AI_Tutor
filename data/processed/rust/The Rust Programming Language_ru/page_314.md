---
source_image: page_314.png
page_number: 314
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.09
tokens: 11589
characters: 1412
timestamp: 2025-12-24T10:31:37.505686
finish_reason: stop
---

После этого выражения мы снова добавили временный вывод `println!` для печати значения `contents` после чтения файла, поэтому мы можем проверить, что программа работает.

Давайте запустим этот код с любой строкой в качестве первого аргумента командной строки (потому что мы ещё не реализовали поисковую часть) и файл poem.txt как второй аргумент:

```
$ cargo run -- the poem.txt
Compiling minigrep v0.1.0 (file:///projects/minigrep)
Finished dev [unoptimized + debuginfo] target(s) in 0.0s
    Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us – don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

Отлично! Этот код прочитал и затем печатал содержимое файла. Хотя наша программа решает поставленную задачу, она не лишена недостатков. Прежде всего, функция `main` решает множество задач. Такую функцию неудобно тестировать. Далее, не отслеживаются возможные ошибки ввода данных. Пока наша программа небольшая, то данными недочётами можно пренебречь. При увеличении размеров программы, такую программу будет всё сложнее и сложнее поддерживать. Хорошей практикой программирования является ранний рефакторинг кода по мере усложнения. Поэтому, далее мы улучшим наш код с помощью улучшения его структуры.