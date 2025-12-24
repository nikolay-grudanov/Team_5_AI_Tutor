---
source_image: page_312.png
page_number: 312
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.66
tokens: 11391
characters: 764
timestamp: 2025-12-24T10:31:06.668170
finish_reason: stop
---

Для проверки корректности работы нашей программы, значения переменных выводятся в консоль. Далее, запустим нашу программу со следующими аргументами: `test` и `sample.txt`:

```
$ cargo run -- test sample.txt
    Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
        Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

Отлично, программа работает! Нам нужно чтобы значения аргументов были сохранены в правильных переменных. Позже мы добавим обработку ошибок с некоторыми потенциальными ошибочными ситуациями, например, когда пользователь не предоставляет аргументы; сейчас мы проигнорируем эту ситуацию и поработаем над добавлением возможности чтения файла.