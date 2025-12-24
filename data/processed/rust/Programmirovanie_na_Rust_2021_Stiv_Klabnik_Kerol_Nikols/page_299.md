---
source_image: page_299.png
page_number: 299
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.76
tokens: 7464
characters: 1927
timestamp: 2025-12-24T10:53:36.903946
finish_reason: stop
---

= help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `query` or `contents`

Компилятор не может знать, какой из двух аргументов нам нужен, поэтому мы должны сообщить об этом. Поскольку аргумент contents содержит весь текст, а мы хотим вернуть совпадающие части этого текста, мы знаем, что contents — именно тот аргумент, который нужно соединить с возвращаемым значением, используя синтаксис жизненного цикла.

В других языках программирования не требуется соединять аргументы с возвращаемыми значениями в сигнатуру. Хотя на первый взгляд, возможно, это покажется странным, но со временем все станет проще. Возможно, вы захотите сравнить этот пример с примером из раздела «Проверка ссылок с помощью жизненных циклов» (с. 235).

А теперь давайте выполним тест:

$ cargo test
    Compiling minigrep v0.1.0 (file:///projects/minigrep)
--warnings--
    Finished dev [unoptimized + debuginfo] target(s) in 0.43 secs
    Running target/debug/deps/minigrep-abcabcabc

running 1 test
test tests::one_result ... FAILED

failures:

---- tests::one_result stdout ----
    thread 'tests::one_result' panicked at 'assertion failed: `(left == right)`
left: `["safe, fast, productive."]`,
right: `[]`)', src/lib.rs:48:8
note: Run with `RUST_BACKTRACE=1` for a backtrace.

failures:
    tests::one_result

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out

error: test failed, to rerun pass '--lib'

Великолепно! Тест не сработал, как мы и ожидали. Давайте сделаем так, чтобы тест завершался успешно!

Написание кода для успешного завершения теста

В настоящее время наш тест не срабатывает, потому что мы всегда возвращаем пустой вектор. Для того чтобы это исправить и реализовать функцию search, программа должна выполнить следующие действия:

1. Перебрать каждую строку содержимого.
2. Проверить, содержит ли строка содержимого строку запроса.